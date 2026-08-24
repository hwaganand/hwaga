# 음악 — SUNO 프롬프트

> 《세 번째 만남》 · 5분 식전영상
> **결론: 한 곡으로 간다.** 컷마다 다른 곡을 붙이지 않는다.

---

## 0. 왜 한 곡인가

**① 5분은 곡 하나가 커버하는 길이다.**
컷마다 곡을 바꾸면 5분 동안 음악이 6~7번 갈린다. 하객은 그걸 "편집이 산만하다"로 읽는다.

**② 이 영상의 감정은 이미 사운드로 설계돼 있다.**
정적, 앰비언스 소거, 심장박동 — 전부 효과음으로 만들어놨다.
음악은 그 위에 **깔리는 바닥**이지, 감정을 만드는 주체가 아니다.

**③ 3화의 전환은 음악이 아니라 컬러와 리듬으로 한다.**
쿨톤 → 웜톤, 티키타카 → 침묵. 여기서 음악까지 바뀌면 과잉이다.

**④ 한 곡이면 편집이 훨씬 쉽다.**
컷 길이를 조정할 때 곡을 다시 붙일 필요가 없다.

---

## 1. 구조 — 한 곡, 네 구간

곡 하나를 4분 30초로 뽑아서 **구간별 볼륨만 조절**한다.

| 구간 | 시간 | 음악 상태 | 이유 |
|---|---|---|---|
| 콜드 오픈 | 0:00–0:35 | **없음 → 타이틀에서 인** | 앰비언스 컷아웃이 살아야 한다 |
| 1화 | 0:35–1:45 | 작게 (-18dB) | 대사와 정적이 주인공 |
| 1화 침묵 컷 | — | **완전히 뺀다** | 정적이 연출이다 |
| 2화 | 1:45–3:00 | 보통 (-12dB) | 감정이 올라가는 구간 |
| **3화 리듬 붕괴 전** | 3:00–3:40 | 보통 | 티키타카를 받쳐준다 |
| **3화 손 잡는 순간** | — | **완전히 뺀다** | 옷깃과 숨소리만 |
| 3화 손 이후 | 3:45–4:10 | 크게 (-6dB) | 유일하게 음악이 앞에 나오는 구간 |
| 최종화 | 4:10–4:50 | 크게 | 몽타주 |
| 쿠키 | 4:50–5:05 | 작게 | 웃기게 마무리 |

⚠️ **음악을 빼는 두 지점이 이 영상의 핵심이다.**
1화 침묵 컷, 3화 손 잡는 순간. 여기서 음악이 깔려 있으면 두 장면 다 죽는다.

⚠️ 콜드 오픈은 **타이틀이 뜰 때 음악이 처음 들어온다.**
그 전 35초는 카페 소음과 대사만. 0.5초 무음 뒤 타이틀과 함께 음악 시작.

---

## 2. SUNO 프롬프트 — 메인 (코미디 강조 확정본)

**Style of Music**
```
Playful acoustic comedy-romance instrumental, bouncy pizzicato strings
lead, warm nylon-string guitar, light staccato piano, soft brushed
snare with a gentle swing, plucked upright bass, a single clarinet
answering the melody. Charming and mischievous, with small comic
pauses between phrases. Unhurried mid tempo around 92 BPM. The
arrangement thins out to solo nylon guitar and sustained strings in the
final third, turning tender without changing key. Warm Korean romantic
comedy soundtrack feel. Leaves plenty of space between phrases.
No vocals.
```

**Exclude Styles**
```
vocals, lyrics, singing, whistling, ukulele, kazoo, slide whistle,
cartoon sound effects, slapstick percussion, circus music, polka,
handclaps, epic orchestral, cinematic trailer, EDM, synthwave,
aggressive drums, brass fanfare, sad piano ballad cliche
```

**Title:** `Three Times`
**Instrumental:** ON ✅ (반드시 켠다)
**Length:** 4분 30초 이상

---

## 2-1. 왜 이 편성인가 — 코미디와 3화를 동시에 잡는 법

**문제:** 코미디를 강조하면 3화 손 잡는 장면이 가벼워진다.
**해법:** 편성이 두꺼울 때 웃기고, **얇아지면 애틋해지는 악기**를 고른다.

