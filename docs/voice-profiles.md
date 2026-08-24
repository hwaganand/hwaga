# 보이스 프로필 — 《세 번째 만남》

> 「보이스 프로필 바이블 v2」 공식 적용.
> **프로필은 에셋이다. 모든 씬 프롬프트에 원문을 통째로 복붙한다. 패러프레이즈 금지.**

---

## 0. 캐스팅 대비 설계

한 씬에 같이 나오는 인물끼리 최소 두 축 이상 벌어지게 잡았다.

| 캐릭터 | 음역대 | 속도 | 질감 | 억양 |
|---|---|---|---|---|
| 서연 (26) | 중고음 | 고른 페이스 | 가볍고 건조 | 서울 표준 |
| 민준 (27) | 중저음 바리톤 | 느림·머뭇 | 부드럽고 눌림 | 서울 표준 |
| 지원 (26, 친구) | 고음 | 아주 빠름 | 숨섞임·웃음 | 서울 구어 |
| 정 이모 (38, 주선자) | 중음 | 느긋함 | 따뜻·약한 콧소리 | **부산 사투리** |

**서연 ↔ 지원**이 가장 가까운 쌍이다(둘 다 여성·서울말) — 음역대(중고음↔고음), 속도(고른↔아주 빠름), 질감(건조↔숨섞임) 세 축으로 벌려놨다.
**주선자를 부산 사투리로 뺀 것**은 의도적이다. 1화에서 전화 목소리로만 등장하는데, 서울말 여성이 하나 더 늘면 서연과 섞인다.

---

## 1. 고정층 — 복붙용 프로필 원문

**이 블록은 토씨 하나 바꾸지 않는다.** 수정이 필요하면 v2로 버전을 올리고, 이후 모든 씬에 v2만 쓴다.

### `@voice_SEOYEON_v1` — 신부 서연 (이 영상의 화자)

```
SEO-YEON: A 26-year-old South Korean woman with a light, mid-high,
slightly dry voice. Even-paced, casual Seoul-standard Korean in a
talking-to-a-close-friend cadence — unpolished, with small breaths
and half-laughs falling between phrases.
Definitely a native South Korean speaker; never a foreign, dubbed or
AI-narrator accent; never a broadcast-narrator, audiobook or
voice-actress reading tone; no regional dialect.
```

⚠️ 이 캐릭터의 최대 위험은 **낭독체**다. 영상 전체 내레이션을 맡기 때문에 모델이 자꾸 내레이터 톤으로 끌고 간다. 그래서 네거티브를 3중으로 걸었다.

### `@voice_MINJUN_v1` — 신랑 민준

```
MIN-JUN: A 27-year-old South Korean man with a soft, mid-low baritone
that sits slightly back in the throat. Slow, halting Seoul-standard
Korean with frequent pauses and unfinished sentence endings, in an
awkward, unpracticed cadence.
Definitely a native South Korean speaker; never a foreign, dubbed or
AI-narrator accent; never a smooth, confident or charismatic delivery;
no regional dialect.
```

⚠️ `never a smooth, confident or charismatic delivery` 가 이 캐릭터의 생명줄이다.
모델은 중저음 남성에게 매력적인 저음을 주려는 편향이 있다. **목소리가 멋있어지면 캐릭터가 죽는다.**

### `@voice_JIWON_v1` — 친구 지원

```
JI-WON: A 26-year-old South Korean woman with a bright, high, slightly
breathy voice. Fast, bouncy casual Seoul Korean with rising sentence-end
intonation and quick, giggly bursts.
Definitely a native South Korean speaker; never a foreign, dubbed or
AI-narrator accent; never a calm or measured delivery; no regional dialect.
```

### `@voice_JUNGIMO_v1` — 주선자 정 이모

```
JUNG-IMO: A 38-year-old South Korean woman with a warm, mid-range,
slightly nasal voice. Unhurried Busan (Gyeongsang) dialect with a
coaxing, over-confident salesperson cadence.
The dialect stays identical in every line; never drifts into standard
Seoul Korean; never a foreign, dubbed or AI-narrator accent.
```

