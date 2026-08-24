# 제1화 — 홍자매 톤 버전

> 《세 번째 만남》 제1화 · 최악의 소개팅
> 티키타카 로코 문법으로 재작성. **하이브리드 B안의 1화.**

---

## 0. 톤 — 전 화 홍자매 통일 ★확정

| 화 | 톤 |
|---|---|
| 1화 | 홍자매 |
| 2화 | 홍자매 |
| 3화 | 홍자매 |
| 최종화 | 홍자매 |

**작가를 섞지 않는다.** 하이브리드(3화만 임상춘) 안은 폐기됐다.

### 홍자매는 감정 씬도 홍자매로 쓴다

톤을 통일한다고 3화가 약해지지 않는다. 방식이 다를 뿐이다.

| | 임상춘 | 홍자매 |
|---|---|---|
| 감정 만드는 법 | 촌스럽고 담백한 대사로 정면 돌파 | **티키타카를 하다가 한 사람이 안 받아침** |
| 전환 신호 | 톤 자체가 바뀜 | **리듬이 깨짐** |
| 관객이 느끼는 것 | "갑자기 진지해졌다" | **"어? 왜 대답을 못 하지"** |

**핵심 장치: 받아치던 사람이 멈춘다.**
1~2화 내내 두 사람은 말을 주고받는다. 3화에서 서연이 처음으로 받아치지 못한다.
웃다가 조용해지는 게 아니라, **웃기려던 사람이 실패하는 순간**이 감정이다.

이게 톤을 바꾸는 것보다 낫다. 하객 입장에서 이질감이 없고,
1~2화에서 쌓아온 티키타카가 그대로 무기가 된다.

### 3화 고백 — 홍자매 버전

```
SEO-YEON: "왜 왔어요?"
MIN-JUN: "아, 그… 이거 주려고요."
SEO-YEON: "뭔데요."
MIN-JUN: "죽이요."
SEO-YEON: "…죽이요?"
MIN-JUN: "네. 죽."
SEO-YEON: "…아니 왜 죽을."
MIN-JUN: "아플 때 먹는 거니까요."
SEO-YEON: "저 안 아픈데요."
MIN-JUN: "…"
(사이)
MIN-JUN: "…아파 보이는데요."
(서연, 대답하지 못한다. 이 화에서 처음이다)
MIN-JUN: "제가 말을 잘 못해서요. 자꾸 이상한 걸 사와요."
MIN-JUN: "근데 앞으로도 계속 이럴 거예요."
```

**"…아파 보이는데요"에서 리듬이 깨진다.**
그 앞까지는 완벽한 티키타카다. 죽 얘기로 여덟 번을 주고받는다.
그러다 민준이 한 박자 늦게, 원래 하려던 말이 아닌 말을 한다.
서연은 받아치지 못한다 — **1~2화를 통틀어 처음이다.**

민준 캐릭터는 그대로다. 말주변 없고, 표현 서툴고, 행동으로 하는 사람.
보이스 프로필의 `never a smooth, confident or charismatic delivery`가 여기서 정점을 찍는다.
**고백이 안 유창해서** 감정이 산다.

---

## 0-0. 확정 레퍼런스 ★ 컷 생성 시 이것을 건다

| 태그 | 인물 | 레퍼런스 |
|---|---|---|
| `@char_MINJUN_suit_v1` | 신랑 (네이비 풀정장) | job `02b92aef-d68d-4ca7-bf19-d3e9454d3454` |
| `@char_SEOYEON_v2` | 신부 | media `602a8bd9-97b3-4225-bb97-ac96c4ebfc0d` |

보이스는 `docs/voice-profiles.md`의 프로필 **원문**을 VOICES 섹션에 통째로 복붙한다.

---

## 0-1. 파이프라인 검증 완료 ★

**컷 6을 Seedance 2.5로 실제 생성해서 확인했다. 수정 없이 확정.**

