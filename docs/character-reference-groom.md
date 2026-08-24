# 캐릭터 레퍼런스 시트 — 신랑(남자 주인공) 「민준」

> 식전영상 《세 번째 만남》 재현 컷용 캐릭터 일관성 레퍼런스
> 산출물: 이미지 3장 (전신 3분할 / 표정 4분할 / 얼굴 턴어라운드 4분할)

---

## 0. 입력 상태

| 항목 | 상태 |
|---|---|
| 인물 사진 | ⬜ **필요** — 정면 1장, 45도 1장, 측면 1장, 전신 1장 (총 3~4장) |
| 키·체형 | ⬜ **필요** — 예: "178cm, 마른 편" |
| 시나리오 | ✅ 확보 — 로맨틱 코미디 《세 번째 만남》, 현대 한국, 30대 초반 회사원 |
| 화풍 | ✅ 실사 포토리얼 (기본값) |

사진과 키/체형이 들어오면 아래 `{얼굴 특징 고정 문구}`를 실제 얼굴 기반으로 교체한다.
**이 문구는 3장 프롬프트에 토씨 하나 안 틀리고 똑같이 들어가야 한다.** 정체성이 흔들리는 건 대부분 이 문구가 장마다 미묘하게 달라서 생긴다.

---

## 1. 캐릭터 설정

| 항목 | 내용 |
|---|---|
| 이름 | 민준 (신랑 역) |
| 나이대 | 30대 초반 |
| 직업 | 회사원 (사무직) |
| 성격 | 말주변 없음, 표현 서툼, 행동으로 하는 사람 |
| 비주얼 키워드 | **"과하게 차려입은 성실함"** — 소개팅에 힘을 너무 준 티가 나는 단정함 |
| 코미디 포인트 | 옷은 완벽한데 표정이 굳어 있음 / 자세가 미묘하게 경직됨 |

캐릭터의 웃음은 얼굴이 아니라 **"열심히 준비한 티"** 에서 나온다. 프롬프트에 "약간 경직된 자세(slightly stiff posture)"를 넣는 이유다.

---

## 2. 의상 세트

**메인 = 세트 A.** 3장 모두 세트 A로 통일한다. 다른 세트는 씬별 추가 생성용.

| 세트 | 씬 | 구성 |
|---|---|---|
| **A · 소개팅 룩 (메인)** | 1화 | 갓 다린 하늘색 옥스퍼드 셔츠(맨 위 단추까지 잠금) + 네이비 블레이저 + 얇은 니트 넥타이(차콜) + 베이지 치노 + 새것 티 나는 브라운 로퍼 + 은색 메탈 시계 |
| B · 비 오는 날 | 2화 | 차콜 그레이 코트, **오른쪽 어깨만 비에 젖어 색이 진해짐**, 손에 접힌 우산 |
| C · 회사 앞 밤 | 3화 | 화이트 셔츠 소매 걷음, 넥타이 느슨하게 풀림, 손에 종이봉투 |
| D · 인터뷰 컷 | 전 회차 | 편한 라이트 그레이 니트, 무지 배경 앞 의자에 앉은 상반신 |
| E · 웨딩 | 최종화 | 블랙 턱시도, 화이트 보타이, 부토니에 |

---

## 3. 얼굴 특징 고정 문구 (사진 받으면 교체)

**한글 (예시 — 실제 사진 기반으로 덮어쓸 것)**
```
30대 초반 한국인 남성, 갸름한 계란형 얼굴, 쌍꺼풀 없는 부드러운 눈매,
곧은 콧대, 얇고 단정한 입술, 짙고 곧은 눈썹,
짧고 깔끔한 투블럭 검은 머리(이마가 살짝 드러남), 웜 아이보리 피부톤.
```

**English**
```
Korean man in his early 30s, slim oval face, soft monolid eyes,
straight nose bridge, thin well-defined lips, dark straight eyebrows,
short neat two-block black hair with a slightly exposed forehead, warm ivory skin tone.
```

---

# 4. 프롬프트 — 사진 1 (전신 정면 / 후면 / 얼굴 클로즈업)

**한글**
```
플레인 그레이 스튜디오 배경, 사실적인 포토그래피 스타일, 3분할 구도.

왼쪽 패널: 키 {키}, {체형} 체형의 30대 초반 한국인 남성의 전신 정면 샷.
갓 다린 하늘색 옥스퍼드 셔츠(맨 위 단추까지 잠금) 위에 네이비 블레이저,
차콜색 얇은 니트 넥타이, 베이지 치노 팬츠, 새것 티가 나는 브라운 로퍼,
왼쪽 손목에 은색 메탈 시계. 어깨에 힘이 들어간 약간 경직된 자세.
단, 얼굴은 보이지 않도록 고개를 살짝 숙일 것.

가운데 패널: 동일 인물, 동일 의상의 전신 후면(뒷모습) 샷. 같은 경직된 자세.

오른쪽 패널: 동일 인물의 얼굴을 크게 클로즈업한 정면 샷, 무표정.

세 패널 모두 동일한 조명(부드러운 정면 키라이트), 동일한 인물,
동일한 의상 디테일(색상·재질·소품)을 유지할 것.
{얼굴 특징 고정 문구}
피부 질감, 셔츠의 면 조직, 블레이저의 울 질감, 니트 타이의 짜임을 사실적으로 표현.
```

