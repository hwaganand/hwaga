# 제1화 컷 리스트 — 영상 생성용 프롬프트

> 《세 번째 만남》 제1화 · 최악의 소개팅 (0:35 – 1:45)
> 10컷. 각 컷은 그대로 복붙해서 영상 생성에 넣을 수 있게 작성됨.

---

## 0. 사용법 — 반드시 읽을 것

각 컷 프롬프트에는 **VOICES 섹션에 프로필 원문을 통째로 붙여넣어야 한다.**
`@voice_XXX_v1` 태그만 쓰면 모델은 그 목소리를 본 적이 없다 (바이블 F1).
프로필 원문은 `docs/voice-profiles.md` 제1장에 있다.

캐릭터 이미지도 마찬가지다. 컷마다 해당 인물의 레퍼런스를 첨부한다.

| 태그 | 인물 | 레퍼런스 |
|---|---|---|
| `@char_MINJUN_suit_v1` | 신랑 민준 (네이비 풀정장) | job `02b92aef-d68d-4ca7-bf19-d3e9454d3454` ✅확정 |
| `@char_SEOYEON_v1` | 신부 서연 | job `8ef87687-63e0-40b6-bd72-c5f964c0c702` |

⚠️ **이 파일은 초안이다. 채택본은 `docs/episode1-hong.md`(홍자매 톤)이다.**

### 씬 의상 — 시트 의상이 아니다

레퍼런스 시트는 **얼굴 고정용**이다. 1화의 실제 의상은 아래로 갈아입힌다.

| 인물 | 1화 소개팅 룩 |
|---|---|
| 민준 | 갓 다린 하늘색 옥스퍼드 셔츠(맨 위 단추까지) + 네이비 울 블레이저 + 차콜 니트 타이 + 베이지 치노 + 새것 브라운 로퍼 + 왼손목 은색 시계 |
| 서연 | 크림 아이보리 니트 가디건 + 화이트 이너 + 블랙 테일러드 슬랙스 + 블랙 로퍼 + 진주 귀걸이 |

**민준의 "과하게 차려입은 티"가 1화 코미디의 핵심**이다. 넥타이는 소개팅에 과하다 — 그게 포인트다.

### 공통 룩 (전 컷 동일)

```
LOOK: Contemporary Seoul, autumn. Naturalistic cinematic photography,
soft muted color grading with slightly desaturated cool tones.
35mm lens feel, handheld with minimal movement. Shallow but not
extreme depth of field.
NEGATIVE: no on-screen text, no watermark, no logos, no subtitles
burned in, no background music, no score.
```

⚠️ **1~2화는 채도 낮은 쿨톤으로 통일한다.** 3화 손 잡는 순간의 웜톤 전환을 위한 밑작업이다. 여기서 따뜻하게 찍으면 3화가 죽는다.

⚠️ 프롬프트에 `no background music, no score`를 매번 넣는다. 안 넣으면 모델이 음악을 깔아버린다.

---

# 컷 1 — 신부의 집 / 오전

> `자막 카드: 제1화 · 최악의 소개팅`

```
SUBJECT: @char_SEOYEON_v1 — a woman in her mid 20s in her bedroom on a
weekend morning, phone pressed to her ear with one shoulder while she
holds a blouse up against herself in front of a mirror. Two other tops
are already thrown on the bed behind her. She looks at her reflection,
unconvinced, and drops the blouse onto the pile.
WARDROBE: cream ivory ribbed knit cardigan over a white inner top,
black tailored trousers, small pearl stud earrings.
CAMERA: medium shot from behind her shoulder, catching her face in the
mirror. Handheld, almost still.
LIGHTING: soft cool morning daylight through a window, slightly
desaturated grade.

VOICES:
[@voice_JUNGIMO_v1 원문]
[@voice_SEOYEON_v1 원문]

DELIVERY: Jung-imo is coaxing and over-certain, selling hard, entirely
unbothered. Seo-yeon's reply is flat and unconvinced, thrown away
without looking up.
ADDRESSING: A phone conversation. Neither speaks to the room or camera.
SPEAKERS: Two speakers only. Exact lines, no ad-libs, no extra voices.
PROCESSING: Jung-imo is band-limited phone-line audio. Seo-yeon is
unprocessed, close.
DIALOGUE VOLUME: Both voices at clear, natural speech volume, well
above the quiet room tone.

DIALOGUE (Korean):
JUNG-IMO (phone): "진짜 괜찮은 사람이야. 믿어봐."
SEO-YEON: "그 말 저번에도 했어."

SOUND: hangers sliding on a rail, fabric rustle, a zip. Quiet room tone.
```

