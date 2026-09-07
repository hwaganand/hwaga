"""
Suno 라이브러리 전체를 WAV로 순차 다운로드하는 스크립트.

사용법:
    pip install playwright
    playwright install chromium
    python suno_wav_downloader.py

첫 실행 시 브라우저 창이 뜨면 직접 로그인하세요 (자동 로그인 안 함 - 비번을
스크립트에 넣지 않기 위함). 로그인 세션은 PROFILE_DIR에 저장되므로
다음부터는 로그인 없이 바로 진행됩니다.

주의:
    - WAV 다운로드는 Pro/Premier 플랜에서만 가능합니다.
    - Suno 화면 구조가 바뀌면 collect_song_rows / download_wav_for_row 의
      셀렉터를 실제 DOM 기준으로 수정해야 합니다.
    - 처음 돌릴 때는 HEADLESS = False 상태로 두고 눈으로 확인하세요.
"""

import random
import re
import time
from pathlib import Path

from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

# ---------------- 설정 (필요하면 여기만 수정) ----------------
DOWNLOAD_DIR = Path.home() / "Downloads" / "suno_wav"
PROFILE_DIR = Path.home() / ".suno_downloader_profile"  # 로그인 세션 저장 위치
LIBRARY_URL = "https://suno.com/me"  # 라이브러리 URL이 다르면 수정
HEADLESS = False  # 처음엔 반드시 False로 눈으로 확인
DELAY_RANGE = (4, 9)  # 곡 사이 랜덤 대기 (초) - 레이트리밋 회피용, 줄이지 말 것
MAX_SCROLL_ROUNDS = 200  # 라이브러리 전체 스크롤 로딩 시도 횟수 상한
WAV_ENCODE_TIMEOUT_MS = 180_000  # WAV는 서버에서 새로 인코딩되므로 넉넉히
ROW_SELECTOR = '[data-testid="song-row"], [role="row"]'  # 안 맞으면 여기 교체
# --------------------------------------------------------------


def sanitize_filename(name: str) -> str:
    name = re.sub(r'[\\/:*?"<>|]', "_", name).strip()
    return name[:150] or "untitled"


def collect_song_rows(page):
    """라이브러리를 끝까지 스크롤하며 곡 행(row) 요소들을 모은다."""
    prev_count = -1
    stable_rounds = 0

    for _ in range(MAX_SCROLL_ROUNDS):
        count = page.locator(ROW_SELECTOR).count()

        if count == prev_count:
            stable_rounds += 1
            if stable_rounds >= 3:  # 3회 연속 증가 없으면 끝까지 로딩된 것으로 판단
                break
        else:
            stable_rounds = 0
        prev_count = count

        page.mouse.wheel(0, 2000)
        page.wait_for_timeout(800)

    return page.locator(ROW_SELECTOR).all()


def get_row_title(row, index: int) -> str:
    try:
        text = row.inner_text(timeout=3000).strip().splitlines()
        for line in text:
            if line.strip():
                return sanitize_filename(line)
    except Exception:
        pass
    return f"song_{index:04d}"


def download_wav_for_row(page, row, index, total) -> bool:
    """행 하나에서 ⋯ 메뉴 -> Download -> WAV 클릭 후 다운로드 완료까지 대기."""
    title = get_row_title(row, index)
    out_path = DOWNLOAD_DIR / f"{title}.wav"

    if out_path.exists():
        print(f"[{index}/{total}] 이미 있음, 건너뜀: {title}")
        return True

    try:
        row.scroll_into_view_if_needed(timeout=5000)
        row.hover(timeout=5000)

        more_btn = row.get_by_role(
            "button", name=re.compile(r"more|option|menu|\.\.\.|⋯", re.I)
        ).first
        more_btn.click(timeout=5000)

        page.get_by_text("Download", exact=True).first.click(timeout=5000)

        # 클릭이 expect_download 블록 안에 있어야 다운로드 이벤트를 놓치지 않는다
        with page.expect_download(timeout=WAV_ENCODE_TIMEOUT_MS) as dl_info:
            page.get_by_text("WAV", exact=True).first.click(timeout=5000)

        dl_info.value.save_as(out_path)
        print(f"[{index}/{total}] 완료: {title}")
        return True

    except PWTimeout:
        print(f"[{index}/{total}] 실패(타임아웃): {title}")
        print("  → 셀렉터가 안 맞거나, 플랜이 WAV 미지원일 수 있습니다.")
        page.keyboard.press("Escape")  # 열려 있는 메뉴 닫고 다음 곡으로
        return False
    except Exception as e:
        print(f"[{index}/{total}] 실패: {title} - {e}")
        page.keyboard.press("Escape")
        return False


def main():
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
    PROFILE_DIR.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=str(PROFILE_DIR),
            headless=HEADLESS,
            accept_downloads=True,
        )
        page = context.pages[0] if context.pages else context.new_page()
        page.goto("https://suno.com")

        input(
            "\n브라우저에서 Suno 로그인 후, 라이브러리(내 곡 목록) 페이지로 이동하세요.\n"
            "다 되면 여기서 Enter를 누르세요...\n"
        )

        if "/me" not in page.url:
            try:
                page.goto(LIBRARY_URL)
                page.wait_for_load_state("networkidle", timeout=30_000)
            except Exception:
                pass

        print("라이브러리 전체 스크롤하며 곡 목록 수집 중...")
        rows = collect_song_rows(page)
        total = len(rows)
        print(f"총 {total}곡 발견")

        if total == 0:
            print("곡을 못 찾았습니다. LIBRARY_URL 또는 ROW_SELECTOR를 확인해주세요.")
            print("F12로 곡 행을 검사(Inspect)해서 실제 속성을 확인하세요.")
            context.close()
            return

        ok = fail = 0
        for i, row in enumerate(rows, start=1):
            if download_wav_for_row(page, row, i, total):
                ok += 1
            else:
                fail += 1
            time.sleep(random.uniform(*DELAY_RANGE))

        print(f"\n완료: 성공 {ok} / 실패 {fail} / 전체 {total}")
        print(f"저장 위치: {DOWNLOAD_DIR}")
        print("실패분은 같은 명령을 다시 실행하면 이어받습니다.")
        context.close()


if __name__ == "__main__":
    main()