---

## 2. 변동층 — 씬마다 새로 쓰는 5가지

고정층에는 **감정을 절대 넣지 않는다.** 아래는 씬 프롬프트 쪽에 매번 새로 쓴다.

1. **이 씬의 감정 딜리버리**
2. **물리 동작과 목소리의 관계** (걸으며 / 뛰며 / 울먹이며)
3. **발화 대상 잠금** (누구에게 하는 말인가)
4. **발화자 수 + 비언어 사운드 규격**
5. **대사 볼륨** — 조용한 씬일수록 반드시 명시

---

## 3. 씬별 VOICES 블록 — 그대로 복붙

### 콜드 오픈 · 카페

```
VOICES:
[@voice_SEOYEON_v1 원문 붙여넣기]
[@voice_JIWON_v1 원문 붙여넣기]

DELIVERY: Seo-yeon's delivery is heated and venting, riding fast on
the front of the beat. She is complaining to a friend, not performing
for an audience. Ji-won's single line is a short, surprised prompt.
PHYSICALITY: Seo-yeon gestures widely while speaking; the movement adds
breath breaks but never breaks the words.
ADDRESSING: Every line is addressed directly to the friend across the
table. Neither woman speaks to the camera.
SPEAKERS: Two speakers only. Exact lines, no ad-libs, no extra voices.
Background cafe patrons are unintelligible murmur only.
DIALOGUE VOLUME: Dialogue at clear, natural speech volume, well above
the cafe room tone.
```

### 1화 S#1-1 · 신부의 집 (전화)

```
VOICES:
[@voice_JUNGIMO_v1 원문 붙여넣기]
[@voice_SEOYEON_v1 원문 붙여넣기]

DELIVERY: Jung-imo is coaxing and over-certain, selling hard.
Seo-yeon's reply is flat and unconvinced, thrown away.
ADDRESSING: A phone conversation. Neither speaks to the room.
SPEAKERS: Two speakers only. Exact lines, no ad-libs.
PROCESSING: Jung-imo's voice is band-limited phone-line audio.
Seo-yeon's voice is unprocessed and close-mic'd.
DIALOGUE VOLUME: Both voices at clear, natural speech volume.
```

### 1화 S#1-3 · 카페 첫 대면

```
VOICES:
[@voice_MINJUN_v1 원문 붙여넣기]
[@voice_SEOYEON_v1 원문 붙여넣기]

DELIVERY: Min-jun's delivery is stiff with nerves — he starts sentences
he cannot finish and trails off. He is trying to sound composed and
failing. Seo-yeon's replies are minimal, polite and hollow; she is
running out of interest, not being rude.
PHYSICALITY: Both are seated. Min-jun's tension compresses his voice
without causing stuttering; the words stay intelligible.
ADDRESSING: Every line is addressed across the table to the other
person. Neither speaks to the room or the camera.
SPEAKERS: Two speakers only. Exact lines, no ad-libs, no extra voices.
The silences contain no dialogue at all — only room tone.
DIALOGUE VOLUME: Dialogue at clear, natural speech volume, well above
the cafe room tone.
```

**재난 #3(말 겹침)은 별도 지시:**
```
OVERLAP: The two lines are spoken simultaneously and collide. Neither
line is cleanly audible over the other. Both stop abruptly at the same
moment, followed by silence.
```

### 1화 S#1-4 · 신부 내레이션

```
VOICES:
[@voice_SEOYEON_v1 원문 붙여넣기]

DELIVERY: Dry and faintly amused, as if she still cannot believe it.
A half-laugh sits under the line. She is recalling, not performing.
ADDRESSING: Spoken to an unseen interviewer, not to the camera and not
to another character in the scene.
SPEAKERS: One speaker only. Exact line, no ad-libs, no extra voices.
PROCESSING: Close-mic'd voice-over, completely dry, no room reverb.
DIALOGUE VOLUME: Dialogue at clear, natural speech volume, well above
the ambience.
```

### 3화 S#3-4 · 신랑 고백 ★최고 난도

