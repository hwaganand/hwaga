# Element 등록 현황 (Higgsfield Reference Elements)

조회일: 2026-09-06 / 워크스페이스 전체 목록 기준.
프롬프트의 `<<<element_id>>>` 자리에 넣을 실제 UUID를 여기서 관리한다.

## 등록 완료 (2건)

| 프롬프트 키 | Element 이름 | element_id | 분류 |
|---|---|---|---|
| `soonja_current` | `soonja-current` | `7006e364-0b27-4414-8835-b10ecb39a8b5` | character |
| `market_rice_shop_day` | `market-rice-shop` | `fd24c118-1077-473f-9a1b-1475aaaf459f` | environment |

## 미등록 — 생성/등록 필요

### EP01 CUT01(1979 화재구조) 프롬프트가 요구하는 3건 — **전부 없음**

| 프롬프트 플레이스홀더 | 원본 레퍼런스 파일 | 상태 |
|---|---|---|
| `<<<young_mansik_element_id>>>` | 정만식_젊은시절/`01_기본_감청색작업복_v5.png` (+표정8종, 각도8종) | 미등록 |
| `<<<young_soonja_element_id>>>` | 박순자_젊은시절/`01_기본_1970년대.png` (+표정8종, 각도8종) | 미등록 |
| `<<<factory_fire_1979_element_id>>>` | 1979 봉제공장 내부 배경 | **이미지 자체가 없음** |

→ **현재 상태로는 CUT01 렌더가 물리적으로 불가능하다.**

### 캐릭터 (미등록)

`taesu`, `taemin`, `migyeong`, `soonja_young`, `mansik_young`,
`seongjun_current`, `seongjun_young`, `byeongcheol_current`, `byeongcheol_young`,
`seongjun_wife_young`, `migyeong_baby`, `market_vendor`(이미지 자체 없음)

### 환경 (미등록, 6종 중 5종)

`hospital_room`, `hospital_atm`, `hospital_corridor`, `hospital_lounge`,
`seongjun_study_night`, `factory_fire_1979`

### 소품 (미등록, 6종 전부)

`soonja_wallet`, `soonja_bank_card`, `soonja_phone`, `taesu_phone`,
`hospital_tray`, `photo_1979_reversed`

## 등록 절차 메모

1. 레퍼런스 PNG를 업로드(media_upload → PUT → media_confirm)해 `media_id` 확보
2. Reference Element로 `create` (category: character / environment / prop)
3. 반환된 UUID를 이 표에 기록
4. 컷 프롬프트의 `<<<...>>>`를 해당 UUID로 치환

**주의:** Element는 한 장짜리 이미지 참조다. 표정 8종·각도 8종 시트를 함께 물리려면
프롬프트 한 벌에 같은 인물의 Element 여러 개를 붙이거나, 3장을 한 장으로 합성한 시트를
하나의 Element로 등록하는 방식 중 하나를 정해야 한다. (현행 CUT01 프롬프트는
"기본·표정·각도 시트 3장을 같은 캐릭터 묶음으로 사용한다"고 적혀 있으므로 전자 방식 전제.)
