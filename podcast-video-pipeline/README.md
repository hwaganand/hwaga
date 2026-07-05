# 🎙️ 팟캐스트 → 슬라이드쇼 영상 자동화 파이프라인

mp3 팟캐스트 파일 하나를 입력하면:

1. **음성인식(STT)** — faster-whisper로 타임스탬프 포함 텍스트 추출
2. **세그먼트 분할** — 문장 경계 기준으로 약 100개 구간 분할
3. **이미지 프롬프트 생성** — Gemini 텍스트 모델로 구간별 삽화 프롬프트 자동 작성
4. **이미지 생성** — Gemini 2.5 Flash Image("nano banana")로 이미지 100장 생성
5. **영상 조립** — ffmpeg로 오디오와 싱크된 슬라이드쇼 mp4 완성

까지 **CLI 명령 하나**로 자동 실행됩니다.

## 📁 프로젝트 구조

```
podcast-video-pipeline/
├── input/
│   └── podcast.mp3          # 여기에 mp3를 넣으세요
├── output/                   # 자동 생성됨
│   ├── transcript.json       # STT 결과 (타임스탬프 포함)
│   ├── image_prompts.json    # 세그먼트별 이미지 프롬프트
│   ├── images/img_001.png …  # 생성된 이미지
│   ├── subtitles.srt         # (자막 옵션 사용 시)
│   └── output.mp4            # 최종 영상
├── make_radio_video.py
├── config.yaml
├── requirements.txt
└── .env                      # API 키 (직접 생성)
```

## 🛠️ 설치

### 1. 필수 프로그램

- **Python 3.11+**
- **ffmpeg** (ffprobe 포함)
  - macOS: `brew install ffmpeg`
  - Windows: `winget install ffmpeg` 또는 https://ffmpeg.org/download.html

### 2. 파이썬 패키지

```bash
cd podcast-video-pipeline
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. API 키 설정

[Google AI Studio](https://aistudio.google.com/apikey)에서 Gemini API 키를 발급받아:

```bash
cp .env.example .env
# .env 파일을 열어 GEMINI_API_KEY=발급받은키 입력
```

## 🚀 사용법

```bash
# 기본 실행 (이미지 100장)
python make_radio_video.py --input input/podcast.mp3 --segments 100

# 테스트 모드 — 짧은 mp3(1분 이내 권장)로 세그먼트 5개만 처리
python make_radio_video.py --input input/short_test.mp3 --dry-run

# 크로스페이드 전환 + 자막 + 풀HD
python make_radio_video.py --input input/podcast.mp3 \
    --crossfade 0.5 --subtitles --resolution 1920x1080
```

### 주요 옵션

| 옵션 | 설명 | 기본값 |
|------|------|--------|
| `--input` | 입력 mp3 경로 (필수) | — |
| `--segments` | 세그먼트(=이미지) 개수 | 100 |
| `--output-dir` | 결과물 폴더 | `output/` |
| `--resolution` | 영상 해상도 | `1280x720` |
| `--crossfade` | 이미지 전환 페이드 길이(초), 0이면 끔 | 0 |
| `--subtitles` | 자막 오버레이 켜기 | 꺼짐 |
| `--dry-run` | 테스트 모드 (세그먼트 5개) | 꺼짐 |
| `--force` | transcript/프롬프트 캐시 무시하고 재생성 | 꺼짐 |
| `--config` | 설정 파일 경로 | `config.yaml` |

세그먼트 개수, 이미지 스타일 문구, whisper 모델 크기 등은 `config.yaml`에서도 조정할 수 있습니다.

## 🔄 중단/재시작 (중요)

이미지 100장 생성은 시간과 비용이 크기 때문에 **모든 단계가 이어하기 가능**하게 설계되어 있습니다:

- `transcript.json`이 있으면 STT를 건너뜁니다
- `image_prompts.json`에 이미 생성된 프롬프트는 재사용합니다
- `images/img_NNN.png`가 이미 있으면 해당 이미지는 건너뜁니다
- API rate limit에 걸리면 지수 백오프로 자동 재시도합니다 (기본 5회)

중간에 끊겼다면 **같은 명령을 그대로 다시 실행**하면 이어서 진행됩니다.
처음부터 다시 하려면 `output/` 폴더를 지우거나 `--force`를 사용하세요.

## 🎨 이미지 스타일

실버 세대 시청자를 고려해 모든 이미지 프롬프트에 아래 스타일이 고정 반영됩니다
(`config.yaml`의 `style_guide`에서 수정 가능):

> 따뜻하고 밝은 톤, 고령층이 편안하게 볼 수 있는 삽화 스타일,
> 부드러운 파스텔 색감, 자극적이지 않은 평화로운 분위기

## ⚠️ 참고

- 크로스페이드(`--crossfade`)는 이미지 100장 기준 렌더링 시간이 크게 늘어납니다.
  먼저 크로스페이드 없이 확인 후 최종 렌더링에만 사용하는 것을 권장합니다.
- 한국어 STT 정확도가 아쉬우면 `config.yaml`의 `whisper_model`을
  `medium` 또는 `large-v3`로 올리세요 (처리 시간 증가).
- Gemini 무료 등급은 이미지 생성 rate limit이 낮습니다. 100장 생성 시
  유료 등급(pay-as-you-go) 사용을 권장합니다.