| 검증 항목 | 결과 |
|---|---|
| BGM 차단 (`no background music, no score, no soundtrack`) | ✅ |
| 대사 겹침 (OVERLAP 블록) | ✅ |
| 얼굴 유지 (레퍼런스 2인 동시) | ✅ |
| 앰비언스 소거 (손 닿는 순간) | ✅ |

생성 조건: `seedance_2_5` / `omni_reference` / 16:9 / 10초 / 1080p / `generate_audio: true`
job `29f0a60e-bff1-4599-86e2-2c8cd967e1b4`

**이 컷의 프롬프트 구조를 나머지 9컷에 그대로 쓴다.**
특히 아래 세 가지는 검증된 문구이므로 바꾸지 않는다.

1. VOICES 섹션에 프로필 **원문 전체**를 넣는다 (태그 참조 금지)
2. 네거티브에 `no background music, no score, no soundtrack` **세 개를 다** 넣는다
3. 대사 없는 컷에는 `Zero speakers` 잠금을 명시한다

⚠️ 중간에 "IN THE DARK" 프리셋 추천이 뜨면 거절한다 (`declined_preset_id`).
밝은 카페 씬과 정반대다.

---

## 1. 홍자매 문법 vs 임성한 문법

정반대다. 같은 컷을 정확히 반대로 찍는다.

| | 임성한 | 홍자매 |
|---|---|---|
| 리듬 | 느리고 무겁게 | **빠르고 가볍게** |
| 정적 | 늘려서 견딜 수 없게 | **대사로 감싼다** |
| 대사 | 문어체, 선언 | **구어체, 핑퐁** |
| 클로즈업 | 감정 과장용 | **개그 리액션용** |
| 컷 길이 | 길게 버팀 | **짧게 끊어 침** |
| 속마음 | 정면 응시 독백 | **V.O. 혼잣말** |

### 홍자매 시그니처 6가지

| # | 장치 | 이 화에서 |
|---|---|---|
| 1 | **티키타카** | 대사가 핑퐁처럼 빠르게 오감 |
| 2 | **말꼬리 잡기** | 상대 말의 단어를 되받아침 |
| 3 | **V.O. 혼잣말** | 속마음이 실시간으로 흐름 |
| 4 | **러닝 개그** | 한 요소가 계속 돌아옴 → **넥타이** |
| 5 | **정적을 대사로 감싸기** | "저기…" "네." "…아니에요." |
| 6 | **회수** | 마지막에 러닝 개그를 되갚음 |

⚠️ **이 화의 러닝 개그는 "넥타이"다.**
컷 2에서 심고 → 컷 3에서 키우고 → 컷 4에서 써먹고 → **컷 10에서 회수한다.**
회수가 이 버전의 가장 큰 무기다. 임성한 버전에는 없는 구조다.

---

## 2. 보이스 — 딜리버리만 교체

**고정층 프로필은 건드리지 않는다.** `docs/voice-profiles.md` 원문 그대로.

홍자매 딜리버리 공통 문구:
```
DELIVERY (romcom register): Lines are traded quickly and lightly,
overlapping at the edges as in natural conversation. Delivery is
colloquial and unforced, never declarative or literary. Reactions land
fast. When a pause happens it is short and awkward rather than weighty,
and it is broken by speech rather than held.
```

⚠️ 이건 **변동층**이다. 3화에서는 이 문단을 빼고 임상춘 딜리버리로 교체한다 (바이블 F3).

---

# 3. 컷 리스트 — 홍자매 버전

## 컷 1 — 신부의 집 / 오전

> `자막 카드: 제1화 · 최악의 소개팅`

