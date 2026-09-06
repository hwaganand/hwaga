# 〈엄마의 통장〉 EP01 스토리보드 및 Element 매트릭스

## 강훅 콜드 오픈 추가안 — 승인 대기

| CUT | 시간 | 핵심 비트 | 캐릭터 | 환경 | 레퍼런스 | 모델/예상비용 |
|---|---:|---|---|---|---|---|
| 00A | 0–8초 | 회전하는 동전 뒤로 쓰러진 순자, 상인과 시장 사람들이 달려온다 | `soonja_current`, 흐린 시장 인파 | `market_rice_shop_day` | 순자 전신·표정·방향 3장 + 풍년쌀상회 | WAN 3.0, 480p, 8초 = 8크레딧 |
| 00B | 8–16초 | ATM 18억 인서트와 태수의 얼어붙은 반응 | `taesu` | `hospital_atm` | 태수 전신·표정·방향 3장 + ATM | 승인 후 제작 |
| 00C | 16–25초 | 1979년 화재 속 젊은 만식이 젊은 순자를 구한다 | `young_mansik`, `young_soonja` | `factory_fire_1979` | 두 인물 레퍼런스 + 공장 배경 | 승인 후 제작 |

**00A 키프레임:** `storyboard/EP01_COLDOPEN_CUT00A_keyframe_v1.png`  
**상태:** 사용자 승인 대기. 승인 전 영상 렌더 금지.

## 제작 규격

- 총 12컷 × 15초 = 약 180초
- 16:9
- 모든 컷은 BGM 없이 대사와 현장음만 생성
- ATM 숫자, 거래내역, 발신자 이름은 영상 생성 모델에 맡기지 않고 후반 합성
- 한 컷의 실제 화자는 최대 2명
- 4명 이상이 필요한 장면은 반응 쇼트로 분리

## 반복 에셋

### 캐릭터 Elements

- `soonja_current` — 박순자
- `taesu` — 정태수
- `migyeong` — 정미경
- `taemin` — 정태민
- `seongjun_current` — 한성준
- `market_vendor` — 시장상인, EP01 조연 신규 생성 필요

### 환경 Elements

- `market_rice_shop_day` — 오래된 재래시장 쌀가게 골목, 낮
- `hospital_room` — 4인 병실의 창가 침대 구역
- `hospital_atm` — 병원 1층의 조용한 ATM 코너
- `hospital_corridor` — 병원 복도
- `hospital_lounge` — 작은 병원 휴게실
- `seongjun_study_night` — 어두운 목재 서재, 야간

### 소품 Elements

- `soonja_wallet` — 오래된 갈색 가죽 지갑
- `soonja_bank_card` — 무브랜드 체크카드
- `soonja_phone` — 글씨가 크게 설정된 검은 스마트폰
- `taesu_phone` — 검은 스마트폰
- `hospital_tray` — 금속 수저가 놓인 병원 식판
- `photo_1979_reversed` — 뒷면이 보이도록 뒤집힌 오래된 단체사진

## 씬 블로킹 락

### 병원 입원실

`순자는 화면 중앙의 창가 침대에 있고, 태수는 화면 왼쪽, 미경은 침대 오른쪽, 태민은 출입문 가까운 화면 오른쪽 뒤에 선다. 모든 쇼트는 동일한 액션 축을 유지하며 인물은 화면 좌우를 서로 바꾸지 않는다.`

### 병원 휴게실

`태수는 테이블 화면 왼쪽, 미경은 중앙 맞은편, 태민은 화면 오른쪽에 앉는다. 세 사람은 휴대폰이 놓인 테이블 중심을 향하며 모든 쇼트는 동일한 180도 축을 유지한다.`

### 성준의 서재

`성준은 책상 오른쪽 창가에 서고 뒤집힌 사진은 화면 왼쪽 전경 책상 위에 놓인다. 카메라는 책상 바깥쪽 축을 유지한다.`

## 컷 매트릭스

| CUT | 시간 | 핵심 비트 | 캐릭터 | 환경 | 소품 | 추천 BGM(후반) |
|---|---:|---|---|---|---|---|
| 01 | 0–15초 | 순자가 흥정 중 쓰러진다 | `soonja_current`, `market_vendor` | `market_rice_shop_day` | 천 원짜리 | 02 순자의 시장 아침 → 무음 전환 |
| 02 | 15–30초 | 병실에서 체크카드를 건넨다 | `soonja_current`, `taesu` | `hospital_room` | `soonja_wallet`, `soonja_bank_card` | 05 박순자 테마 |
| 03 | 30–45초 | ATM 잔액 18억 발견 | `taesu` | `hospital_atm` | `soonja_bank_card`, `taesu_phone` | 03 18억의 발견 |
| 04 | 45–60초 | 태수가 동생들을 호출한다 | `taesu` | `hospital_corridor` | `taesu_phone` | 03 18억의 발견 |
| 05 | 60–75초 | 세 남매가 잔액을 확인한다 | `taesu`, `migyeong`, `taemin` | `hospital_lounge` | `taesu_phone` | 04 세 남매 대소동 |
| 06 | 75–90초 | 반복 입금자 한성준 발견 | `taesu`, `migyeong`, `taemin` | `hospital_lounge` | `taesu_phone` | 12 45년의 입금 내역 |
| 07 | 90–105초 | 태수가 순자를 추궁한다 | `soonja_current`, `taesu` | `hospital_room` | `hospital_tray`, `taesu_phone` | 05 박순자 테마 |
| 08 | 105–120초 | 순자 “내 돈 아니야” | `soonja_current`, `migyeong` | `hospital_room` | `hospital_tray` | 01 메인 테마 변주 |
| 09 | 120–135초 | 한성준의 전화가 온다 | `soonja_current`, `taemin` | `hospital_room` | `soonja_phone` | 10 최병철의 가면이 아닌 03 미스터리 펄스 |
| 10 | 135–150초 | 성준이 돈 확인 여부를 묻는다 | `seongjun_current` | `seongjun_study_night` | `photo_1979_reversed`, 스마트폰 | 09 한성준 테마 |
| 11 | 150–165초 | “그 돈 말고도” | `soonja_current`, `seongjun_current` | 병실/서재 교차 | `soonja_phone`, `photo_1979_reversed` | 09 한성준 테마 |
| 12 | 165–180초 | “돌려받아야 할 게 있습니다” | `seongjun_current`, `soonja_current` | 서재/병실 교차 | `hospital_tray`, `photo_1979_reversed` | 01 메인 테마 미스터리 엔딩 |

## 스토리보드 이미지 승인 게이트

- [ ] 시장상인 캐릭터 생성 및 선택
- [ ] 환경 6종 생성
- [ ] 핵심 소품 6종 생성
- [ ] 12개 키프레임 생성
- [ ] 사용자 스토리보드 승인
- [ ] `project.json`의 `storyboard.approved`를 `true`로 변경
- [ ] 승인 후에만 영상 생성