**English**
```
Plain gray studio background, photorealistic photography style, 3-panel composition.

Left panel: full-body front shot of a {height}, {body type} Korean man in his early 30s.
Crisply ironed light-blue oxford shirt buttoned to the top, navy blazer,
thin charcoal knit tie, beige chinos, visibly brand-new brown loafers,
silver metal watch on the left wrist. Slightly stiff posture with tensed shoulders.
Face must NOT be visible — head tilted slightly down.

Center panel: same person, same outfit, full-body back view, same stiff posture.

Right panel: large front-facing close-up of the same person's face, neutral expression.

Keep identical lighting (soft frontal key light), identical identity,
and identical costume details (color/material/props) across all three panels.
{fixed facial-identity phrase}
Render realistic skin texture, cotton weave of the shirt, wool texture of the blazer,
and the knit pattern of the tie.
```

---

# 5. 프롬프트 — 사진 2 (표정 4종)

로맨틱 코미디용으로 표정을 교체했다. 기본 세트(웃음/분노/긴장/고통)는 이 캐릭터에 안 맞는다.

**한글**
```
플레인 그레이 배경, 동일 인물의 얼굴을 4개 패널로 나열.
각 패널은 목까지만 보이는 정면 클로즈업이며 표정만 다르게 연출:

1) 긴장해서 굳은 어색한 미소 — 입꼬리만 올라가고 눈은 안 웃음
2) 커피를 쏟은 직후의 당황 — 눈이 커지고 입이 살짝 벌어짐, 이마에 옅은 땀
3) 진심을 말할 때의 담담하고 흔들림 없는 눈빛 — 표정은 거의 없지만 시선이 곧음
4) 마음 놓고 활짝 웃는 표정 — 눈가에 주름이 잡히는 진짜 웃음

헤어스타일, 조명, 카메라 각도, 얼굴 생김새(눈·코·입 형태)는
4개 패널 모두 완전히 동일하게 유지. 의상은 네이비 블레이저와 차콜 니트 타이로 통일.
{얼굴 특징 고정 문구}
```

**English**
```
Plain gray background, the same person's face shown across 4 panels.
Each panel is a front-facing close-up cropped at the neck, differing only in expression:

1) stiff awkward smile from nervousness — mouth corners raised but eyes not smiling
2) flustered shock right after spilling coffee — widened eyes, slightly open mouth, faint sweat on the forehead
3) calm unwavering gaze while speaking sincerely — almost no expression, but a steady direct look
4) a full relaxed genuine smile — crinkles at the corners of the eyes

Keep hairstyle, lighting, camera angle, and facial identity (eyes/nose/mouth shape)
fully identical across all four panels.
Outfit consistent: navy blazer with charcoal knit tie.
{fixed facial-identity phrase}
```

---

# 6. 프롬프트 — 사진 3 (얼굴 4방향 턴어라운드)

**한글**
```
플레인 그레이 배경, 동일 인물 얼굴의 4방향 턴어라운드를
얇은 세로 구분선으로 나눈 4개 패널.

1) 완전 측면(프로필, 90도)
2) 45도 측면
3) 정면
4) 완전 후면(뒷머리)

네이비 블레이저와 하늘색 옥스퍼드 셔츠, 차콜 니트 타이를 입은 상반신 일부가
함께 보이도록 구성. 무표정.
모든 패널에서 헤어스타일, 조명(부드러운 정면 키라이트), 피부톤,
의상 디테일을 동일하게 유지. 머리 높이와 크기를 4패널에서 정렬할 것.
{얼굴 특징 고정 문구}
```

**English**
```
Plain gray background, 4-panel turnaround of the same person's head,
separated by thin vertical dividers.

1) full profile (90°)
2) 3/4 angle (45°)
3) front view
4) full back view (back of the head)

Include part of the upper torso wearing the navy blazer, light-blue oxford shirt,
and charcoal knit tie. Neutral expression.
Keep hairstyle, lighting (soft frontal key light), skin tone, and costume details
identical across all panels. Align head height and scale across the four panels.
{fixed facial-identity phrase}
```

---

## 7. 일관성 체크리스트

- [ ] 세 장 모두 **같은 레퍼런스 사진 묶음**을 첨부했는가
- [ ] 배경이 세 장 모두 동일한 무지 회색인가
- [ ] `{얼굴 특징 고정 문구}`가 세 장에 **완전히 동일한 문장**으로 들어갔는가
- [ ] 의상(하늘색 셔츠 / 네이비 블레이저 / 차콜 니트 타이 / 베이지 치노 / 브라운 로퍼)이 세 장에서 같은가
- [ ] 조명이 세 장 모두 "부드러운 정면 키라이트"인가
- [ ] 시계가 세 장 모두 왼쪽 손목에 있는가 (소품 위치는 자주 뒤집힌다)

## 8. 생성 팁

- **사진1을 먼저 뽑고, 마음에 드는 결과를 사진2·3의 레퍼런스로 재투입**한다. 원본 사진만 넣는 것보다 얼굴이 훨씬 덜 흔들린다.
- 턴어라운드(사진3)의 **후면 패널이 제일 자주 깨진다.** 안 되면 4패널을 한 번에 뽑지 말고 후면만 따로 뽑아서 붙이는 게 빠르다.
- 표정 4종에서 얼굴이 사람이 바뀐 것처럼 나오면, 표정 묘사를 **더 약하게** 쓴다. "활짝"보다 "옅게 미소"가 정체성 유지에 유리하다.
- 신부 레퍼런스도 만들 경우, **조명·배경·카메라 거리 문구를 신랑 것과 똑같이** 써야 나중에 투샷 합성이 자연스럽다.
