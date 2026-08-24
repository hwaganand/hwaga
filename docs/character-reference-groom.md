# 캐릭터 레퍼런스 시트 — 신랑(남자 주인공) 「민준」

> 식전영상 《세 번째 만남》 재현 컷용 캐릭터 일관성 레퍼런스
> **버전 3 — 확정 레퍼런스 이미지(3분할 시트) 기준으로 고정**

---

## 0. 기준 이미지

사용자가 확정한 3분할 시트(전신 정면 / 전신 후면 / 얼굴 클로즈업)를 **사진1로 확정**한다.
남은 산출물은 두 장:

| # | 구성 | 상태 |
|---|---|---|
| 사진1 | 전신 정면 / 후면 / 얼굴 클로즈업 | ✅ **확정** (기준 이미지) |
| 사진2 | 표정 4종 | ⬜ 생성 대기 |
| 사진3 | 얼굴 4방향 턴어라운드 | ⬜ 생성 대기 |

**사진2·3은 반드시 기준 이미지를 레퍼런스로 첨부해서 생성한다.** 텍스트만으로 뽑으면 얼굴이 흔들린다.

---

## 1. 얼굴 특징 고정 문구 ★ 두 장에 토씨 하나 안 틀리고 동일하게

**한글**
```
20대 초반의 매우 잘생긴 한국인 남성, 한국 아이돌·드라마 남주 비주얼.
갸름한 V라인 계란형 얼굴, 섬세하지만 또렷한 턱선, 좁은 턱끝,
높지만 부드러운 광대.
맑은 쌍꺼풀이 있는 아몬드형 눈, 따뜻한 갈색 홍채,
바깥쪽 눈꼬리가 살짝 아래로 내려가 순한 인상, 길고 짙은 속눈썹,
차분하고 곧은 시선.
짙고 도톰한 일자 눈썹에 아주 완만한 아치, 눈과 가깝게 낮게 자리 잡음.
곧고 가느다란 콧대에 작고 정제된 코끝.
또렷한 큐피드 보우의 부드럽고 도톰한 입술, 자연스러운 로즈 톤,
얼굴 대비 작은 입.
밝고 매끈한 웜 아이보리 피부, 잡티 없이 은은한 광채,
아주 미세한 자연 질감만 남을 것.
```

**English**
```
An extremely handsome Korean man in his early 20s, Korean idol / K-drama
leading-man visuals.
Slim V-line oval face, delicate but clearly defined jawline, narrow chin,
high yet soft cheekbones.
Almond-shaped eyes with clear double eyelids, warm brown irises,
slightly downturned outer corners giving a gentle look, long dark lashes,
calm steady gaze.
Thick straight dark eyebrows with a very slight arch, set low and close to the eyes.
Straight narrow nose bridge with a small refined tip.
Soft full lips with a well-defined cupid's bow, natural rose tone,
small mouth relative to the face.
Fair, smooth warm-ivory skin, blemish-free with a subtle healthy glow,
only the very finest natural skin texture.
```

## 1-1. 헤어 고정 문구

**한글**
```
검정에 가까운 아주 짙은 머리색, 중간 길이.
윗머리는 볼륨감 있게 부드러운 웨이브와 컬이 자연스럽게 엉킨 질감,
앞머리는 옆으로 흘러 이마를 일부 덮음.
옆머리는 짧게 정리되어 귀가 드러남. 바람에 날리지 않은 고정 스타일링, 매트 마감.
```

**English**
```
Very dark near-black hair, medium length.
Voluminous textured top with soft loose waves and curls tangled naturally,
fringe swept to one side partially covering the forehead.
Sides tapered short with the ears exposed.
Styled and static with no wind, matte finish.
```

## 1-2. 체형 고정 문구

**한글**
```
키가 크고 매우 마른 체형, 좁은 어깨와 가는 허리, 다리가 길고 비율이 좋음.
```

**English**
```
Tall and very slim build, narrow shoulders, slim waist, long legs, excellent proportions.
```

---

## 2. 세트 고정 (기준 이미지와 동일하게)

앞 버전의 회색 배경 / 네이비 블레이저는 **폐기**. 기준 이미지에 맞춘다.

| 항목 | 확정값 |
|---|---|
| 배경 | 웜 베이지·그레이지 톤의 은은한 질감 벽, 심리스 |
| 조명 | 부드럽고 따뜻한 확산광, 정면에서 살짝 측면, 그림자 약함 |
| 의상 | 아이보리(크림) 릴랙스핏 포플린 셔츠 — 첫 단추 풀고 카라 오픈, 긴소매 / 블랙 테일러드 스트레이트 슬랙스 / 블랙 가죽 더비 슈즈 |
| 액세서리 | 없음 |

씬별 의상(비 오는 날 코트, 회사 앞 밤, 웨딩 턱시도)은 **시트가 아니라 실제 재현 컷 단계**에서 갈아입힌다.

---

# 3. 프롬프트 — 사진 2 (표정 4종)

**기준 이미지를 레퍼런스로 첨부하고 생성할 것.**

