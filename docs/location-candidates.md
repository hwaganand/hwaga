# 장소 배경 후보 50 — 이미지 생성용 프롬프트

> 인물이 없는 **빈 공간 플레이트** 프롬프트다. 캐릭터 레퍼런스(민준/서연
> 의상 후보와 같은 베이스 얼굴 사진)와 같이 `image_references`로 걸어서
> 인물+장소를 함께 생성하거나, 장소만 먼저 빈 플레이트로 뽑아 고정해두고
> 나중에 인물 컷마다 반복해서 걸 수도 있다.
>
> ⚠️ **3화까지만 대본이 있다.** "3화" 라벨 항목만 실제 장면 근거가 있고,
> 나머지는 전부 상황을 가정한 후보다.
>
> ⚠️ 이미 확정된 장소(2화: 남성복 매장·서연의 방·이탈리안 레스토랑·서연의
> 집 현관·밤거리·인터뷰 백드롭)는 여기 다시 안 넣었다 — `location-reference-episode2.md` 참고.
>
> ⚠️ 실존 브랜드 로고·간판 텍스트는 전부 네거티브로 막는다. 카테고리는
> 의상 후보 리스트(민준/서연)와 짝을 맞춰서, 같은 상황이면 옷과 장소를
> 같이 골라 쓸 수 있게 했다.

```python
prompts = [
    # ── 카페 / 실내 데이트 (5) ──
    "A small independent coffee shop interior, warm wood tables, hanging pendant lights, a large street-facing window with soft daylight, a shelf of books in the background, no people, no signage or logos.",
    "A minimalist white-walled cafe with marble tabletops, potted plants near the window, soft natural light, empty chairs, no branding visible.",
    "A cozy dessert cafe with pastel pink walls, a glass display case of cakes softly out of focus in the background, warm afternoon light through sheer curtains.",
    "A bookstore cafe with tall wooden shelves lining the walls, a reading nook with a single armchair, warm lamp light, soft shallow depth of field.",
    "A rooftop cafe terrace with string lights overhead, a city skyline softly blurred in the background, small round tables, golden-hour light.",

    # ── 저녁 데이트 / 레스토랑·바 (5) ──
    "An intimate wine bar interior, dim warm lighting, a dark wood counter, wine bottles on shelves softly out of focus, two bar stools at a small table.",
    "A modern Japanese izakaya interior, warm paper lanterns, a dark wood counter, blurred bottles on shelves, low ambient lighting.",
    "A rooftop bar at night, string lights and the glow of a city skyline behind, a small round table with two stools, warm low lighting.",
    "A French bistro interior, a checkered floor, a small round marble table, brass fixtures, warm evening light through lace curtains.",
    "A quiet steakhouse interior, dark leather booth seating, low warm pendant lighting, a single candle on the table, blurred wine glasses in the background.",

    # ── 비 오는 날 (3) ──
    "A cafe window seat looking out onto a rain-streaked street at dusk, warm interior light contrasting with the cool blue-grey rain outside.",
    "A covered outdoor market alley at night, rain falling just past the awning, string lights reflecting on wet pavement, warm shop lights blurred in the background.",
    "A quiet indoor bookstore with rain visible through a large window, soft warm lamps, tall shelves, empty reading chairs.",

    # ── 3화 — 회사 앞, 밤 (2) ──
    "A modern office building lobby at night, most lights off except a few overhead fluorescents, glass doors reflecting the street outside, an empty reception desk.",
    "A quiet street just outside an office building at night, a convenience store's glow spilling onto the sidewalk, a single streetlamp, an empty street.",

    # ── 친구들과 모임 (3) ──
    "A casual pub interior, wooden tables, string lights, a chalkboard menu softly out of focus in the background, warm dim lighting, empty seats.",
    "A karaoke room interior, colorful mood lighting, a low table with a microphone, patterned sofa seating, no people.",
    "A casual barbecue restaurant interior, low tables with built-in grills, warm lighting, an exposed brick wall, empty seating.",

    # ── 부모님 / 격식 있는 자리 (3) ──
    "An elegant traditional Korean restaurant private room, a low wooden table, floor cushions, soft warm lighting, a paper screen door softly lit from behind.",
    "A formal hotel restaurant dining room, white tablecloths, chandeliers, large windows with a city view, empty tables neatly set.",
    "A quiet tea house interior, wooden furniture, a tea set on a low table, soft natural light through a paper-screened window.",

    # ── 갈등 / 무거운 씬 배경 (3) ──
    "An empty subway platform at night, cold fluorescent lighting, a single bench, no people, a train just visible pulling away in the distance.",
    "A stairwell landing in an apartment building, bare fluorescent light, concrete walls, a single window showing a dark night sky.",
    "A quiet parking garage at night, rows of empty spaces, a single flickering overhead light, cool concrete tones.",

    # ── 화해 / 밝은 회복 씬 배경 (3) ──
    "A sunlit park bench under a large tree, dappled light through leaves, a walking path curving into the background, soft warm daylight.",
    "A quiet riverside walking path at golden hour, warm low sunlight reflecting on the water, a bench in the foreground.",
    "A small neighborhood bakery interior, warm morning light, bread displayed on wooden shelves, a single small table by the window.",

    # ── 겨울 (5) ──
    "A snow-covered park path lined with bare trees, soft overcast winter light, footprints in fresh snow, a single bench dusted with snow.",
    "A warmly lit indoor ice rink cafe area, large windows overlooking the rink, string lights, empty tables.",
    "A cozy living room with a lit fireplace, warm ambient light, a soft blanket draped over an armchair, a window showing snow falling outside.",
    "A winter night street lined with holiday string lights, light snow falling, warm shop windows glowing along the sidewalk.",
    "A ski lodge interior, wooden beams, a large stone fireplace, warm lighting, large windows showing snowy mountains outside.",

    # ── 여름 (5) ──
    "A sunny public park with green lawns, tall trees casting dappled shade, a paved walking path, bright clear daylight.",
    "A quiet beach at golden hour, gentle waves, soft warm light, footprints in the sand, no people.",
    "An outdoor rooftop pool area, blue water reflecting sunlight, lounge chairs, a clear summer sky.",
    "A vibrant night market street, string lights and food stall glows softly blurred in the background, warm summer evening air.",
    "A botanical garden greenhouse, lush green plants, soft diffused sunlight through glass panels, a stone path winding through.",

    # ── 야외 나들이 / 이벤트 (4) ──
    "A cherry blossom park path in full bloom, soft pink petals drifting, warm spring daylight, a bench beneath the trees.",
    "An amusement park at dusk, a Ferris wheel glowing softly in the background, string lights along a walking path, warm colorful ambient light.",
    "A ski resort slope base area, snow-capped mountains in the background, wooden lodge buildings, clear bright winter daylight.",
    "A quiet public beach boardwalk at sunset, warm orange light over the water, a wooden railing in the foreground.",

    # ── 여행 / 공항 (2) ──
    "A modern airport departure hall, large windows showing an airfield, rows of empty seating, soft overhead lighting.",
    "An airport gate waiting area at night, large windows reflecting runway lights, empty rows of seats, a quiet, still atmosphere.",

    # ── 집 / 실내 사적 공간 (3) ──
    "A softly lit modern apartment living room, a large window with sheer curtains, a comfortable sofa, warm evening lamp light.",
    "A minimalist kitchen at night, warm under-cabinet lighting, a small dining table set for two, quiet and empty.",
    "A cozy bedroom with warm lamp light, soft bedding, a window showing city lights at night, quiet and still.",

    # ── 프로포즈 / 결혼 관련 장소 (4) ──
    "A rooftop terrace decorated with soft string lights and candles at dusk, a city skyline glowing in the background, a small table set with two chairs.",
    "An elegant garden venue at golden hour, rows of white chairs facing a floral arch, soft warm evening light.",
    "A grand wedding hall interior, white floral arrangements, a long aisle, soft warm chandelier lighting, empty of guests.",
    "A quiet overlook at night with a full view of a city skyline, string lights along a railing, warm golden light — reserved for the most emotionally significant possible scene.",
]
```