---

# 컷 2 — 신랑의 집 / 오전 (교차 편집)

```
SUBJECT: @char_MINJUN_v1 — a man in his mid 20s standing in front of a
bathroom mirror, knotting a thin charcoal knit tie. He pulls it undone,
starts again, stops, then wipes both palms down the front of his
trousers.
WARDROBE: crisply ironed light-blue oxford shirt buttoned to the top,
navy wool blazer, thin charcoal knit tie, beige chinos, silver watch on
the left wrist.
CAMERA: medium close-up on the mirror reflection, chest to head.
Handheld, almost still.
LIGHTING: soft cool morning daylight, slightly desaturated grade.

VOICES: none. No dialogue in this shot.
SPEAKERS: Zero speakers. No dialogue, no voice-over, no ad-libs, no
extra voices anywhere in this shot.

SOUND: fabric friction of the tie being pulled, a single exhale,
bathroom room tone. No music.
```

⚠️ **대사 없는 컷에도 `Zero speakers`를 명시한다.** 안 쓰면 모델이 대사를 지어낸다 (바이블 F5).

---

# 컷 3 — 휴대폰 화면 인서트

```
SUBJECT: An extreme close-up of a smartphone screen held in a man's
hand, showing a Korean search engine results page. The thumb scrolls
once, slowly.
CAMERA: extreme close-up, screen fills the frame, slight angle.
LIGHTING: screen glow on the fingers, cool ambient room light.

ON-SCREEN TEXT (rendered inside the phone screen, Korean):
"소개팅 첫 대화 주제 추천"
"소개팅 3분 만에 어색해질 때"

VOICES: none.
SPEAKERS: Zero speakers. No dialogue, no voice-over.
SOUND: a single soft thumb-tap on glass, room tone.
```

😂 **웃음 포인트 ①** — 이 컷은 자막 없이 화면만으로 웃긴다. 2초면 충분하다.

---

# 컷 4 — 카페 문 열림 / 슬로우모션

```
SUBJECT: @char_SEOYEON_v1 — a woman in her mid 20s pushing open a cafe
door and stepping inside. She scans the room. Slow motion.
WARDROBE: cream ivory ribbed knit cardigan over a white inner top,
black tailored trousers, black loafers.
CAMERA: from inside the cafe, medium-wide, low angle, slow push in.
Extreme slow motion, roughly 4x.
LIGHTING: strong backlight through the glass door, a lens flare across
the frame, cool desaturated grade.

VOICES: none.
SPEAKERS: Zero speakers. No dialogue, no voice-over, no extra voices.
Background cafe patrons are unintelligible murmur only.

SOUND: a door chime, then the cafe ambience drops into a heavy
low-passed muffle as if heard underwater, with a slow heartbeat
underneath. No music, no score.
```

⚠️ 여기가 1화의 낚시다. **로맨틱하게 시작해야** 다음 컷의 추락이 산다.

---

# 컷 5 — 침묵

```
SUBJECT: @char_MINJUN_v1 and @char_SEOYEON_v1 seated across a small
cafe table, neither speaking. He turns a water glass a quarter turn.
She glances at the window, then back. Neither makes eye contact for
more than a moment.
WARDROBE: as established.
CAMERA: static two-shot from the side, then cut to an insert close-up
of his hand on the glass.
LIGHTING: flat cafe daylight, cool desaturated grade.

VOICES: none.
SPEAKERS: Zero speakers. No dialogue at all in this shot. No voice-over,
no ad-libs, no extra voices. Background patrons are unintelligible
murmur only.

SOUND: room tone only — a distant espresso machine, faint cutlery.
Deliberately empty. No music, no score, no sound design added to fill
the silence.
```

