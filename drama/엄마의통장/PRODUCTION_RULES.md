# 〈엄마의 통장〉 제작 규칙 정본 (Production Rules)

업로드된 `project.json`, `ACTIVE_REFERENCES.json`, `STORYBOARD.md`,
`scripts/EP01_CUT01_1979_화재구조_한영프롬프트.md` 4개 문서에서 추출한 규칙.
**앞으로 모든 컷 작업은 이 문서를 기준으로 한다.**

## 1. 작품 규격 (변경 금지)

| 항목 | 값 |
|---|---|
| 제목 | 엄마의 통장 |
| 형식 | 20부작 AI 가족 미스터리 드라마 |
| 화면비 | 16:9 |
| 회당 길이 | 180초 |
| 컷 길이 | 15초 × 12컷 |
| 프레임레이트 | 24fps |
| 마스터 스크립트 | `엄마의통장_MASTER_수정본.md` (**현재 리포지토리에 없음**) |

### 통일 스타일 문자열 (모든 프롬프트 POSITIVE LOCKS 말미에 그대로 삽입)

```text
cinematic photorealistic Korean live-action drama, natural skin texture, physical cine lens, 24fps, restrained saturation, warm domestic highlights and cool mystery shadows, realistic gravity and contact shadows, consistent identities across every cut
```

## 2. 절대 규칙 (Hard Rules)

1. **BGM 금지.** 모든 컷은 대사 + 현장음(diegetic)만 생성. 음악은 후반작업에서만 얹는다.
2. **한 컷의 실제 화자는 최대 2명.** 4명 이상 필요한 장면은 반응 쇼트로 분리한다.
3. **화면 내 글자 생성 금지.** ATM 숫자, 거래내역, 발신자 이름, 자막은 영상 모델에 맡기지 않고 **후반 합성**.
4. **레퍼런스는 `01_캐릭터_현재사용` 폴더만 사용.** `99_보관_이전버전`은 절대 참조 금지.
   `ACTIVE_REFERENCES.json`의 `excluded` 목록 파일은 어떤 경우에도 쓰지 않는다.
5. **승인 게이트.** `project.json`의 `storyboard.approved`와 `video_render_allowed`가
   `true`가 되기 전에는 영상 렌더 금지. 키프레임 이미지 승인이 먼저다.
6. **180도 축 유지.** 씬별 블로킹 락(아래)을 모든 쇼트에서 동일하게 지킨다. 인물의 화면 좌우가 바뀌면 안 된다.
7. **이름 변경 반영.** 정민호 → **정태민**. 구 이름은 어디에도 남기지 않는다.

## 3. 씬 블로킹 락 (Blocking Lock)

- **병원 입원실** — 순자: 화면 중앙 창가 침대 / 태수: 화면 왼쪽 / 미경: 침대 오른쪽 / 태민: 출입문 쪽 화면 오른쪽 뒤.
- **병원 휴게실** — 태수: 테이블 화면 왼쪽 / 미경: 중앙 맞은편 / 태민: 화면 오른쪽. 세 사람 모두 휴대폰이 놓인 테이블 중심을 향함.
- **성준의 서재** — 성준: 책상 오른쪽 창가 / 뒤집힌 사진: 화면 왼쪽 전경 책상 위. 카메라는 책상 바깥쪽 축 유지.
- **1979 봉제공장(화재)** — 순자: 화면 왼쪽(선반에 다리 눌림) / 만식: 화면 오른쪽 통로 / 출구: 왼쪽 뒤 / 불길: 오른쪽 뒤. 카메라는 행동축 남쪽.

## 4. 컷 프롬프트 표준 구조 (11블록)

`scripts/EP01_CUT01_1979_화재구조_한영프롬프트.md`가 표준 템플릿이다.
모든 컷 프롬프트는 **한글판 + 영문판 2벌**을 같은 순서로 작성한다.