```
SUBJECT: @char_SEOYEON_v1 holding a top against herself in front of a
mirror, phone wedged against her shoulder. She swaps it for another,
then goes back to the first one. Two more lie on the bed.
CAMERA: medium shot catching her in the mirror, quick reframes with
each swap. Handheld, light.
LIGHTING: cool morning daylight, slightly desaturated.

VOICES:
[@voice_JUNGIMO_v1 원문]
[@voice_SEOYEON_v1 원문]
[홍자매 딜리버리 공통 문구]

DELIVERY: Jung-imo is cheerfully unbothered and pushing hard. Seo-yeon
answers fast and dry, barely looking up, landing each reply on the beat.
ADDRESSING: A phone conversation. Neither speaks to the room or camera.
SPEAKERS: Two speakers only. Exact lines, no ad-libs, no extra voices.
PROCESSING: Jung-imo is band-limited phone-line audio.
DIALOGUE VOLUME: Both voices at clear, natural speech volume, well above
the quiet room tone.

DIALOGUE (Korean):
JUNG-IMO (phone): "야, 이번엔 진짜다."
SEO-YEON: "언니 '진짜'는 지난번이 세 번째였어."
JUNG-IMO (phone): "그라믄 이번이 네 번째제."
SEO-YEON: "…그게 자랑이야?"

SOUND: hangers sliding, fabric rustle, a zip. Quiet room tone. No music.
```

😂 **말꼬리 잡기(장치 2)** — "진짜"를 되받아친다. 첫 컷부터 리듬을 잡는다.

---

## 컷 2 — 신랑의 집 / 오전 ★러닝 개그 심는 컷

```
SUBJECT: @char_MINJUN_v1 in front of a mirror rehearsing a greeting to
his own reflection, adjusting his expression each time. He glances down
at his thin knit tie, tugs it, and grimaces slightly.
WARDROBE: crisply ironed light-blue oxford shirt buttoned to the top,
navy wool blazer, thin charcoal knit tie, beige chinos.
CAMERA: medium close-up on the reflection. Quick cuts between each
attempt.
LIGHTING: cool morning daylight, slightly desaturated.

VOICES:
[@voice_MINJUN_v1 원문]
[홍자매 딜리버리 공통 문구]

DELIVERY: He is rehearsing, correcting himself out loud between
attempts, entirely earnest and slightly embarrassed. Each attempt has a
different, badly chosen tone.
ADDRESSING: He speaks to his own reflection. Not to the camera.
SPEAKERS: One speaker only. Exact lines, no ad-libs, no extra voices.
DIALOGUE VOLUME: Dialogue at clear, natural speech volume.

DIALOGUE (Korean):
MIN-JUN: "안녕하세요."
MIN-JUN: "…아니 너무 딱딱한가."
MIN-JUN: "안녕하세요~"
MIN-JUN: "…이건 좀 느끼한데."
MIN-JUN (looking down at the tie): "…넥타이는 좀 아닌가."

SOUND: fabric friction, a small sigh, room tone. No music.
```

⚠️ **여기서 넥타이를 심는다.** 앞으로 세 번 더 돌아온다.

---

## 컷 3 — 휴대폰 검색 인서트 ★러닝 개그 키우는 컷

```
SUBJECT: Extreme close-up of a phone screen showing Korean search
results. The thumb scrolls down through three queries.
CAMERA: extreme close-up, screen fills frame.
LIGHTING: screen glow, cool ambient.

ON-SCREEN TEXT (Korean, inside the phone):
"소개팅 첫 대화 주제 추천"
"소개팅 넥타이 오바인가요"
"넥타이 안 매면 성의 없어 보이나요"

VOICES: none.
SPEAKERS: Zero speakers. No dialogue, no voice-over, no extra voices.
SOUND: soft thumb-taps on glass, room tone. No music.
```

😂 **웃음 포인트 ①** — 검색어 세 개로 이 사람의 30분을 설명한다.
두 번째와 세 번째가 서로 모순된다는 게 개그다.

---

## 컷 4 — 카페 문 열림 ★러닝 개그 써먹는 컷

