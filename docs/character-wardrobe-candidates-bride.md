# 서연 의상 후보 50 — 이미지 편집용 프롬프트

> 베이스: `@char_SEOYEON_v2` (media `602a8bd9-97b3-4225-bb97-ac96c4ebfc0d`,
> 전신 정면·후면·얼굴 클로즈업 시트 — 유일한 확정 기준 사진). 이 사진에
> 아래 프롬프트를 `WARDROBE:` 자리에 얹어서 의상만 바꾼다.
>
> ⚠️ **3화까지만 대본이 있다.** 아래 중 "3화" 라벨이 붙은 항목만 실제 장면
> 근거가 있고, 나머지는 전부 상황을 가정한 후보다 — 대본이 나오면 갈아엎을
> 각오로 본다.
>
> ⚠️ 이미 확정된 룩(1화 크림 가디건, 2화 차콜 니트+미디스커트, 2화 원피스/실내복)은
> 여기 다시 안 넣었다. 캐스트 색 설계상 서연은 **크림 아이보리 + 블랙**이
> 기본 팔레트라, 후보들도 대부분 그 안에서 움직이고 색이 들어가는 항목은
> 의도적으로 표시했다.

```python
prompts = [
    # ── 캐주얼 데이트 (5) ──
    "A cream ribbed knit cardigan over a white cotton camisole, straight light-wash denim, white leather sneakers, small pearl stud earrings.",
    "A soft blush-pink knit sweater tucked into a black pleated midi skirt, black ballet flats, a thin gold necklace.",
    "A pale lavender cotton blouse with puffed sleeves, straight ivory trousers, tan suede loafers.",
    "A white cropped knit vest over a light blue collared shirt, straight khaki trousers, white canvas sneakers.",
    "A soft grey oversized cardigan over a plain white t-shirt, black skinny jeans, white sneakers, small hoop earrings.",

    # ── 스마트 캐주얼 / 저녁 데이트 (5) ──
    "A fitted black turtleneck under a cream wool blazer, straight black trousers, black kitten-heel pumps, delicate gold layered necklaces.",
    "A dusty-rose satin blouse with a soft bow at the collar, black tailored trousers, black pointed-toe flats.",
    "A charcoal wrap dress, knee-length, cinched at the waist, black ankle boots, small pearl earrings.",
    "A cream silk camisole under an open ivory blazer, straight black trousers, nude pointed-toe heels.",
    "A deep burgundy velvet midi dress, long sleeves, black ankle boots, a thin gold chain necklace.",

    # ── 비 오는 날 (3) ──
    "A translucent ivory PVC raincoat over a plain white t-shirt and black leggings, black rain boots, hair pulled back in a low ponytail.",
    "A pale yellow rain jacket, hood down, over a grey sweater and dark jeans, white sneakers already damp at the toe.",
    "A cropped black trench coat, belted, over a cream knit sweater, straight jeans, black ankle boots, a small umbrella held loosely.",

    # ── 3화 — 회사, 밤, 지친 퇴근길 (2) ──
    "A simple white blouse with the sleeves slightly wrinkled, a grey pencil skirt, black flats, hair falling loose after a long day at the office, no jewelry.",
    "A soft ivory cardigan thrown over a plain white blouse and black trousers, flat black loafers, a laptop bag over one shoulder, visibly tired.",

    # ── 친구들과 만남 / 그룹 (3) ──
    "A yellow knit crop top under a light denim overshirt, straight white trousers, white sneakers, small gold hoop earrings.",
    "A striped navy-and-white long-sleeve top, black wide-leg trousers, white sneakers, a canvas tote bag.",
    "A soft mint-green cardigan over a white camisole, light wash denim shorts, white sneakers.",

    # ── 부모님 / 격식 있는 자리 (3) ──
    "A cream silk blouse with a soft tie neck, a black tailored pencil skirt, black kitten heels, small pearl earrings and a thin pearl necklace.",
    "A pale powder-blue wool dress, knee-length, long sleeves, nude flats, a delicate gold necklace.",
    "An ivory knit twin-set — cardigan and matching sleeveless top — over a black pleated skirt, black flats, pearl stud earrings.",

    # ── 갈등 / 무거운 씬 (3) ──
    "A plain black long-sleeve top and dark grey trousers, no jewelry, hair pulled back tightly, no makeup emphasis.",
    "A wrinkled white shirt untucked over black leggings, hair undone, visibly not put-together.",
    "An oversized grey sweater with sleeves pulled over her hands, black leggings, no shoes.",

    # ── 화해 / 밝은 회복 씬 (3) ──
    "A soft peach knit sweater, straight ivory trousers, white flats, a thin gold necklace, hair styled softly.",
    "A white broderie-anglaise blouse, light blue denim skirt, white sneakers, small pearl earrings.",
    "A pale yellow cardigan over a white camisole, straight cream trousers, tan flats.",

    # ── 겨울 (5) ──
    "A cream wool coat, belted at the waist, over a black turtleneck and black trousers, black leather boots, a soft grey scarf.",
    "A black puffer coat over a cream knit sweater, dark jeans, white sneakers, a knit beanie in oatmeal.",
    "A camel wool coat over a white turtleneck, straight black trousers, brown leather boots, small gold earrings.",
    "A chunky oatmeal turtleneck sweater, black pleated skirt, black knee-high boots, a soft knit scarf in ivory.",
    "A quilted ivory long coat over a black sweater, straight dark jeans, black ankle boots, black leather gloves held rather than worn.",

    # ── 여름 (5) ──
    "A white broderie-anglaise sundress, thin straps, tan leather sandals, a small straw bag.",
    "A pale blue linen sleeveless blouse tucked into white linen shorts, white canvas sneakers.",
    "A soft yellow cotton sundress with a square neckline, white sandals, small gold hoop earrings.",
    "A white cotton camisole under an open pale mint short-sleeve shirt, light denim shorts, white sneakers.",
    "A cream linen wrap dress, short sleeves, tan woven sandals, a straw sun hat held in hand.",

    # ── 야외 나들이 / 이벤트 (4) ──
    "A soft pink knit cardigan over a white dress, straight black leggings underneath for warmth, white sneakers — cherry-blossom-picnic styling.",
    "A cream quilted vest over a white long-sleeve top, straight jeans, brown ankle boots, a knit beanie.",
    "A white ribbed base layer under a light blue ski jacket, black ski trousers, a knit hat, snow goggles pushed up on her forehead.",
    "A white linen cover-up over a black one-piece swimsuit, bare feet, a wide-brim straw hat — beach-day styling.",

    # ── 여행 / 공항 (2) ──
    "An oversized cream wool coat over a black turtleneck, straight black trousers, white sneakers, a small crossbody bag.",
    "A soft grey hoodie under an open beige trench coat, black leggings, white sneakers, pulling a cream carry-on suitcase.",

    # ── 홈웨어 (3) ──
    "A plain white oversized t-shirt and grey jersey shorts, bare feet, hair in a loose bun.",
    "A soft pastel-pink waffle-knit robe over a white camisole and shorts, no shoes.",
    "A plain ivory long-sleeve loungewear set, matching top and trousers, hair down, no makeup emphasis.",

    # ── 프로포즈 / 결혼 관련 포멀 (4) ──
    "A cream silk slip dress, midi length, delicate spaghetti straps, nude heels, a thin gold necklace and small pearl earrings.",
    "A pale blush chiffon dress with long sleeves and a soft flowing skirt, nude pointed-toe heels, hair styled in soft waves.",
    "A full ivory wedding-adjacent gown, off-shoulder neckline, floor-length, delicate lace detailing, hair in an updo, pearl drop earrings — reserved only for the most formal possible scene.",
    "A soft champagne-gold satin dress, knee-length, thin straps, nude heels, a delicate gold necklace — warm-toned and elevated, breaking deliberately from her usual cream/black palette for this one culminating scene.",
]
```

## 카테고리 요약

| 구간 | 개수 |
|---|---|
| 캐주얼 데이트 | 5 |
| 스마트 캐주얼/저녁 데이트 | 5 |
| 비 오는 날 | 3 |
| 3화 (회사·퇴근길) | 2 |
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

⚠️ 색 규칙 — **웜톤/유채색이 두드러지는 포멀(샴페인골드 드레스 등)은 프로포즈급
장면에만** 넣었다. 나머지 46개는 서연의 기본 팔레트(크림 아이보리+블랙)
안에서 파스텔 톤으로만 변주했다 — 캐스트 색 설계표(2화 문서)와 안 부딪히게.