⚠️ **이 컷은 소리를 채우지 않는 것이 연출이다.** 어색함은 정적이 만든다.
BGM이 없어서 오히려 유리한 구간이다.

---

# 컷 6 — 재난 #1 · 커피

> `자막: 재난 #1`

```
SUBJECT: @char_MINJUN_v1 and @char_SEOYEON_v1 at the cafe table. An
iced americano tips over and spills across the table. Both reach for
the napkin dispenser at the same instant and their hands collide. Both
flinch back sharply.
CAMERA: medium two-shot, quick handheld reframe following the spill.
LIGHTING: flat cafe daylight, cool desaturated grade.

VOICES: none — reactions only.
SPEAKERS: Zero speakers. No intelligible dialogue. Both characters
produce only short involuntary reaction sounds — a sharp inhale and a
small startled sound — caused by the spill and the hand collision.
No words, no ad-libs.

SOUND: ice and liquid hitting the table, napkins pulled fast from a
dispenser, a chair leg scraping. No music.
```

😂 **웃음 포인트 ②**

---

# 컷 7 — 재난 #2 · ERP

> `자막: 재난 #2 — 회사 얘기 20분째`
> `자막: (집에 가고 싶다)`

```
SUBJECT: @char_MINJUN_v1 talking earnestly across the cafe table, small
explanatory hand gestures. @char_SEOYEON_v1 listening with a fixed
polite expression, eyes slightly unfocused.
CAMERA: over-the-shoulder on him, then cut to a static close-up on her
face holding two beats too long.
LIGHTING: flat cafe daylight, cool desaturated grade.

VOICES:
[@voice_MINJUN_v1 원문]
[@voice_SEOYEON_v1 원문]

DELIVERY: Min-jun's delivery is stiff with nerves — he starts sentences
he cannot finish and trails off, filling gaps with work detail because
it is the only ground he is sure of. He is trying to sound composed and
failing. Seo-yeon's reply is minimal, polite and hollow; she is running
out of interest, not being rude.
PHYSICALITY: Both are seated. His tension compresses his voice without
causing stuttering; the words stay intelligible.
ADDRESSING: Every line is addressed across the table to the other
person. Neither speaks to the room or the camera.
SPEAKERS: Two speakers only. Exact lines, no ad-libs, no extra voices.
DIALOGUE VOLUME: Dialogue at clear, natural speech volume, well above
the cafe room tone.

DIALOGUE (Korean):
MIN-JUN: "그래서 저희 팀이 그… ERP를…"
SEO-YEON: "아… 네…"

SOUND: cafe room tone, a cup set down somewhere off screen. No music.
```

---

# 컷 8 — 재난 #3 · 말 겹침

> `자막: 재난 #3 — 헤어질 때`

```
SUBJECT: @char_MINJUN_v1 and @char_SEOYEON_v1 standing outside the cafe,
about to part. Both start speaking at the same moment, both stop. A beat
of stillness, then an awkward small bow from each, out of sync.
CAMERA: medium two-shot, static, slight distance between them held in
frame.
LIGHTING: overcast daylight, cool desaturated grade.

VOICES:
[@voice_MINJUN_v1 원문]
[@voice_SEOYEON_v1 원문]

DELIVERY: Both are flustered and over-polite.
OVERLAP: The two lines are spoken simultaneously and collide. Neither
line is cleanly audible over the other. Both stop abruptly at the same
moment, followed by two full seconds of silence before either moves.
ADDRESSING: Each speaks to the other, not to the street or the camera.
SPEAKERS: Two speakers only. Exact lines, no ad-libs, no extra voices.
DIALOGUE VOLUME: Dialogue at clear, natural speech volume.

DIALOGUE (Korean):
MIN-JUN: "다음에 또—"
SEO-YEON: "저 이만—"

SOUND: street ambience, a passing car. Then the two-second gap carries
room tone only. No music.
```

😂 **웃음 포인트 ③** — 겹치는 소리와 **2초의 정적**이 이 컷의 전부다. 정적을 자르지 말 것.

---

# 컷 9 — 신부 인터뷰 / V.O.