```
SUBJECT: @char_SEOYEON_v1 pushing open a cafe door and spotting him.
Slow motion on her entrance. Then a hard cut to @char_MINJUN_v1 at a
table, straightening his tie as he stands.
CAMERA: slow-motion medium-wide on her entrance with backlight, then a
fast cut to a medium of him. The slow motion ends abruptly on the cut.
LIGHTING: backlight through the glass door, cool desaturated grade.

VOICES:
[@voice_SEOYEON_v1 원문]
[홍자매 딜리버리 공통 문구]

DELIVERY: Two short interior thoughts, dropped casually, the second one
deflating the first. Light and quick, not dramatic.
ADDRESSING: Interior monologue. She does not speak aloud and does not
look at the camera.
SPEAKERS: One speaker only, in voice-over. No spoken dialogue in the
scene itself, no extra voices. Background patrons are unintelligible
murmur only.
PROCESSING: Voice-over is close-mic'd and dry, clearly separate from
the room.
DIALOGUE VOLUME: Voice-over at clear, natural speech volume, well above
the cafe ambience.

DIALOGUE (Korean, voice-over):
SEO-YEON (V.O.): "어. 잘생겼다."
SEO-YEON (V.O.): "…넥타이만 아니면."

SOUND: door chime, cafe ambience. On the cut to him, the ambience snaps
back to normal from the slow-motion muffle. No music, no score.
```

😂 **웃음 포인트 ②** — 로맨스 낚시를 **2초 만에** 스스로 무너뜨린다.
임성한 버전은 여기서 6배 슬로우로 계속 밀지만, 홍자매는 바로 깬다.

---

## 컷 5 — 침묵 ★정적을 대사로 감싸기

```
SUBJECT: @char_MINJUN_v1 and @char_SEOYEON_v1 seated across a cafe
table. He starts to speak, stops. She waits. He gives up. She nods.
Neither has said anything of substance.
CAMERA: static two-shot, with two quick reaction inserts — his mouth
opening and closing, her polite blink.
LIGHTING: flat cafe daylight, cool desaturated grade.

VOICES:
[@voice_MINJUN_v1 원문]
[@voice_SEOYEON_v1 원문]
[홍자매 딜리버리 공통 문구]

DELIVERY: Min-jun's opener dies in his mouth. Seo-yeon's replies are
small, patient and entirely empty. The pauses between lines are short
and awkward, never weighty.
ADDRESSING: Across the table. Neither speaks to the room or camera.
SPEAKERS: Two speakers only. Exact lines, no ad-libs, no extra voices.
DIALOGUE VOLUME: Dialogue at clear, natural speech volume, well above
the cafe room tone.

DIALOGUE (Korean):
MIN-JUN: "저기…"
SEO-YEON: "네."
MIN-JUN: "…아니에요."
(short pause)
SEO-YEON: "…네."

SOUND: cafe room tone, a distant espresso machine. No music.
```

⚠️ 임성한 버전과 **정확히 반대**다. 저쪽은 정적을 4초로 늘렸고,
여기서는 **정적을 대사로 감싸서** 짧게 만든다. 웃음의 종류가 다르다.

---

## 컷 6 — 재난 #1 · 커피 ★티키타카 정점

> `자막: 재난 #1`

```
SUBJECT: @char_MINJUN_v1 and @char_SEOYEON_v1 at the cafe table. An iced
americano tips and spills. Both start apologising over each other,
neither finishing a sentence. They end up mopping the table together;
their hands meet on the same napkin and both freeze for a beat.
CAMERA: quick handheld reframe on the spill, then fast cuts between
their faces on each line, then a static insert on the two hands stopped
on the napkin.
LIGHTING: flat cafe daylight, cool desaturated grade.

VOICES:
[@voice_MINJUN_v1 원문]
[@voice_SEOYEON_v1 원문]
[홍자매 딜리버리 공통 문구]

DELIVERY: Both talk over each other, each trying to take the blame,
lines colliding and cutting off. The rhythm accelerates, then stops dead
when their hands touch.
ADDRESSING: Across the table, to each other only.
SPEAKERS: Two speakers only. Exact lines, no ad-libs, no extra voices.
OVERLAP: The apology lines overlap at their edges, each starting before
the previous one finishes, but each line stays intelligible.
DIALOGUE VOLUME: Dialogue at clear, natural speech volume, well above
the cafe room tone.

DIALOGUE (Korean):
MIN-JUN & SEO-YEON (together): "아—"
MIN-JUN: "제가—"
SEO-YEON: "아니 제가—"
MIN-JUN: "제가 쏟았으니까—"
SEO-YEON: "제가 팔을 쳤으니까—"
(beat)
MIN-JUN: "…같이 할까요."
SEO-YEON: "…네."

SOUND: ice and liquid hitting the table, napkins pulled fast, then
silence on the hand contact — the ambience drops for one beat and
returns. No music, no score.
```