## 카테고리 요약 (의상 리스트와 1:1 매칭)

| 구간 | 개수 |
|---|---|
| 카페/실내 데이트 | 5 |
| 저녁 데이트/레스토랑·바 | 5 |
| 비 오는 날 | 3 |
| 3화 (회사 앞·밤) | 2 |
| 친구들/그룹 | 3 |
| 부모님/격식 | 3 |
| 갈등/무거운 씬 | 3 |
| 화해/밝은 회복 | 3 |
| 겨울 | 5 |
| 여름 | 5 |
| 야외 나들이/이벤트 | 4 |
| 여행/공항 | 2 |
| 집/실내 사적 공간 | 3 |
| 프로포즈/결혼 관련 장소 | 4 |
| **합계** | **50** |

⚠️ 색 규칙 — 의상 후보와 같은 원칙. **웜톤이 노골적인 곳(프로포즈 야경,
웨딩홀)은 마지막 카테고리에만** 넣었고, 나머지 46개는 대체로 자연광·중립
조명 위주로 잡아서 3화 손 잡는 순간의 웜톤 전환과 안 부딪히게 했다.

⚠️ 전부 인물 없는 빈 공간이라 **캐릭터 얼굴 레퍼런스와 같이 걸어도 얼굴이
장소 사진에 물릴 위험이 없다.** 다만 매 컷 같은 장소를 반복해서 써야 하는
경우(레스토랑 사례처럼)는 플레이트 하나를 확정해서 media ID로 고정하고
그 컷들 전부에 재사용하는 걸 권장한다.