**한글**
```
첨부한 레퍼런스 이미지와 완전히 동일한 인물.
웜 베이지 톤의 은은한 질감 배경, 얇은 세로 구분선으로 나눈 4분할 구도.
각 패널은 목까지만 보이는 정면 클로즈업이며, 표정만 다르게 연출:

1) 긴장해서 굳은 어색한 미소 — 입꼬리만 살짝 올라가고 눈은 안 웃음
2) 커피를 쏟은 직후의 당황 — 눈이 커지고 입이 살짝 벌어짐, 눈썹이 올라감
3) 진심을 말할 때의 담담하고 흔들림 없는 눈빛 — 표정은 거의 없지만 시선이 곧음
4) 마음 놓고 웃는 진짜 미소 — 눈가에 옅은 주름

{얼굴 특징 고정 문구}
{헤어 고정 문구}

의상: 아이보리 포플린 셔츠, 첫 단추 풀고 카라 오픈 — 4패널 동일.
조명: 부드럽고 따뜻한 확산광, 4패널 방향과 톤 완전 동일.
헤어스타일, 카메라 각도, 얼굴 생김새는 4패널 모두 완전히 동일하게 유지.

제외: 텍스트·워터마크·로고·프레임 테두리 금지, 보케·얕은 심도 금지,
머리카락 날림 금지, 패널당 인물 한 명, 소품·가구·배경 오브젝트 금지,
전신 금지(얼굴 클로즈업만), 플라스틱·왁스 같은 CGI 피부 금지.
```

**English**
```
The exact same person as in the attached reference image.
Warm beige subtly textured seamless background, 4-panel composition divided by
thin vertical dividers. Each panel is a front-facing close-up cropped at the neck,
differing ONLY in expression:

1) stiff awkward smile from nervousness — mouth corners barely raised, eyes not smiling
2) flustered shock right after spilling coffee — widened eyes, slightly open mouth,
   raised eyebrows
3) calm unwavering gaze while speaking sincerely — almost no expression, steady direct look
4) a relaxed genuine smile — faint crinkles at the corners of the eyes

{fixed facial-identity phrase}
{fixed hair phrase}

Wardrobe: ivory poplin shirt, top button undone, open collar — identical in all 4 panels.
Lighting: soft warm diffused light, identical direction and tone across all 4 panels.
Keep hairstyle, camera angle, and facial identity fully identical across all four panels.

NEGATIVE: no text, no watermark, no logos, no frame borders, no bokeh,
no shallow depth of field, no wind-blown hair, exactly one person per panel,
no props, no furniture, no background objects, no full body (face close-up only),
no plastic or waxy CGI skin.
```

---

# 4. 프롬프트 — 사진 3 (얼굴 4방향 턴어라운드)

**기준 이미지를 레퍼런스로 첨부하고 생성할 것.**

**한글**
```
첨부한 레퍼런스 이미지와 완전히 동일한 인물.
웜 베이지 톤의 은은한 질감 배경, 얇은 세로 구분선으로 나눈 4분할 구도.
동일 인물 머리의 4방향 턴어라운드:

1) 완전 측면(프로필, 90도)
2) 45도 측면
3) 정면
4) 완전 후면(뒷머리)

아이보리 포플린 셔츠를 입은 상반신 일부가 함께 보이도록 구성. 무표정.
{얼굴 특징 고정 문구}
{헤어 고정 문구}

조명: 부드럽고 따뜻한 확산광, 4패널 방향과 톤 완전 동일.
헤어스타일, 피부톤, 의상 디테일을 4패널 모두 동일하게 유지.
머리 높이와 크기를 4패널에서 정렬할 것.

제외: 텍스트·워터마크·로고·프레임 테두리 금지, 보케·얕은 심도 금지,
머리카락 날림 금지, 패널당 인물 한 명, 소품·배경 오브젝트 금지,
플라스틱·왁스 같은 CGI 피부 금지.
```

**English**
```
The exact same person as in the attached reference image.
Warm beige subtly textured seamless background, 4-panel composition divided by
thin vertical dividers. A 4-way turnaround of the same person's head:

1) full profile (90°)
2) 3/4 angle (45°)
3) front view
4) full back view (back of the head)

Include part of the upper torso wearing the ivory poplin shirt. Neutral expression.
{fixed facial-identity phrase}
{fixed hair phrase}

Lighting: soft warm diffused light, identical direction and tone across all 4 panels.
Keep hairstyle, skin tone, and costume details identical across all panels.
Align head height and scale across the four panels.

NEGATIVE: no text, no watermark, no logos, no frame borders, no bokeh,
no shallow depth of field, no wind-blown hair, exactly one person per panel,
no props, no background objects, no plastic or waxy CGI skin.
```

---

## 5. 일관성 체크리스트

- [ ] 사진2·3 생성 시 **기준 이미지를 레퍼런스로 첨부**했는가
- [ ] `{얼굴 특징 고정 문구}`가 두 장에 완전히 동일한 문장으로 들어갔는가
- [ ] 배경이 세 장 모두 웜 베이지인가 (회색으로 튀지 않았는가)
- [ ] 조명이 세 장 모두 부드러운 웜 확산광인가
- [ ] 셔츠가 세 장 모두 아이보리 포플린, 첫 단추 풀린 상태인가
- [ ] 헤어 볼륨과 앞머리 방향이 세 장에서 같은가

## 6. 생성 팁

- 턴어라운드의 **후면 패널이 제일 자주 깨진다.** 안 되면 후면만 따로 뽑아 붙이는 게 빠르다.
- 표정 4종에서 사람이 바뀐 것처럼 나오면 표정 묘사를 **더 약하게** 쓴다. "활짝"보다 "옅게 미소"가 정체성 유지에 유리하다.
- 감성 조명(골든아워·역광·보케)은 시트가 아니라 **실제 재현 컷 단계**에서 얹는다. 시트는 설계도다.
- 신부 레퍼런스도 만들 경우 **배경·조명·카메라 거리 문구를 신랑 것과 똑같이** 써야 투샷 합성이 자연스럽다.