😂 **웃음 포인트 ③** — 서로 자기 탓이라고 우기는 티키타카.
그리고 **"같이 할까요"에서 처음으로 리듬이 맞는다.** 이 컷이 이 버전의 백미다.
임성한 버전(3단 줌인 + 징)과 완전히 다른 장면이 된다.

---

## 컷 7 — 재난 #2 · ERP ★V.O. 혼잣말

> `자막: 재난 #2 — 회사 얘기 20분째`

```
SUBJECT: @char_MINJUN_v1 explaining something with real enthusiasm.
@char_SEOYEON_v1 nodding at intervals with a fixed polite smile. On his
question, her smile freezes.
CAMERA: over-the-shoulder on him, cut to her face on each interior
thought, then a static close-up holding on her frozen smile.
LIGHTING: flat cafe daylight, cool desaturated grade.

VOICES:
[@voice_MINJUN_v1 원문]
[@voice_SEOYEON_v1 원문]
[홍자매 딜리버리 공통 문구]

DELIVERY: Min-jun is genuinely enthusiastic and picks up speed as he
goes — this is the one subject he is comfortable with. Seo-yeon's spoken
replies are hollow and automatic; her interior lines are fast, dry and
resigned. Her final interior line is flat, like a verdict.
ADDRESSING: Min-jun speaks across the table. Seo-yeon's spoken lines go
to him; her interior lines are voice-over and go to no one in the scene.
She does not look at the camera.
SPEAKERS: Two speakers only. Exact lines, no ad-libs, no extra voices.
PROCESSING: Seo-yeon's voice-over is close-mic'd and dry, clearly
separate from the room.
DIALOGUE VOLUME: Dialogue and voice-over both at clear, natural speech
volume, well above the cafe room tone.

DIALOGUE (Korean):
MIN-JUN: "그래서 저희 팀이 ERP를 도입했는데요—"
SEO-YEON (V.O.): "ERP가 뭐지."
MIN-JUN: "—그게 전사적 자원 관리라고—"
SEO-YEON (V.O.): "아, 물어보면 20분 더 하겠지."
SEO-YEON: "아… 네…"
MIN-JUN: "관심 있으세요?"
SEO-YEON: "…네?"
MIN-JUN (brightening): "더 설명드릴까요?"
SEO-YEON (V.O.): "망했다."

SOUND: cafe room tone, a cup set down off screen. No music.
```

😂 **웃음 포인트 ④** — 속마음과 겉말이 어긋나는 홍자매 특기.
`"관심 있으세요?"` 에서 민준이 밝아지는 게 잔인해서 웃긴다.

---

## 컷 8 — 재난 #3 · 헤어질 때

> `자막: 재난 #3 — 헤어질 때`