1. `SCENE CONTEXT` — 등장인물 수를 숫자로 못 박는다 ("EXACTLY TWO CHARACTERS — NO DUPLICATES")
2. `ACTIVE REFERENCES` — `<<<element_id>>>`가 무엇을 고정하는지 명시. 배경은 geometry만 고정, 카메라 각도는 자유
3. `GEO SPATIAL LAYOUT` — 좌우/전후 관계와 액션 축
4. `FIRST FRAME AND SPATIAL BLOCKING` — 첫 프레임은 이미 사건이 진행 중인 상태로
5. `FORMAT MODE` — 16:9, 24fps, 길이, 하드컷 수, 카메라 운용, 자막 없음
6. `OPTICS AND CAMERA` — 샷별 화각(도), 거리(m), 높이, 컷 타이밍(초)
7. `ACTION TIMING` — 초 단위 구간별 동작 + 대사
8. `PHYSICS` — 무게·반동·먼지·중력 표현
9. `LIGHTING` — 주광원/보조광/캐치라이트
10. `AUDIO` — 현장음 목록 + 대사 1줄. "이 문장 외의 대사는 없다" 명시
11. `POSITIVE LOCKS` — 인원수·의상·구조·좌우관계·마지막 프레임 상태 + 통일 스타일 문자열 + BGM 금지 문구

## 5. 모델 호출값

| 항목 | CUT01 화재구조 | 콜드오픈 00A |
|---|---|---|
| model | `seedance_2_0` | `wan3_0` |
| genre | `drama` | — |
| duration | 15초 | 8초 |
| resolution | — | 480p |
| aspect_ratio | 16:9 | 16:9 |
| generate_audio | `true` | — |
| 예상 크레딧 | — | 8 |

H3 / WAN 3.0에서 쓸 때는 세 레퍼런스를 캐릭터·캐릭터·배경으로 각각 첨부하고
`<<<...>>>`를 해당 서비스의 레퍼런스 태그로 치환한다.

## 6. 캐릭터 키 매핑 (두 파일의 이름 체계가 다름 — 이 표가 기준)

| project.json 키 | ACTIVE_REFERENCES.json 폴더명 | 인물 |
|---|---|---|
| `soonja_current` | 박순자_현재 | 박순자 (현재) |
| `soonja_young` | 박순자_젊은시절 | 젊은 박순자 |
| `taesu` | 정태수 | 정태수 (장남) |
| `taemin` | 정태민 | 정태민 (차남) |
| `migyeong` | 정미경 | 정미경 (딸) |
| `mansik_young` | 정만식_젊은시절 | 젊은 정만식 |
| `seongjun_current` | 한성준_현재 | 한성준 (현재) |
| `seongjun_young` | 한성준_젊은시절 | 젊은 한성준 |
| `byeongcheol_current` | 최병철_현재 | 최병철 (현재) |
| `byeongcheol_young` | 최병철_젊은시절 | 젊은 최병철 |
| `seongjun_wife_young` | 성준의아내_젊은시절 | 젊은 성준의 아내 |
| `migyeong_baby` | 정미경_아기 | 아기 정미경 |

- **정만식 현재 시점 레퍼런스는 없다.** 만식은 회상(1979)에만 등장하는 것으로 간주.
- **`market_vendor`(시장상인)는 두 파일 어디에도 없다.** EP01 CUT01에 필요 → 신규 생성 대상.
- 만식 확정 의상: 감청색 면 트윌 작업 재킷 + 동색 일자 작업 바지 + 아이보리 니트 + 검은 가죽 작업화 (`01_기본_감청색작업복_v5.png`).
  이전 버전(미소년 v3, 페트롤블루 v4, 1979 v1/v2)은 전부 excluded.

## 7. 열려 있는 이슈 (해결 전에는 렌더 금지)

1. **마스터 스크립트 부재** — `엄마의통장_MASTER_수정본.md`가 없어 CUT02~12의 실제 대사를 쓸 수 없다.
2. **컷 넘버링 충돌** — 컷 매트릭스의 `CUT 01`은 "시장에서 쓰러짐"인데,
   프롬프트 파일명은 `EP01_CUT01_1979_화재구조`이고 내용은 콜드오픈 `00C`(1979 화재)와 같다. 번호 체계 통일 필요.
3. **러닝타임 초과** — 콜드오픈 25초 + 본편 180초 = 205초. `episode_target_seconds: 180`과 불일치.
4. **모델 혼용** — 콜드오픈 `wan3_0`, CUT01 `seedance_2_0`. 모델이 섞이면 얼굴 일관성이 무너진다. 한 에피소드는 한 모델로 통일 권장.
5. **Element 미등록** — `ELEMENT_REGISTRY.md` 참조. 프롬프트의 `<<<element_id>>>`를 채울 실제 ID가 대부분 없다.
