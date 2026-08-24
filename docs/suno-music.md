# 음악 — SUNO 프롬프트

> 《세 번째 만남》 · 5분 식전영상
> **결론: 한 곡으로 간다.** 컷마다 다른 곡을 붙이지 않는다.

---

## 0. 구조 — 한 멜로디, 두 편곡 ★확정

**한 곡으로 통일하려던 초안은 폐기됐다.** 이유가 명확하다.

104 BPM 통통 튀는 곡은 **볼륨을 내려도 템포와 질감이 남는다.**
3화 손 잡는 장면에 그 곡이 얇아진 채로 깔려 있어도, 통통 튀던 잔상이 지워지지 않는다.

그렇다고 다른 두 곡을 쓰면 다른 영화처럼 들린다.

**해법: 같은 멜로디를 두 가지로 편곡한다.**

| | 1화가 원하는 것 | 3화가 원하는 것 |
|---|---|---|
| 템포 | 빠르게 | 느리게 |
| 타악 | 있어야 함 | 없어야 함 |
| 편성 | 두껍게 | 얇게 |
| 멜로디 | **같음** | **같음** |

드라마 OST가 실제로 쓰는 방식이다. 같은 테마가 감정에 따라 옷을 갈아입는다.

⚠️ **하객이 3화에서 그 멜로디를 알아보는 것이 이 설계의 전부다.**
"아까 그 웃긴 노래인데 지금은 왜 이러지" — 그 순간이 감정이다.
두 개의 다른 곡으로는 절대 못 만드는 효과다.

---

## 1. 프롬프트 A — 메인 (콜드오픈 ~ 2화, 최종화, 쿠키)

**Style of Music**
```
Bouncy acoustic romantic-comedy instrumental, walking upright bass
driving the groove, staccato pizzicato strings, muted rhythmic nylon
guitar chops on the offbeat, bright marimba doubling the melody,
woodblock and tambourine, light brushed snare with a springy shuffle,
a cheeky clarinet answering every phrase. Playful stop-time hits and
small comic pauses. Lively mid-up tempo around 104 BPM, skipping and
buoyant. A clear, simple, singable melody that repeats. Warm Korean
romantic comedy soundtrack. No vocals.
```

**Exclude Styles**
```
vocals, lyrics, singing, whistling, ukulele, kazoo, slide whistle,
cartoon sound effects, slapstick percussion, circus music, polka,
big band swing, epic orchestral, cinematic trailer, EDM, synthwave,
aggressive drums, brass fanfare, sad piano ballad cliche
```

**Instrumental:** ON ✅ · **Title:** `Three Times`

⚠️ `A clear, simple, singable melody that repeats` 가 핵심이다.
**멜로디가 단순해야 3화에서 알아본다.** 복잡하면 리프라이즈가 안 먹힌다.

### 통통 튀는 느낌은 어디서 오는가

| 요소 | 역할 |
|---|---|
| **워킹 업라이트 베이스** | 베이스가 걸어다니면 곡이 앞으로 굴러간다. 가장 큰 요인 |
| **엇박 기타 커팅** | 통통 튀는 느낌의 절반이 여기서 나온다 |
| 우드블록·탬버린 | 경쾌한 질감 |
| 마림바 | 멜로디를 두 배로 밝게 |
| stop-time hits | 다 같이 멈췄다 들어오는 장치. 1화 재난 컷과 맞는다 |
| 104 BPM | 티키타카 속도 |

---

## 2. 프롬프트 B — 리프라이즈 (3화)

**A를 먼저 확정한 뒤, SUNO의 Cover 기능으로 만든다.** 그래야 멜로디가 같다.

```
Same melody, completely different arrangement. Tender acoustic ballad
instrumental, solo nylon-string guitar carrying the theme, warm
sustained strings entering underneath, a single soft piano note at
phrase ends. No percussion at all, no bass groove. Slow and patient
around 68 BPM. Intimate, restrained, quietly emotional. Long silences
between phrases. Same key as the original. No vocals.
```

핵심은 `No percussion at all, no bass groove` 다.
**통통 튀던 요소를 전부 제거하는 것**이 이 편곡의 전부다.

---

## 3. 구간별 운용

| 구간 | 곡 | 볼륨 |
|---|---|---|
| 콜드 오픈 | 없음 → 타이틀에서 **A** 인 | — |
| **1화 재난 3종** | **A** | **-14dB (크게)** |
| **1화 침묵 컷** | **없음** | **0** |
| 1화 컷 7 (ERP) | A | -20dB (대사가 촘촘하다) |
| 1화 컷 10 (후크) | A | -20dB, 알림음 뒤 0으로 |
| 2화 | A | -12dB |
| 2화 비 씬 | A | -14dB |
| 3화 티키타카 | **B** | -18dB |
| **3화 손** | **없음** | **0** |
| 3화 손 이후 | B | -6dB |
| **최종화 몽타주** | **A 복귀** | -6dB |
| 쿠키 | A | -12dB |