```
SUBJECT: @char_MINJUN_v1 and @char_SEOYEON_v1 outside the cafe. Both
start speaking at once, both stop, then each tries to yield to the
other, colliding again. Finally both bow — badly out of sync, one
starting as the other finishes.
CAMERA: static medium two-shot. Quick reaction cuts on the yielding
lines. Hold the wide on the mistimed bows.
LIGHTING: overcast daylight, cool desaturated grade.

VOICES:
[@voice_MINJUN_v1 원문]
[@voice_SEOYEON_v1 원문]
[홍자매 딜리버리 공통 문구]

DELIVERY: Both are flustered and over-polite, each deferring to the
other and neither getting anywhere.
OVERLAP: The first two lines are spoken simultaneously and collide,
neither cleanly audible. Both stop at the same moment. The deferring
lines that follow also start on top of each other.
ADDRESSING: To each other, not to the street or camera.
SPEAKERS: Two speakers only. Exact lines, no ad-libs, no extra voices.
DIALOGUE VOLUME: Dialogue at clear, natural speech volume.

DIALOGUE (Korean):
MIN-JUN: "다음에 또—"
SEO-YEON: "저 이만—"
(both stop)
MIN-JUN: "…먼저 하세요."
SEO-YEON: "…아니 먼저 하세요."
(short silence)
(both bow, mistimed)

SOUND: street ambience, a passing car. A short beat of room tone in the
silence. No music.
```

😂 **웃음 포인트 ⑤** — 양보가 또 겹친다. 겹침을 두 번 쓰는 게 홍자매식이다.

---

## 컷 9 — 신부 인터뷰 / V.O.

```
SUBJECT: @char_SEOYEON_v1 seated on a plain chair against a neutral
wall, present day, talking to an unseen interviewer. She snorts a small
laugh before answering, then pauses before the last line.
CAMERA: static medium close-up, eyeline slightly off-lens.
LIGHTING: soft even interview lighting, neutral grade — visibly
different from the cafe scenes.

VOICES:
[@voice_SEOYEON_v1 원문]
[홍자매 딜리버리 공통 문구]

DELIVERY: The first line is dry and amused, thrown away. Then a real
pause before the last line, which lands lighter and slightly puzzled —
it is a hinge, not a punchline.
ADDRESSING: To the unseen interviewer, never to the camera.
SPEAKERS: One speaker only. Exact lines, no ad-libs, no extra voices.
PROCESSING: Close-mic'd, completely dry, no room reverb.
DIALOGUE VOLUME: Dialogue at clear, natural speech volume.

DIALOGUE (Korean):
SEO-YEON: "심장이요? 아니 그게 뛰려면 뭐가 있어야 뛰죠."
SEO-YEON: "근데 그날 밤에요."
(pause)
SEO-YEON: "…심장이 아니라 폰이 뛰더라고요."

SOUND: quiet interior room tone only. No music.
```

⚠️ 마지막 줄이 **다음 컷으로 넘어가는 다리**다. 임성한 버전에는 없는 연결이다.
말장난 하나로 챕터를 넘긴다.

---

## 컷 10 — 밤 11시 47분 / 후크 ★러닝 개그 회수

```
SUBJECT: @char_SEOYEON_v1 lying in a dark bedroom lit only by her phone.
A messenger notification arrives. She reads. A third message arrives
below the first two. Her thumb stops over the screen.
CAMERA: close-up on the phone screen filling most of the frame. The
third message arrives while the shot holds. Then a small push to her
face.
LIGHTING: near darkness, only phone-screen light, cool grade.

ON-SCREEN TEXT (Korean, inside the messenger, arriving in order):
"오늘 제가 너무 긴장해서 실수가 많았어요."
"혹시… 딱 한 번만 더 기회 주실 수 있을까요?"
"아 그리고 넥타이는 다음엔 안 맬게요."
Timestamp visible: 11:47 PM

VOICES:
[@voice_SEOYEON_v1 원문]
[홍자매 딜리버리 공통 문구]

DELIVERY: A single interior line, quiet and caught off guard — half a
laugh, half genuine surprise. Not sentimental.
ADDRESSING: Interior monologue. She does not speak aloud.
SPEAKERS: One speaker only, in voice-over. No spoken dialogue in the
scene, no extra voices.
PROCESSING: Voice-over is close-mic'd and completely dry.
DIALOGUE VOLUME: Voice-over at clear, natural speech volume, well above
the room tone.

DIALOGUE (Korean, voice-over):
SEO-YEON (V.O.): "…아니 그걸 왜 알아."

SOUND: notification chimes — two, then a beat, then a third. Then
silence except faint room tone. No music, no score.
```

