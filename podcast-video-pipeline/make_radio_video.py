#!/usr/bin/env python3
"""
make_radio_video.py — 팟캐스트 mp3 → 슬라이드쇼 영상(mp4) 자동화 파이프라인.

단계:
  1. transcribe()             : faster-whisper STT → output/transcript.json
  2. segment()                : transcript를 N개 구간으로 분할 (문장 경계 기준)
  3. generate_image_prompts() : Gemini 텍스트 모델로 이미지 프롬프트 생성 → output/image_prompts.json
  4. generate_images()        : Gemini 이미지 모델(nano banana)로 이미지 생성 → output/images/img_NNN.png
  5. assemble_video()         : ffmpeg로 이미지 + 오디오 합성 → output/output.mp4

실행 예:
  python make_radio_video.py --input input/podcast.mp3 --segments 100
  python make_radio_video.py --input input/podcast.mp3 --dry-run
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import random
import shutil
import subprocess
import sys
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any, Callable, Optional, TypeVar

log = logging.getLogger("make_radio_video")

T = TypeVar("T")

# ── 기본 설정 (config.yaml / CLI 인자로 덮어쓰기 가능) ──────────────────────
DEFAULT_CONFIG: dict[str, Any] = {
    "segments": 100,
    "output_dir": "output",
    "whisper_model": "small",          # tiny / base / small / medium / large-v3
    "language": "ko",
    "text_model": "gemini-2.5-flash",
    "image_model": "gemini-2.5-flash-image",   # "nano banana"
    "style_guide": (
        "따뜻하고 밝은 톤, 고령층이 편안하게 볼 수 있는 삽화 스타일, "
        "부드러운 파스텔 색감, 자극적이지 않은 평화로운 분위기, "
        "warm and bright tone, gentle storybook illustration for senior viewers"
    ),
    "resolution": "1280x720",
    "fps": 24,
    "crossfade": 0.0,                  # 초 단위. 0이면 크로스페이드 없음
    "subtitles": False,                # 자막 오버레이 여부
    "max_retries": 5,
    "retry_base_delay": 2.0,           # 지수 백오프 기본 대기(초)
}

DRY_RUN_SEGMENTS = 5


# ── 데이터 구조 ──────────────────────────────────────────────────────────────
@dataclass
class TranscriptSegment:
    """faster-whisper가 반환한 문장 단위 구간."""
    start: float
    end: float
    text: str


@dataclass
class SlideSegment:
    """이미지 1장이 담당하는 오디오 구간 (여러 문장 묶음)."""
    index: int
    start: float
    end: float
    text: str
    prompt: Optional[str] = None


# ── 공통 유틸 ────────────────────────────────────────────────────────────────
def retry_with_backoff(
    fn: Callable[[], T],
    *,
    what: str,
    max_retries: int,
    base_delay: float,
) -> T:
    """API 호출 실패(rate limit 등) 시 지수 백오프 재시도."""
    for attempt in range(max_retries):
        try:
            return fn()
        except Exception as exc:  # noqa: BLE001 — SDK 예외 종류가 다양함
            if attempt == max_retries - 1:
                raise
            delay = base_delay * (2 ** attempt) + random.uniform(0, 1)
            log.warning(
                "%s 실패 (%d/%d회): %s — %.1f초 후 재시도",
                what, attempt + 1, max_retries, exc, delay,
            )
            time.sleep(delay)
    raise RuntimeError("unreachable")


def load_config(config_path: Path) -> dict[str, Any]:
    """config.yaml이 있으면 기본값에 병합."""
    config = dict(DEFAULT_CONFIG)
    if config_path.exists():
        import yaml
        with open(config_path, encoding="utf-8") as f:
            user_cfg = yaml.safe_load(f) or {}
        config.update({k: v for k, v in user_cfg.items() if v is not None})
        log.info("설정 파일 로드: %s", config_path)
    return config


def get_api_key() -> str:
    """`.env` 또는 환경변수에서 Gemini API 키 로드."""
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass
    key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key:
        sys.exit(
            "오류: GEMINI_API_KEY가 설정되지 않았습니다. "
            ".env 파일에 GEMINI_API_KEY=... 를 추가하세요."
        )
    return key


def get_genai_client() -> Any:
    from google import genai
    return genai.Client(api_key=get_api_key())


def probe_audio_duration(audio_path: Path) -> float:
    """ffprobe로 오디오 전체 길이(초)를 구한다."""
    result = subprocess.run(
        [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(audio_path),
        ],
        capture_output=True, text=True, check=True,
    )
    return float(result.stdout.strip())


def format_srt_time(seconds: float) -> str:
    ms = int(round(seconds * 1000))
    h, rem = divmod(ms, 3_600_000)
    m, rem = divmod(rem, 60_000)
    s, ms = divmod(rem, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


# ── 1단계: STT ───────────────────────────────────────────────────────────────
def transcribe(
    audio_path: Path,
    output_dir: Path,
    *,
    model_size: str,
    language: str,
    force: bool = False,
) -> list[TranscriptSegment]:
    """faster-whisper로 음성인식 후 transcript.json 저장. 이미 있으면 재사용."""
    transcript_path = output_dir / "transcript.json"
    if transcript_path.exists() and not force:
        log.info("[1/5] transcript.json이 이미 존재 — STT 건너뜀 (%s)", transcript_path)
        with open(transcript_path, encoding="utf-8") as f:
            data = json.load(f)
        return [TranscriptSegment(**s) for s in data["segments"]]

    log.info("[1/5] STT 시작: %s (모델=%s, 언어=%s)", audio_path, model_size, language)
    from faster_whisper import WhisperModel

    model = WhisperModel(model_size, device="auto", compute_type="auto")
    raw_segments, info = model.transcribe(
        str(audio_path), language=language, vad_filter=True,
    )

    segments: list[TranscriptSegment] = []
    for seg in raw_segments:
        text = seg.text.strip()
        if not text:
            continue
        segments.append(TranscriptSegment(start=seg.start, end=seg.end, text=text))
        log.info("  [%7.1fs ~ %7.1fs] %s", seg.start, seg.end, text[:60])

    if not segments:
        sys.exit("오류: 음성인식 결과가 비어 있습니다. 입력 오디오를 확인하세요.")

    payload = {
        "audio": str(audio_path),
        "language": info.language,
        "duration": info.duration,
        "segments": [asdict(s) for s in segments],
    }
    with open(transcript_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    log.info("[1/5] STT 완료: 문장 %d개 → %s", len(segments), transcript_path)
    return segments


# ── 2단계: 세그먼트 분할 ─────────────────────────────────────────────────────
def segment(
    transcript_segments: list[TranscriptSegment],
    num_segments: int,
    audio_duration: float,
) -> list[SlideSegment]:
    """문장 경계를 유지하면서 전체 오디오를 약 num_segments개 구간으로 분할."""
    n = min(num_segments, len(transcript_segments))
    if n < num_segments:
        log.warning(
            "[2/5] 문장 수(%d)가 요청 세그먼트 수(%d)보다 적어 %d개로 조정",
            len(transcript_segments), num_segments, n,
        )

    origin = transcript_segments[0].start
    total = transcript_segments[-1].end - origin

    groups: list[list[TranscriptSegment]] = []
    current: list[TranscriptSegment] = []
    for i, seg in enumerate(transcript_segments):
        current.append(seg)
        remaining_sentences = len(transcript_segments) - i - 1
        remaining_groups = n - len(groups) - 1
        # 다음 그룹 경계(누적 목표 시각)를 넘었고, 남은 문장으로 남은 그룹을
        # 채울 수 있으면 문장 경계에서 그룹 마감
        boundary = origin + total * (len(groups) + 1) / n
        if remaining_groups > 0 and seg.end >= boundary and remaining_sentences >= remaining_groups:
            groups.append(current)
            current = []
    if current:
        groups.append(current)

    slides: list[SlideSegment] = []
    for idx, group in enumerate(groups):
        start = 0.0 if idx == 0 else slides[-1].end
        end = audio_duration if idx == len(groups) - 1 else group[-1].end
        slides.append(SlideSegment(
            index=idx + 1,
            start=start,
            end=end,
            text=" ".join(g.text for g in group),
        ))

    log.info(
        "[2/5] 세그먼트 분할 완료: %d개 (평균 %.1f초)",
        len(slides), audio_duration / len(slides),
    )
    return slides


# ── 3단계: 이미지 프롬프트 생성 ──────────────────────────────────────────────
PROMPT_TEMPLATE = """당신은 라디오 팟캐스트 영상의 삽화 프롬프트 작가입니다.
아래는 팟캐스트의 한 구간 내용입니다:

---
{text}
---

이 내용을 표현하는 이미지 생성용 영어 프롬프트를 1개만 작성하세요.

규칙:
- 반드시 다음 스타일을 반영: {style_guide}
- 텍스트/글자가 이미지에 나타나지 않도록 "no text" 포함
- 사람 얼굴 클로즈업보다는 장면/풍경/상징 중심
- 프롬프트 문장만 출력 (설명, 따옴표, 번호 금지)"""


def generate_image_prompts(
    slides: list[SlideSegment],
    output_dir: Path,
    *,
    client: Any,
    text_model: str,
    style_guide: str,
    max_retries: int,
    retry_base_delay: float,
    force: bool = False,
) -> list[SlideSegment]:
    """세그먼트별 이미지 프롬프트를 Gemini 텍스트 모델로 생성, 매 건마다 저장."""
    prompts_path = output_dir / "image_prompts.json"

    # 기존 결과 재사용 (idempotent): 같은 텍스트의 프롬프트는 다시 만들지 않음
    existing: dict[int, dict[str, Any]] = {}
    if prompts_path.exists() and not force:
        with open(prompts_path, encoding="utf-8") as f:
            for item in json.load(f):
                existing[item["index"]] = item

    def save() -> None:
        with open(prompts_path, "w", encoding="utf-8") as f:
            json.dump([asdict(s) for s in slides], f, ensure_ascii=False, indent=2)

    total = len(slides)
    for slide in slides:
        cached = existing.get(slide.index)
        if cached and cached.get("prompt") and cached.get("text") == slide.text:
            slide.prompt = cached["prompt"]
            log.info("[3/5] 프롬프트 %d/%d — 기존 결과 재사용", slide.index, total)
            continue

        log.info("[3/5] 프롬프트 %d/%d 생성 중...", slide.index, total)
        request_text = PROMPT_TEMPLATE.format(text=slide.text, style_guide=style_guide)

        def call() -> str:
            response = client.models.generate_content(
                model=text_model, contents=request_text,
            )
            result = (response.text or "").strip()
            if not result:
                raise ValueError("빈 응답")
            return result

        slide.prompt = retry_with_backoff(
            call,
            what=f"프롬프트 {slide.index} 생성",
            max_retries=max_retries,
            base_delay=retry_base_delay,
        )
        save()

    save()
    log.info("[3/5] 이미지 프롬프트 %d개 완료 → %s", total, prompts_path)
    return slides


# ── 4단계: 이미지 생성 (nano banana) ────────────────────────────────────────
def generate_images(
    slides: list[SlideSegment],
    images_dir: Path,
    *,
    client: Any,
    image_model: str,
    max_retries: int,
    retry_base_delay: float,
) -> list[Path]:
    """프롬프트별 이미지 생성. 이미 존재하는 파일은 건너뜀 (재시작 가능)."""
    from google.genai import types

    images_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    total = len(slides)

    for slide in slides:
        image_path = images_dir / f"img_{slide.index:03d}.png"
        paths.append(image_path)

        if image_path.exists() and image_path.stat().st_size > 0:
            log.info("[4/5] 이미지 %d/%d — 이미 존재, 건너뜀 (%s)",
                     slide.index, total, image_path.name)
            continue
        if not slide.prompt:
            sys.exit(f"오류: 세그먼트 {slide.index}의 프롬프트가 없습니다. 3단계를 먼저 실행하세요.")

        log.info("[4/5] 이미지 %d/%d 생성 중: %s...", slide.index, total, slide.prompt[:70])

        def call() -> bytes:
            response = client.models.generate_content(
                model=image_model,
                contents=slide.prompt,
                config=types.GenerateContentConfig(
                    response_modalities=["IMAGE", "TEXT"],
                ),
            )
            for candidate in response.candidates or []:
                for part in candidate.content.parts or []:
                    inline = getattr(part, "inline_data", None)
                    if inline is not None and inline.data:
                        return inline.data
            raise ValueError("응답에 이미지 데이터가 없습니다")

        image_bytes = retry_with_backoff(
            call,
            what=f"이미지 {slide.index} 생성",
            max_retries=max_retries,
            base_delay=retry_base_delay,
        )
        tmp_path = image_path.with_suffix(".tmp")
        tmp_path.write_bytes(image_bytes)
        tmp_path.rename(image_path)  # 부분 저장된 파일이 남지 않도록 원자적 저장
        log.info("[4/5] 이미지 %d/%d 저장 완료: %s", slide.index, total, image_path.name)

    log.info("[4/5] 이미지 %d장 준비 완료 → %s", total, images_dir)
    return paths


# ── 5단계: 영상 조립 (ffmpeg) ────────────────────────────────────────────────
def write_srt(slides: list[SlideSegment], srt_path: Path) -> None:
    lines: list[str] = []
    for slide in slides:
        lines.append(str(slide.index))
        lines.append(f"{format_srt_time(slide.start)} --> {format_srt_time(slide.end)}")
        lines.append(slide.text)
        lines.append("")
    srt_path.write_text("\n".join(lines), encoding="utf-8")


def build_scale_filter(resolution: str, fps: int) -> str:
    width, height = resolution.lower().split("x")
    return (
        f"scale={width}:{height}:force_original_aspect_ratio=decrease,"
        f"pad={width}:{height}:(ow-iw)/2:(oh-ih)/2:color=#FFF8EE,"
        f"fps={fps},format=yuv420p,setsar=1"
    )


def assemble_video(
    slides: list[SlideSegment],
    images_dir: Path,
    audio_path: Path,
    output_dir: Path,
    *,
    resolution: str,
    fps: int,
    crossfade: float,
    subtitles: bool,
) -> Path:
    """이미지들을 각 세그먼트 길이만큼 표시하며 오디오와 합성 → output.mp4."""
    output_path = output_dir / "output.mp4"
    durations = [max(0.5, s.end - s.start) for s in slides]
    scale_filter = build_scale_filter(resolution, fps)

    subtitle_filter = ""
    if subtitles:
        srt_path = output_dir / "subtitles.srt"
        write_srt(slides, srt_path)
        # output_dir을 cwd로 실행하므로 상대 경로 사용 (경로 이스케이프 문제 회피)
        subtitle_filter = (
            ",subtitles=subtitles.srt:force_style="
            "'FontSize=18,PrimaryColour=&H00FFFFFF,OutlineColour=&H80000000,Outline=2'"
        )
        log.info("[5/5] 자막 파일 생성: %s", srt_path)

    log.info(
        "[5/5] 영상 조립 시작 (이미지 %d장, 해상도 %s, 크로스페이드 %.1f초)",
        len(slides), resolution, crossfade,
    )

    if crossfade > 0 and len(slides) > 1:
        cmd = _build_xfade_command(
            slides, durations, images_dir, audio_path, output_dir,
            scale_filter=scale_filter, subtitle_filter=subtitle_filter,
            crossfade=crossfade,
        )
    else:
        cmd = _build_concat_command(
            slides, durations, images_dir, audio_path, output_dir,
            scale_filter=scale_filter, subtitle_filter=subtitle_filter,
        )

    result = subprocess.run(cmd, cwd=output_dir, capture_output=True, text=True)
    if result.returncode != 0:
        log.error("ffmpeg 실패:\n%s", result.stderr[-3000:])
        sys.exit("오류: ffmpeg 영상 조립에 실패했습니다.")

    log.info("[5/5] 영상 조립 완료 → %s", output_path)
    return output_path


def _build_concat_command(
    slides: list[SlideSegment],
    durations: list[float],
    images_dir: Path,
    audio_path: Path,
    output_dir: Path,
    *,
    scale_filter: str,
    subtitle_filter: str,
) -> list[str]:
    """concat demuxer 방식 (크로스페이드 없음, 빠름)."""
    concat_path = output_dir / "concat.txt"
    lines: list[str] = []
    for slide, duration in zip(slides, durations):
        rel = os.path.relpath(images_dir / f"img_{slide.index:03d}.png", output_dir)
        lines.append(f"file '{rel}'")
        lines.append(f"duration {duration:.3f}")
    # concat demuxer 규칙: 마지막 파일은 한 번 더 명시해야 duration이 적용됨
    last_rel = os.path.relpath(images_dir / f"img_{slides[-1].index:03d}.png", output_dir)
    lines.append(f"file '{last_rel}'")
    concat_path.write_text("\n".join(lines), encoding="utf-8")

    return [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0", "-i", str(concat_path.resolve()),
        "-i", str(audio_path.resolve()),
        "-filter_complex", f"[0:v]{scale_filter}{subtitle_filter}[v]",
        "-map", "[v]", "-map", "1:a",
        "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        "output.mp4",
    ]


def _build_xfade_command(
    slides: list[SlideSegment],
    durations: list[float],
    images_dir: Path,
    audio_path: Path,
    output_dir: Path,
    *,
    scale_filter: str,
    subtitle_filter: str,
    crossfade: float,
) -> list[str]:
    """xfade 필터 체인 방식 (크로스페이드 적용, 이미지 수가 많으면 느림)."""
    n = len(slides)
    fade = min(crossfade, min(durations) / 2)  # 짧은 구간보다 긴 페이드 방지

    cmd: list[str] = ["ffmpeg", "-y"]
    for slide, duration in zip(slides, durations):
        # 마지막 클립을 제외하고 페이드 겹침만큼 길이를 늘려 오디오 싱크 유지
        clip_dur = duration + (fade if slide.index != slides[-1].index else 0)
        image = str((images_dir / f"img_{slide.index:03d}.png").resolve())
        cmd += ["-loop", "1", "-t", f"{clip_dur:.3f}", "-i", image]
    cmd += ["-i", str(audio_path.resolve())]

    filters: list[str] = []
    for i in range(n):
        filters.append(f"[{i}:v]{scale_filter}[v{i}]")

    prev = "v0"
    offset = 0.0
    for i in range(1, n):
        offset += durations[i - 1]
        label = f"x{i}" if i < n - 1 else "vfinal"
        filters.append(
            f"[{prev}][v{i}]xfade=transition=fade:duration={fade:.3f}:offset={offset:.3f}[{label}]"
        )
        prev = label
    if subtitle_filter:
        filters.append(f"[vfinal]{subtitle_filter.lstrip(',')}[vsub]")
        final_label = "vsub"
    else:
        final_label = "vfinal"

    script_path = output_dir / "xfade_filters.txt"
    script_path.write_text(";\n".join(filters), encoding="utf-8")

    cmd += [
        "-filter_complex_script", str(script_path.resolve()),
        "-map", f"[{final_label}]", "-map", f"{n}:a",
        "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        "output.mp4",
    ]
    return cmd


# ── 파이프라인 실행 ──────────────────────────────────────────────────────────
def run_pipeline(args: argparse.Namespace) -> None:
    config = load_config(Path(args.config))

    # CLI 인자가 지정되면 config보다 우선
    for key in ("segments", "output_dir", "resolution", "crossfade"):
        value = getattr(args, key, None)
        if value is not None:
            config[key] = value
    if args.subtitles:
        config["subtitles"] = True

    if args.dry_run:
        config["segments"] = DRY_RUN_SEGMENTS
        log.info("=== DRY RUN 모드: 세그먼트 %d개만 처리 ===", DRY_RUN_SEGMENTS)

    audio_path = Path(args.input)
    if not audio_path.exists():
        sys.exit(f"오류: 입력 파일이 없습니다: {audio_path}")
    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        sys.exit("오류: ffmpeg/ffprobe를 찾을 수 없습니다. ffmpeg를 설치하세요.")

    output_dir = Path(config["output_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)

    audio_duration = probe_audio_duration(audio_path)
    log.info("입력 오디오: %s (%.1f초)", audio_path, audio_duration)

    # 1. STT
    transcript_segments = transcribe(
        audio_path, output_dir,
        model_size=config["whisper_model"],
        language=config["language"],
        force=args.force,
    )

    # 2. 세그먼트 분할
    slides = segment(transcript_segments, int(config["segments"]), audio_duration)

    # 3~4. Gemini 호출
    client = get_genai_client()
    slides = generate_image_prompts(
        slides, output_dir,
        client=client,
        text_model=config["text_model"],
        style_guide=config["style_guide"],
        max_retries=int(config["max_retries"]),
        retry_base_delay=float(config["retry_base_delay"]),
        force=args.force,
    )
    generate_images(
        slides, output_dir / "images",
        client=client,
        image_model=config["image_model"],
        max_retries=int(config["max_retries"]),
        retry_base_delay=float(config["retry_base_delay"]),
    )

    # 5. 영상 조립
    output_path = assemble_video(
        slides, output_dir / "images", audio_path, output_dir,
        resolution=str(config["resolution"]),
        fps=int(config["fps"]),
        crossfade=float(config["crossfade"]),
        subtitles=bool(config["subtitles"]),
    )

    log.info("✅ 전체 파이프라인 완료: %s", output_path)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="팟캐스트 mp3 → 이미지 슬라이드쇼 영상(mp4) 자동 생성",
    )
    parser.add_argument("--input", required=True, help="입력 mp3 파일 경로")
    parser.add_argument("--segments", type=int, default=None,
                        help="세그먼트(=이미지) 개수 (기본 100)")
    parser.add_argument("--output-dir", default=None, help="결과물 폴더 (기본 output/)")
    parser.add_argument("--config", default="config.yaml", help="설정 파일 경로")
    parser.add_argument("--resolution", default=None, help="영상 해상도, 예: 1280x720")
    parser.add_argument("--crossfade", type=float, default=None,
                        help="이미지 전환 크로스페이드 길이(초), 예: 0.5")
    parser.add_argument("--subtitles", action="store_true", help="자막 오버레이 켜기")
    parser.add_argument("--dry-run", action="store_true",
                        help=f"테스트 모드: 세그먼트 {DRY_RUN_SEGMENTS}개만 처리")
    parser.add_argument("--force", action="store_true",
                        help="기존 transcript/프롬프트 캐시를 무시하고 다시 생성")
    return parser.parse_args()


def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%H:%M:%S",
    )
    run_pipeline(parse_args())


if __name__ == "__main__":
    main()
