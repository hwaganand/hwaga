# 민준 의상 후보 50 — 이미지 편집용 프롬프트

> 베이스: `@char_MINJUN_base_v2` (job `67b1d302-0a28-4b4b-8ecb-6343f1eaecdd`,
> 아이보리 셔츠+블랙 슬랙스, 얼굴 기준 사진). 이 사진에 아래 프롬프트를
> `WARDROBE:` 자리에 얹어서 의상만 바꾼다.
>
> ⚠️ **3화까지만 대본이 있다.** 아래 중 "3화" 라벨이 붙은 항목만 실제 장면
> 근거가 있고, 나머지는 전부 상황을 가정한 후보다 — 대본이 나오면 갈아엎을
> 각오로 본다.
>
> ⚠️ 이미 확정된 시트(1화 네이비 풀정장, 2화 형광 라임 등산복, 2화 크림
> 니트)는 여기 다시 안 넣었다. 그 세 벌은 그대로 고정.

```python
prompts = [
    # ── 캐주얼 데이트 (5) ──
    "A soft oatmeal-beige cardigan over a plain white crewneck t-shirt, straight-leg indigo denim, white leather sneakers. Relaxed weekend-date styling.",
    "A slim-fit light grey knit polo tucked into tailored taupe chinos, a thin brown leather belt, brown suede loafers. Clean and a little more put-together.",
    "A washed denim shirt jacket over a plain heather-grey t-shirt, straight black jeans, white canvas sneakers. Easy, unstudied off-duty look.",
    "A fine-gauge navy quarter-zip sweater over a white collared shirt with the collar just showing, straight khaki chinos, brown leather sneakers.",
    "A plain sage-green crewneck sweatshirt, black tapered joggers, white running shoes. Deliberately unfussy, almost too casual for a date.",

    # ── 스마트 캐주얼 / 저녁 데이트 (5) ──
    "A fitted black merino turtleneck under a dark olive field jacket, straight dark grey trousers, black leather chelsea boots.",
    "A charcoal knit blazer, unstructured, over a plain white t-shirt, slim black trousers, black leather derbies. No tie, no pocket square.",
    "A deep burgundy corduroy shirt jacket over a black fine-knit sweater, straight indigo denim, dark brown leather boots.",
    "A fitted white dress shirt with the top two buttons open, sleeves rolled to the forearm, dark grey wool trousers, brown leather loafers.",
    "A slim navy cardigan buttoned over a white oxford shirt, grey wool trousers, brown leather derbies. Understated and a little formal for a first proper dinner.",

    # ── 비 오는 날 (3) ──
    "A navy technical rain jacket, unzipped, over a plain grey sweatshirt and black jeans, black waterproof boots. Practical, not stylish.",
    "A translucent PVC raincoat thrown hastily over a wrinkled white shirt, dark trousers, black sneakers already damp at the toe.",
    "A hooded olive-green windbreaker zipped to the chest over a black t-shirt, slim black trousers, dark trail sneakers.",

    # ── 3화 — 회사 앞, 밤, 죽 봉투 (2) ──
    "A dark charcoal wool overcoat worn open over a simple navy crewneck sweater and dark grey trousers, black leather derbies. Neat but clearly off-duty, not dressed up for a date.",
    "A plain black bomber jacket over a grey hoodie, dark jeans, white sneakers, holding a paper takeout bag. Thrown-on-in-a-hurry energy, like he left the house the moment he heard something was wrong.",

    # ── 친구들과 만남 / 그룹 (3) ──
    "A forest-green corduroy overshirt layered over a white t-shirt, straight denim, white sneakers. Slightly more color and texture than his usual neutral palette.",
    "A grey marled hoodie under an unzipped black bomber jacket, black cargo pants, white sneakers. Loud company, quiet outfit.",
    "A mustard-yellow knit vest over a white long-sleeve shirt, straight beige chinos, brown loafers. A single deliberate color note among friends who dress louder than him.",

    # ── 부모님 / 격식 있는 자리 (3) ──
    "A single-breasted charcoal wool blazer over a light blue dress shirt, no tie, top button open, dark grey trousers, black leather shoes.",
    "A soft grey flannel blazer over a white turtleneck, tailored navy trousers, black leather loafers. Formal without a tie, warmer than a full suit.",
    "A dark navy wool waistcoat over a crisp white shirt, sleeves down and buttoned, charcoal trousers, black oxfords. No jacket — trying hard without going all the way to a suit.",

    # ── 갈등 / 무거운 씬 (3) ──
    "A plain black crewneck sweater and dark grey trousers, no accessories, no layering. Deliberately flat and colorless.",
    "A rumpled white dress shirt with the sleeves unevenly rolled, top button undone, no jacket, dark trousers. Looks like he left work without fixing himself up.",
    "A worn grey hoodie, hood down, dark sweatpants. The least put-together he ever looks on screen.",

    # ── 화해 / 밝은 회복 씬 (3) ──
    "A cream cable-knit sweater over a white collared shirt with the collar showing, dark indigo denim, brown leather boots.",
    "A soft powder-blue knit polo, straight beige chinos, white leather sneakers. Lighter, brighter than his usual neutral-cool palette.",
    "A pale grey zip-up cardigan over a white t-shirt, light wash denim, white sneakers. Simple and a little more relaxed in the shoulders than before.",

    # ── 겨울 (5) ──
    "A camel wool overcoat over a fine-gauge navy turtleneck, matching navy trousers, brown leather boots.",
    "A black puffer jacket over a grey hoodie, black jeans, white sneakers, a thin grey scarf loosely wrapped once.",
    "A dark green wool peacoat over a cream turtleneck, straight charcoal trousers, black leather boots.",
    "A chunky oatmeal turtleneck sweater under an unbuttoned dark brown suede jacket, slim black trousers, brown boots.",
    "A quilted navy field jacket over a black merino sweater, dark indigo denim, black leather boots, black leather gloves in hand rather than worn.",

    # ── 여름 (5) ──
    "A short-sleeve white linen shirt, top buttons open, straight beige linen trousers, brown leather sandals.",
    "A plain sky-blue cotton t-shirt under an open short-sleeve checked shirt, light khaki shorts, white canvas sneakers.",
    "A pale grey short-sleeve polo, straight navy chino shorts, white leather sneakers. Clean and simple for a hot day.",
    "A loose white cotton t-shirt tucked into straight indigo denim, sleeves of a thin unbuttoned overshirt rolled to the elbow, white sneakers.",
    "A short-sleeve cream linen button-up, fully buttoned, straight taupe trousers, brown woven leather loafers, no socks.",

    # ── 야외 나들이 / 이벤트 (4) ──
    "A windbreaker in muted forest green, half-zipped over a plain white t-shirt, cargo trousers, hiking sneakers — an intentionally well-fitted version of the episode-2 hiking gag, no neon this time.",
    "A soft grey knit beanie, a black quilted vest over a navy long-sleeve shirt, straight jeans, brown boots. Cherry-blossom-picnic styling.",
    "A black technical ski jacket, unzipped over a grey base layer, dark ski trousers, a knit hat pushed back off his forehead, snow goggles hanging around his neck.",
    "A plain white tank top under an open black linen shirt, swim trunks in navy, bare feet — beach-day styling, visibly less composed than his usual buttoned-up looks.",

    # ── 여행 / 공항 (2) ──
    "An oversized grey wool coat over a black turtleneck, straight black trousers, white sneakers, a small crossbody bag worn across the chest.",
    "A relaxed olive bomber jacket over a plain white t-shirt, straight jeans, white sneakers, wireless earbuds visible, pulling a black carry-on suitcase.",

    # ── 홈웨어 / 무장한 순간 (3) ──
    "A plain grey cotton t-shirt and black jersey shorts, bare feet, hair slightly messy — clearly at home, off duty entirely.",
    "A worn navy hoodie with a faded print barely visible, loose grey sweatpants, one sock missing.",
    "A soft black waffle-knit henley, half-unbuttoned, loose grey lounge trousers, no shoes.",

    # ── 프로포즈 / 결혼 관련 포멀 (4) ──
    "A full matching charcoal wool suit, notch lapels, matching trousers with a sharp crease, a crisp white dress shirt with no tie, top button open, black leather oxfords, a silver watch on the left wrist.",
    "A cream double-breasted wool coat over a fitted black turtleneck and matching black trousers, black leather boots — elevated and warm-toned, breaking deliberately from his usual cool palette.",
    "A full black tuxedo, satin notch lapels, a white formal shirt, black bow tie, black patent leather oxfords — reserved only for the most formal possible scene.",
    "A light grey three-piece wool suit, waistcoat included, a pale blue tie, brown leather oxfords — softer and warmer-toned than the episode-1 navy suit, worn with visible ease instead of nervous stiffness.",
]
```

## 카테고리 요약

| 구간 | 개수 |
|---|---|
| 캐주얼 데이트 | 5 |
| 스마트 캐주얼/저녁 데이트 | 5 |
| 비 오는 날 | 3 |
| 3화 (회사 앞·죽) | 2 |
| 친구들/그룹 | 3 |
| 부모님/격식 | 3 |
| 갈등/무거운 씬 | 3 |
| 화해/밝은 회복 | 3 |
| 겨울 | 5 |
| 여름 | 5 |
| 야외 나들이/이벤트 | 4 |
| 여행/공항 | 2 |
| 홈웨어 | 3 |
| 프로포즈/결혼 포멀 | 4 |
| **합계** | **50** |

⚠️ 색 규칙 하나만 지켰다 — **웜톤 포멀(크림 코트·그레이 스리피스 등)은 프로포즈
급 장면에만** 넣었다. 영상 전체에서 웜톤 전환이 3화 손 잡는 순간 단 한 번이라는
규칙과 안 부딪히게, 나머지 46개는 전부 쿨톤/뉴트럴 팔레트로 유지했다.