**암전.**
> `자막: 그래서, 다시 만났을까요?`

😂 **웃음 포인트 ⑥ — 러닝 개그 회수.**
컷 2에서 심고, 컷 3에서 키우고, 컷 4에서 써먹은 넥타이가 **여기서 되돌아온다.**
그리고 이 회수가 웃기기만 한 게 아니다 —
**"이 사람이 내 표정을 읽고 있었구나"** 를 관객이 먼저 알아챈다.
2화의 "듣고 있었구나"를 1화 마지막에 미리 심는 것이다.

⚠️ 이게 임성한 버전 대비 이 버전의 **가장 큰 구조적 이점**이다.
웃음과 복선을 같은 컷으로 처리한다.

---

## 4. 두 버전 비교

| 컷 | 임성한 | 홍자매 |
|---|---|---|
| 1 | 까치 울음 = 팔자 예언 | 말꼬리 잡기 ("진짜"가 네 번째) |
| 2 | 풀네임 호명 + 거울 앞 맹세 | 인사 연습 + **넥타이 심기** |
| 3 | "인생 끝나나요" | **모순되는 넥타이 검색 2개** |
| 4 | 6배 슬로우 운명적 조우 | 슬로우 → **2초 만에 자폭** |
| 5 | 과잉 클로즈업 + 정적 4초 | **정적을 대사로 감쌈** |
| 6 | 3단 줌인 + 프리즈 + 징 | **티키타카 → "같이 할까요"** |
| 7 | 정면 응시 독백 | **V.O. 혼잣말 + "더 설명드릴까요?"** |
| 8 | 빈 공간 푸시인, 정적 4초 | **양보가 또 겹침** |
| 9 | 격언 → 톤 붕괴 | **말장난으로 다음 컷 연결** |
| 10 | 거의 그대로 | **넥타이 회수 + 복선** |

**임성한 버전:** 웃음이 세다. 낙차가 크다. 대신 5분 내내 보면 피곤하다.
**홍자매 버전:** 웃음이 부드럽다. **복선과 구조가 있다.** 3화 임상춘으로 넘어가기 자연스럽다.

식전영상은 하객이 **처음 보는 사람들**이라는 걸 감안하면 홍자매 쪽이 안전하다.
임성한 톤은 취향을 탄다.

---

## 5. 3화에서 감정을 만드는 법 — 톤은 그대로

**딜리버리 문단을 바꾸지 않는다.** 홍자매 딜리버리 그대로 간다.
아래 한 줄만 3화 고백 씬에 덧붙인다.

```
DELIVERY (this scene only): The exchange runs as fast banter until
Min-jun's line lands a beat late and answers something she did not ask.
From that point Seo-yeon does not reply. The rhythm they have kept up
all episode simply stops, and neither of them restarts it.
```

카메라도 크게 바꾸지 않는다. **딱 하나만 바꾼다.**

| | 1~2화 | 3화 고백 씬 |
|---|---|---|
| 티키타카 구간 | 빠른 컷 전환 | **그대로 빠르게** |
| **리듬이 깨진 뒤** | — | **컷을 끊지 않고 한 테이크로 버틴다** |

리듬이 깨지기 전까지는 1화와 똑같이 찍는다. 그래야 깨지는 게 보인다.
깨진 다음부터 컷을 안 자르는 것, 그게 유일한 변화다.

⚠️ **3화에서 유일하게 금지되는 것: 서연의 V.O. 혼잣말.**
1~2화에서 서연은 속마음을 계속 흘린다. 3화에서는 한 번도 안 흘린다.
**말할 게 없어서가 아니라 정리가 안 돼서다.** 관객은 그 침묵을 알아챈다.