⚠️ **최종화에서 A로 돌아오는 것이 중요하다.**
통통 튀는 곡이 다시 나오면서 "웃으며 끝내기"가 완성된다. B로 끝내면 너무 감상적이다.

⚠️ **1화 재난 컷에서만 음악을 평소보다 크게 올린다.**
코미디는 음악이 리듬을 받쳐줄 때 훨씬 잘 먹힌다.

---

## 3-1. SUNO 작업 순서

1. **A를 5개 이상 뽑는다.** 멜로디가 단순하고 기억에 남는 것을 고른다
2. 확정된 A에서 **Cover** 실행 → B 프롬프트 입력
3. B의 멜로디가 A와 같은지 확인. 다르면 다시 Cover
4. Cover가 계속 안 맞으면 → **B를 별도 생성하되 나일론 기타를 반드시 넣는다.**
   악기가 겹치면 형제곡으로 들린다

**Cover가 이 방식의 관건이다.** 안 되면 4번 폴백으로 가도 충분히 통한다.

### A를 고를 때 기준

- 도입 15초가 밋밋할 것 (콜드 오픈 뒤에 붙일 자리)
- 멜로디를 듣고 따라 흥얼거릴 수 있을 것
- 통통 튀는 곡일수록 SUNO 편차가 크다. **촌스럽게 나온 건 버린다**

---

## 3-2. 더 세게 밀고 싶으면 (A 대체안)

```
Peppy acoustic sitcom instrumental, fast walking upright bass, snappy
pizzicato strings, marimba and glockenspiel trading a mischievous
melody, woodblock, tambourine and finger snaps, tight brushed shuffle,
clarinet and bassoon bickering in call and response. Constant forward
motion, comic stop-time breaks. Bright and busy, around 116 BPM.
A clear, simple, singable melody that repeats. No vocals.
```

116 BPM에 바순까지 들어가면 거의 시트콤 톤이다.
**하객 반응은 이쪽이 더 좋을 수 있지만**, 3화와의 낙차가 너무 커진다.
이걸 쓸 거면 3화에서 음악을 아예 빼는 구간을 더 넓게 잡는다.

## 4. 완전히 다른 방향 (A가 안 맞을 때)

메인이 안 맞으면 아래로 바꾼다. **구조는 그대로, 색깔만 다르다.**

### B. 더 담백하고 조용한 톤 (감정 강조)

```
Sparse solo piano instrumental with soft room tone, single sustained
notes with long decay, occasional low cello. Very slow, around 68 BPM,
patient and unhurried. Intimate and restrained, melancholic but warm.
Long silences between phrases. No vocals.
```

3화가 강해진다. 다만 **1화 코미디가 무거워진다.**

### C. 한국 드라마 OST 정통

```
Korean drama OST instrumental, warm nylon-string guitar and soft piano,
gentle strings entering in the second half, light shaker. Mid tempo
around 80 BPM. Sentimental but restrained, nostalgic, hopeful.
No vocals.
```

가장 안전하다. **하객이 익숙해하는 소리**다. 튀지 않는 게 장점이자 단점.

---

## 5. 뽑을 때 요령

- **한 번에 4~5개 생성하고 고른다.** SUNO는 같은 프롬프트로도 결과 편차가 크다.
- **Instrumental 토글을 반드시 켠다.** 안 켜면 흥얼거림이 섞여 나온다.
- 4분 30초가 한 번에 안 나오면 **Extend**로 늘린다. 처음부터 길게 요구하면 구조가 무너진다.
- 도입 20초가 밋밋한 곡을 고른다. **콜드 오픈 뒤에 붙일 자리**가 필요하다.
- 마음에 드는 곡이 나오면 **같은 곡으로 Extend해서 5분을 채운다.** 다른 곡을 이어붙이지 않는다.

## 6. 편집에서 할 일

1. 곡을 타임라인에 **한 줄로 깐다.** 자르지 않는다.
2. 위 구간표대로 **볼륨 오토메이션만** 그린다.
3. 1화 침묵 컷과 3화 손 컷에서 **완전히 0으로 내린다.** 페이드는 0.5초.
4. 대사가 있는 모든 구간에서 음악을 **-18dB 이하**로 유지한다.
5. 최종화 몽타주에서만 음악이 앞에 나온다.

⚠️ **음악은 대사를 이기면 안 된다.** 이 영상은 대사와 정적으로 만들어져 있다.
음악은 그 사이를 메우는 것이지, 감정을 대신 만들어주는 게 아니다.

## 7. 저작권

SUNO 생성곡은 상업적 이용이 가능한 플랜이 따로 있다.
**식장 상영만 할 거면 문제없지만, 유튜브·인스타 업로드 계획이 있다면**
본인 플랜의 상업 이용 조건을 확인할 것.