```
SUBJECT: @char_SEOYEON_v1 seated on a plain chair against a neutral
wall, present day, speaking to an unseen interviewer just off camera.
She half-laughs before answering.
WARDROBE: cream ivory ribbed knit cardigan over a white inner top.
CAMERA: static medium close-up, eyeline slightly off-lens.
LIGHTING: soft even interview lighting, neutral grade — visibly
different from the cafe scenes.

VOICES:
[@voice_SEOYEON_v1 원문]

DELIVERY: Dry and faintly amused, as if she still cannot believe it.
A half-laugh sits under the line. She is recalling, not performing.
ADDRESSING: Spoken to the unseen interviewer, never to the camera.
SPEAKERS: One speaker only. Exact line, no ad-libs, no extra voices.
PROCESSING: Close-mic'd, completely dry, no room reverb.
DIALOGUE VOLUME: Dialogue at clear, natural speech volume, well above
the ambience.

DIALOGUE (Korean):
SEO-YEON: "심장이요? 안 뛰었어요. 진짜 1도."

SOUND: quiet interior room tone only. No music.
```

⚠️ 이 컷의 **조명과 색이 카페 씬과 확실히 달라야** 시점이 구분된다.
현장(쿨톤·공간감) ↔ 인터뷰(뉴트럴·건조). 이 대비가 영상 구조를 설명한다.

---

# 컷 10 — 밤 11시 47분 / 후크

```
SUBJECT: @char_SEOYEON_v1 lying in bed in a dark room, lit only by her
phone screen. The screen shows a Korean messenger conversation. Her
thumb hovers over the screen and stops, unmoving.
CAMERA: close-up on the phone screen filling most of the frame, her
face soft and partly visible behind it. Then a slow push to her eyes.
LIGHTING: near darkness, only phone-screen light on her face, cool grade.

ON-SCREEN TEXT (rendered inside the messenger, Korean):
"오늘 제가 너무 긴장해서 실수가 많았어요."
"혹시… 딱 한 번만 더 기회 주실 수 있을까요?"
Timestamp visible: 11:47 PM

VOICES: none.
SPEAKERS: Zero speakers. No dialogue, no voice-over, no extra voices.

SOUND: a single messenger notification chime, then complete silence
except faint room tone. The silence holds. No music, no score.
```

**암전.**
> `자막: 그래서, 다시 만났을까요?`

⚠️ 이 컷이 1화 전체의 후크다. **알림음 하나 뒤의 정적**이 길수록 좋다.
읽음 표시 `1`이 사라지는 디테일은 후반 작업으로 넣는 게 확실하다.

---

## 컷별 길이 배분 (총 70초)

| 컷 | 내용 | 길이 |
|---|---|---|
| 1 | 신부의 집 · 전화 | 7초 |
| 2 | 신랑의 집 · 넥타이 | 5초 |
| 3 | 폰 검색 인서트 | 3초 |
| 4 | 카페 문 · 슬로우 | 6초 |
| 5 | 침묵 | 8초 |
| 6 | 재난 #1 커피 | 5초 |
| 7 | 재난 #2 ERP | 10초 |
| 8 | 재난 #3 말 겹침 | 8초 |
| 9 | 인터뷰 V.O. | 6초 |
| 10 | 밤 11시 47분 | 12초 |

침묵(컷5)과 후크(컷10)에 길이를 몰아줬다. **웃긴 컷은 짧게, 감정 컷은 길게.**

## 출고 전 체크

- [ ] 각 컷 VOICES에 **프로필 원문**을 넣었는가 (태그만 쓰지 않았는가)
- [ ] 대사 없는 컷에 `Zero speakers`를 명시했는가
- [ ] 모든 컷에 `no background music, no score`가 들어갔는가
- [ ] 대사 있는 컷에 `DIALOGUE VOLUME`을 명시했는가
- [ ] 캐릭터 레퍼런스 이미지를 컷마다 첨부했는가
- [ ] 컷 5·8·10의 **정적**을 자르지 않았는가
- [ ] 1화 전체가 채도 낮은 쿨톤인가 (인터뷰 컷만 뉴트럴)