| 악기 | 두꺼울 때 | 혼자 남을 때 | 판정 |
|---|---|---|---|
| **피치카토 스트링** | 통통 튀는 코믹 | 서정적 | ✅ |
| **나일론 기타** | 경쾌 | 따뜻하고 애틋 | ✅ |
| **클라리넷** | 익살스러움 | 쓸쓸함 | ✅ |
| 우쿨렐레 | 귀여움 | **계속 귀여움** | ❌ |
| 휘파람 | 유쾌 | **계속 유쾌** | ❌ |
| 핸드클랩 | 신남 | **감정 씬에서 재앙** | ❌ |

⚠️ **우쿨렐레·휘파람·핸드클랩은 Exclude에 넣었다.**
가장 "코미디처럼 들리는" 소리지만, 3화에서 볼륨을 줄여도 음색이 가벼워서 감정이 안 산다.

**추가한 코미디 장치**
- `bouncy pizzicato strings lead` — 1화 재난 3종 세트의 리듬을 받쳐준다
- `soft brushed snare with a gentle swing` — 스윙감이 티키타카와 맞는다
- `a single clarinet answering the melody` — 주고받는 구조가 대사의 핑퐁과 겹친다
- `small comic pauses between phrases` — SUNO가 음을 촘촘히 채우지 않게 한다
- `92 BPM` — 84에서 올렸다. 티키타카 속도에 붙는다

**3화를 지키는 장치**
- `thins out to solo nylon guitar and sustained strings in the final third`
- `turning tender without changing key` — 같은 곡인 게 들려야 한다. 조를 바꾸면 다른 곡이 된다

---

## 3. 구간별 운용 — 코미디 버전

| 구간 | 음악 | 비고 |
|---|---|---|
| 콜드 오픈 | 없음 → 타이틀에서 인 | 앰비언스 컷아웃이 살아야 한다 |
| **1화 재난 3종** | **-14dB, 평소보다 크게** | 코미디는 음악이 받쳐줘야 산다 |
| 1화 침묵 컷 | **완전히 뺀다** | 정적이 연출이다 |
| 2화 | -12dB | |
| 3화 티키타카 | -16dB | 대사가 주인공 |
| **3화 손** | **완전히 뺀다** | 옷깃과 숨소리만 |
| 3화 손 이후 | -6dB | 곡이 알아서 얇아진 구간 |
| 최종화 | -6dB | 몽타주 |
| 쿠키 | -12dB | 다시 통통 튀게 |

⚠️ **1화 재난 컷에서만 음악을 평소보다 크게 올린다.**
코미디는 음악이 리듬을 받쳐줄 때 훨씬 잘 먹힌다.
반대로 대사가 촘촘한 컷 7(ERP)에서는 다시 내린다.

## 4. 대안 세 가지 — 취향에 따라

메인이 안 맞으면 아래로 바꾼다. **구조는 그대로, 색깔만 다르다.**

### A. 코미디를 더 밀고 싶을 때

```
Playful acoustic comedy instrumental, bouncy pizzicato strings, muted
staccato guitar, woodblock and light brushed drums, walking upright
bass, clarinet and bassoon trading a mischievous melody. Bright and
comic, mid tempo around 100 BPM. Thins to solo guitar in the final
third. No vocals.
```

바순이 들어가면 더 익살스러워진다. **3화가 가벼워질 위험이 커지므로**,
이걸 쓸 거면 3화에서 음악을 아예 빼는 구간을 더 넓게 잡는다.

### A-2. 코미디를 뺀 원래 메인 (참고용)

```
Warm indie folk-pop instrumental, gentle fingerpicked acoustic guitar
lead, soft felt piano, light brushed drums entering halfway, subtle
upright bass, airy string pad in the final third. Unhurried mid tempo
around 84 BPM. Bittersweet but hopeful, understated, never triumphant.
Modern Korean drama soundtrack feel. Leaves plenty of space between
phrases. No vocals.
```

감정 쪽에 무게가 실린다. 코미디 강조 결정 전의 버전이다.

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