```
VOICES:
[@voice_MINJUN_v1 원문 붙여넣기]

DELIVERY: For this scene only, the hesitation drops away. His delivery
is plain, level and unadorned — not eloquent, not romantic, simply
certain. He is not performing affection; he is stating a fact.
The pauses remain, but they are calm rather than nervous.
ADDRESSING: Every word is addressed directly to the woman in front of
him. He does not speak to the street, the camera, or himself.
SPEAKERS: One speaker only for these lines. Exact lines, no ad-libs.
DIALOGUE VOLUME: Dialogue at clear, natural speech volume, well above
the quiet night ambience.
```

⚠️ 이 씬은 **고정층의 `halting`과 변동층의 `hesitation drops away`가 정면으로 부딪힌다.** 의도된 것이다.
1~2화 내내 더듬던 사람이 여기서만 안 더듬는 것 — 그 차이가 들려야 3화가 산다.
프로필 자체는 절대 수정하지 말 것. 딜리버리 문장으로만 덮는다.

### 3화 S#3-3 · 신부 내레이션 ★영상의 심장

```
VOICES:
[@voice_SEOYEON_v1 원문 붙여넣기]

DELIVERY: Quiet and held back. She is suppressing tears, not crying —
the voice thickens slightly and slows, but never breaks into sobbing.
No warmth is added; the restraint is what carries the emotion.
ADDRESSING: Spoken to an unseen interviewer.
SPEAKERS: One speaker only. Exact lines, no ad-libs.
PHYSICALITY: A held breath before the second sentence.
PROCESSING: Close-mic'd voice-over, completely dry.
DIALOGUE VOLUME: Dialogue at clear, natural speech volume, well above
the ambience.
```

⚠️ **울면 실패다. 우는 걸 참는 소리여야 한다.** 감정을 얹지 말고 빼는 방향으로 지시할 것.

---

## 4. 출고 전 체크리스트

| | 확인 |
|---|---|
| F1 | 프로필 **원문**을 VOICES 섹션에 통째로 넣었는가 (태그만 참조하지 않았는가) |
| F2 | 각 프로필 끝에 `never` 문장이 붙어 있는가 |
| F3 | 프로필에 감정어가 안 들어갔는가 (감정은 DELIVERY에만) |
| F4 | 같은 씬 화자들이 최소 두 축 이상 벌어져 있는가 |
| F5 | 발화자 수를 명시했는가. 말 안 하는 인물의 소리를 규격화했는가 |
| F6 | 프로필 문구가 지난 씬과 **토씨까지 동일한가** |
| + | 대사 볼륨을 명시했는가 (조용한 씬일수록 필수) |

---

## 5. 사람이 직접 녹음할 경우

AI 생성이 아니라 신랑신부가 직접 목소리를 녹음한다면 위 프로필은 **연기 지시서**로 쓴다.

- **V.O.는 한 번에 다 읽지 말고 구간별로 따로 녹음한다.** 감정이 이어지지 않는다.
- 이불 뒤집어쓰고 녹음하면 울림이 잡힌다. V.O.는 이걸로 충분하다.
- 휴대폰도 근접이면 쓸 만하다. 멀어지는 순간 폰 티가 난다.
- 전화 필터는 후반에서 EQ로 만든다. **실제로 전화로 녹음하지 말 것** (품질이 못 쓴다).
- 서연 역에게는 **"읽지 말고 친구한테 얘기하듯"** 이 한 마디가 제일 잘 먹힌다.
- 민준 역에게는 **"잘하려고 하지 마세요"** 라고 해야 한다. 잘 읽으면 캐릭터가 죽는다.

---

## 6. 3층 거리 규칙

| 층 | 마이크 거리 | 처리 |
|---|---|---|
| 현장 대사 | 보통 | 공간 반사음 있음 |
| 인터뷰 컷 | 근접 | 건조, 룸톤만 |
| V.O. 내레이션 | 가장 근접 | 완전 건조 |

이 **거리 차이가 영상의 구조를 소리로 설명한다.** 섞이면 하객이 지금 어느 시점인지 헷갈린다.
