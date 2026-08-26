# HANDOFF — 《또 봐요?》 제작 인수인계

> AI 숏드라마 4부작. Claude Code / Codex 어느 쪽에서든 이 문서 하나로 이어서 작업할 수 있게 정리했다.
> **중요 프롬프트는 요약하지 않고 원문 그대로 넣었다. 복붙해서 쓰면 된다.**
> 최종 갱신: 2026-08-26 · 브랜치 `claude/wedding-video-romcom-scenario-nyp59d`

---

## 목차

| | | |
|---|---|---|
| [1. 작품 개요](#1-작품-개요) | [6. 보이스 프로필 원문](#6-보이스-프로필--원문-복붙용-) | [11. 다음에 해야 할 작업](#11-다음에-해야-할-작업) |
| [2. 절대 규칙](#2-절대-규칙-claudemd) | [7. 이미지 프롬프트 원문](#7-이미지-프롬프트--원문-복붙용-) | [12. 파일 지도](#12-파일-지도) |
| [3. 전체 시나리오](#3-전체-시나리오) | [8. 영상 프롬프트 원문](#8-영상-프롬프트--원문-복붙용-) | [13. 새 세션 시작 절차](#13-새-세션에서-시작할-때) |
| [4. 캐릭터 설정](#4-캐릭터-설정) | [9. 파이프라인 실전 지식](#9-파이프라인-실전-지식--겪은-함정들-) | |
| [5. 레퍼런스 ID 표](#5-확정된-에셋--레퍼런스-id-표-) | [10. 미결정 사항](#10-아직-결정하지-않은-사항-) | |

**바쁘면 여기만** — 2장(규칙) → 5장(ID 표) → 9장(함정) → 11장(다음 작업)

---

# 1. 작품 개요

| | |
|---|---|
| 제목 | **《또 봐요?》** (원제 《세 번째 만남》) |
| 형식 | AI 생성 숏드라마 4부작 |
| 한 줄 | **소개팅은 최악이었는데, 세 번째 만나고 결혼했다.** |
| 톤 | 홍자매 (전 화 통일) |
| 러닝타임 | 1화 ~90초 / **2화 126초 (16컷)** / 3화 ~70초 / 최종화 미정 |
| 배포 | 쓰레드(Threads) 중심. 원래 결혼식 식전영상으로 출발 |
| 상태 | **1화 생성 완료 · 2화 대본 확정, 컷 생성 대기 · 3화 대본 있음 · 최종화 미작성** |

## 1-1. 이 작품의 유일한 장치 ★

**티키타카를 하다가 한 사람이 안 받아친다.**

톤을 바꿔서 감정을 만들지 않는다. 감정 씬도 홍자매로 쓴다.
1~2화 내내 두 사람은 말을 주고받고, **3화에서 서연이 처음으로 받아치지 못한다.**
웃다가 조용해지는 게 아니라 **웃기려던 사람이 실패하는 순간**이 감정이다.

| | 임상춘 방식 | **홍자매 방식 (채택)** |
|---|---|---|
| 감정 만드는 법 | 담백한 대사로 정면 돌파 | **티키타카 중 한 사람이 안 받아침** |
| 전환 신호 | 톤 자체가 바뀜 | **리듬이 깨짐** |
| 관객이 느끼는 것 | "갑자기 진지해졌다" | **"어? 왜 대답을 못 하지"** |

## 1-2. 화자 구조가 뼈대다 ★★

| | 1~2화 | 3화 |
|---|---|---|
| 서연 | **속으로 말한다** (V.O. 계속) | **침묵한다** (V.O. 0회) |
| 민준 | **소리 내서 흘린다** (V.O. 0회) | **속으로 말한다** (V.O. 1회) |

민준의 V.O.는 **영상 전체에서 딱 한 번**, 3화 컷 6 손이 닿는 순간에만 나온다.

```
민준 (V.O.): …어떡하지.
```

⚠️ **이 한 줄 외에 민준의 V.O.를 어디에도 넣지 않는다.** 두 번 쓰면 그냥 내레이션이 된다.

---

# 2. 절대 규칙 (CLAUDE.md)

## ① 목소리는 반드시 서술한다 ★필수
대사가 있는 **모든 컷**에 목소리 지정을 붙인다. 예외 없다.
누가 말하는지만 쓰지 말고 **어떤 목소리로** 말하는지를 매번 적는다.
V.O.·인터뷰·현장 대사·전화 전부 해당. 표기는 대사 블록 바로 위에 `보이스:` 한 줄.

## ② BGM은 넣지 않는다 ★필수
음악은 사용자가 직접 얹는다. 시나리오에는 **현장음·효과음·무음**만 설계한다.
"음악 최고조", "업템포 비트에 맞춰" 같은 음악 의존 연출 금지.

## ③ 이미지 생성은 한 번에 1장씩
요청 없이 변형 여러 장 뽑지 않는다. 캐릭터 레퍼런스는 확정된 기준 이미지를 첨부해서 생성한다.

## ④ 생성 전 프롬프트 검사 ★필수
이미지·영상 생성 전에 **프롬프트 전문을 사용자에게 보여주고 승인을 받는다.**
(사용자가 "승인 안 받아도 돼"라고 명시적으로 면제한 경우에만 예외)

## ⑤ 한글 대사는 이스케이프 없이 직접 입력 ★
생성 툴에 넘길 때 한글을 `\uXXXX` 로 쓰지 않는다. 한글을 그대로 입력하고,
제출 후 **에코된 프롬프트에서 대사를 눈으로 확인한다.**
> 실제 사고 기록: `리`(리)를 쓰며 `맬`을 의도, `거`(거)를 쓰며 `끼`를 의도,
> `므`(므)를 쓰며 `믄`을 의도 — 영상 3개가 틀린 대사로 생성됐다.

## ⑥ 작가 톤 — 홍자매로 통일
전 화 홍자매. 작가를 섞지 않는다. 감정 씬도 톤을 바꾸지 않는다.
> ⚠️ **공개물에 특정 작가 이름을 쓰지 않는다.** "AI가 특정 작가 스타일을 흉내냈다"는
> 프레임이 작품 자체를 덮어버린다. 내부 문서에서만 톤 레퍼런스로 쓴다.

---

# 3. 전체 시나리오

## 3-1. 제1화 — 최악의 소개팅 (10컷 · ~90초) ✅ 생성 완료

카페. 민준이 **풀정장에 넥타이**를 매고 나와 ERP 얘기를 신나서 한다.
서연은 정중한 미소로 버틴다. 아이스 아메리카노가 쏟아지고 서로 자기 탓이라 우긴다.
헤어질 때 민준 — `"넥타이는 다음엔 안 맬게요."`
그날 밤 서연이 어두운 방에서 폰을 본다.

> **자막: 그래서, 다시 만났을까요?**

핵심 대사 (컷 9 인터뷰):
```
서연: "심장이요? 아니 그게 뛰려면 뭐가 있어야 뛰죠."
서연: "근데 그날 밤에요."
(pause)
서연: "…심장이 아니라 폰이 뛰더라고요."
```

## 3-2. 제2화 — 남친룩 (16컷 · 126초) ✅ 대본 확정, 컷 생성 대기

> **전문은 `docs/episode2-hong.md` 에 있다.** 여기엔 뼈대와 핵심 대사만 옮긴다.

### 구조
| 구간 | 컷 | 역할 |
|---|---|---|
| 교차편집 (옷가게 ↔ 서연 방) | 0~7 (63초) | **순수 코미디** |
| 이탈리안 식당 | 8~10 (37초) | **뒤집기 + 역공** |
| 횡단보도 | 11 (8초) | **무대사 감정** |
| 인터뷰 | 12~13 (16초) | **펀치라인 → 인정** |
| 세 번째 약속 | 14 (8초) | **후크** |

### 대칭이 이 화의 뼈대다
| | 민준 | 서연 |
|---|---|---|
| 도와주는 사람 | 준영 (혼자) | 지원 (혼자) |
| 태도 | 순순히 따름 | **계속 부정** |
| 결과 | **옷을 바꿈** | **세 벌 거쳐 처음 옷으로, 립만 세 번** |

### 컷별 길이 ★ 전부 10초 이하

**길이 = 대사 음절 ÷ 5 + 리액션·정적.** 한국어 자연 대화는 초당 약 5음절.

| 컷 | 내용 | 음절 | 길이 |
|---|---|---|---|
| 0 | 답장 "네." | 21 | 6초 |
| 1 | 교차 시작 | 18 | 7초 |
| 2 | **등산복 등장** ★ | 25 | 9초 |
| 3 | 서연 방 · 원피스 | 34 | 10초 |
| 4 | 니트 · 여성 코너 | 25 | 7초 |
| 5 | **준영의 데이터** | 34 | 10초 |
| 6 | **서연 방 · 립** ★ | 17 | 9초 |
| 7 | 각자 나선다 · 매치컷 | 6 | 5초 |
| 8 | 식당 · 물 두 번 | 18 | 8초 |
| 9A | **오일 파스타 (1)** ★★ | 47 | 10초 |
| 9B | **오일 파스타 (2)** ★★ | 36 | 10초 |
| 10 | **영화 · 역공** ★ | 32 | 9초 |
| 11 | **횡단보도 · 자리** ★ | **0** | 8초 |
| 12 | 인터뷰 · 개별 하드컷 | 32 | 8초 |
| 13 | **인터뷰 · 인정** ★★ | 24 | 8초 |
| 14 | 세 번째 약속 | 0 | 8초 |

⚠️⚠️ **10초를 넘는 컷은 만들지 않는다.** 생성 조건이 `seedance_2_5` 10초다.
컷 9가 원래 15초로 적혀 있었는데 실측 24초였다. **9A / 9B로 쪼갰다.**

### 핵심 대사

**컷 0** — 서연 V.O.: `그래서… 한 번 더 만나기로 했어요.` / `딱 한 번만요.`

**컷 2 (등산복)** — 형광 주황 바람막이 + 정장 바지 + 갈색 구두
```
준영: (곁눈질) …뭐야 저게.
민준: 왜.
준영: 아니 그거 뭐냐고.
민준: 아빠 건데. 따뜻해.
준영: (실소) …벗어.
```

**컷 3 (원피스)**
```
지원: 이거 입어.
서연: 미쳤어?
지원: 왜.
서연: 예의상 가는 건데.
지원: …예의상인데 왜 세 벌째 갈아입어?
서연: ……
```

**컷 4 (여자 니트)**
```
민준: 이거 어때. 니트.
준영: 그거 여자 옷이야.
민준: …어?
준영: 여성 코너잖아.
민준: …아.
```

**컷 5 (준영이 말이 막힌다)**
```
준영: 이거 입어.
민준: 이건 왜.
준영: 전 여친이 이거 좋아했어.
민준: ……
준영: 왜.
민준: 아니… 그걸 왜 아직 알아.
```
😂 **받아치던 사람이 안 받아친다 — 이번엔 준영이다.**
2화에서 이 장치를 **웃음으로** 써두면 3화에서 서연이 같은 자리에 섰을 때
관객이 그 정적을 이미 안다.

**컷 6 (립)** — 세 벌을 거쳐 결국 처음 입었던 옷. 립을 세 번 바른다.
```
지원: …
서연: 왜.
지원: 아무 말도 안 했는데.
서연: 눈으로 했잖아.
```

**컷 7 (매치컷)** — 준영이 민준의 등을 민다 → **손이 등에 닿는 프레임에서 하드컷** →
지원이 서연의 등을 똑같이 민다. **같은 사이즈·같은 앵글·같은 이동 방향(오른쪽).**
```
준영: 가.
(하드컷)
지원: 잘 갔다 와~
```

**컷 8 (물 두 번)** — 서버가 빈 잔에 물을 따른다. 물병을 들어 보이자 민준이 고개를 젓는다 —
두 번째다. 서연이 들어오고 민준이 일어설 때 **잔은 또 비어 있다.**
```
서연: 오래 기다리셨어요?
민준: 아니요. 방금 왔어요.
```
⚠️ **거짓말을 화면이 먼저 반박한다.** 대사로 설명하지 않는다.

**컷 9A**
```
민준: 어떤 거 드실래요?
서연: 오일 파스타로.
민준: 빨리 정하시네요.
서연: 2주 전에 와봤어요.
민준: 혼자요?
서연: 그럴 리가요. 소개팅이었어요.
(민준이 굳는다 — 대사 없음)
```

**컷 9B ★★ 이 화의 핵심**
```
(적막 2초 — 포크 소리만)
민준: 아, 매주 하시나 보다.
서연: 어쩌다 이번에 몰렸어요.
(적막 2초)
서연: 근데 그 사람은 별로였어요.
(민준이 고개를 든다)
서연 (V.O.): …내가 뭘 한 거지.
```
⚠️ **"아, 매주 하시나 보다"를 놀리는 톤으로 읽으면 안 된다.**
진심으로 침묵이 무서워서 아무 말이나 꺼낸 것이다. 비꼬면 그냥 무례한 사람이 된다.
⚠️ 서연의 마지막 줄은 **자기도 모르게 나온 말**이다. 그래서 바로 V.O.로 당황한다.

**컷 10 (역공)**
```
서연: 이 영화 봤어요?
민준: 네.
서연: …또 혼자요?
민준: 아니요.
서연: …네?
민준: 지난달에 소개받은 분이랑요.
(서연이 멈춘다)
서연: ……
```
⚠️ **민준은 「소개팅」이라는 단어를 쓰지 않는다.** 서연이 쓴 말을 되받으면 반격처럼 들린다.
`소개받은 분` 이라고 무심하게 말해야 **악의가 없다는 게** 산다.

**컷 11 (횡단보도) — 무대사 ★**
```
횡단보도 앞에서 신호를 기다린다. 신호가 바뀌고 걷기 시작하는 순간,
민준이 반 발 앞서 나가며 자연스럽게 서연의 차도 쪽으로 자리를 옮긴다.
말도 눈짓도 없다. 건너편에서 헤어진다.
서연이 몇 걸음 가다 돌아본다. 민준은 혼자인데도 여전히 차도 가장자리로 걷고 있다.
서연의 눈이 잠깐 달라진다. 그게 전부다. 다시 돌아서 걷는다.

보이스: 없음
SPEAKERS: Zero speakers. 대사 없음, V.O. 없음.
```
⚠️ **로맨틱하게 강조하지 않는다.** 슬로우·조명 강조·클로즈업 확대 전부 금지.
**민준은 끝까지 자기가 뭘 했는지 모른다.** 그게 이 컷의 전부다.
⚠️ **서연의 반응은 시선 변화 하나뿐이다.** 미소도 놀람도 멈춰 서는 것도 없다.
⚠️ **2화에서 서연의 V.O.가 없는 유일한 컷이다.** 3화 V.O. 소멸의 예고편.
⚠️ **심장박동을 쓰지 않는다.** 3화 컷 6과 쿠키, 두 번만.

> **왜 비·우산이 아닌가** — 앞 컷에 비 예보도 우산도 없어서 날씨가 갑자기 바뀌는 게
> 작위적이었다. 차도 쪽 자리 바꾸기는 **새로 설명할 설정이 하나도 없고**, 무대사로
> 시선만 바꾼다는 기능은 그대로다. 「우산 하나, 젖은 어깨」는 이 작품에서 유일하게
> 클리셰를 비틀지 않는 컷이었다.

**컷 12 (개별 인터뷰 하드컷) ★**
```
1) 준영 단독 — 회색 벽, 미디엄 샷
2) 서연 단독 — 아이보리 벽, 미디엄 클로즈업
3) 지원 단독 — 밝은 회백색 벽, 미디엄 샷
4) 서연 단독 — 2)와 완전히 동일한 프레임

준영: 그 니트 제가 골랐어요.
(하드컷)
서연: …무슨 니트요?
(하드컷)
지원: 쟤 그날 립 세 번 발랐어요.
(하드컷)
서연: …야.
```
⚠️ **세 사람은 같은 공간에 있지 않다.** 배경·조명 방향·프레임 사이즈를 셋 다 다르게 잡는다.
서로 쳐다보거나 반응하는 컷을 절대 넣지 않는다.
⚠️ **「…야.」는 지원에게 하는 말이 아니다.** 인터뷰어 앞에서 혼자 반응하는 것이라 더 웃긴다.

**컷 13 (인정) ★★**
```
서연: 호감은 아니고요.
(사이)
서연: 다음에 뭘 입고 올지는 좀 궁금해요.
```
⚠️ **부정이 먼저 오고 인정이 나중에 온다.** 순서가 바뀌면 캐릭터가 무너진다.
묻지도 않았는데 먼저 부정하는 게 서연이다.
⚠️ **이 화의 소재(남친룩)로 감정을 말한다.** 「좋아해요」라고 하지 않는다.
⚠️ **감상적으로 읽으면 안 된다.** 가벼운 톤으로 무거운 말을 해야 3화가 산다.

**컷 14 (세 번째 약속)**
```
[상단] 이민준
[민준 말풍선] 이번 주 토요일 괜찮으세요?
[입력창] "네." → (삭제) → "좋아요."
[서연 말풍선] 좋아요.
```
**암전.** > `자막: 그리고 세 번째 만남에서, 모든 게 바뀝니다.`

### ★ 컷 0 ↔ 컷 14 가 2화의 감정선이다
| | 컷 0 (두 번째 약속) | 컷 14 (세 번째 약속) |
|---|---|---|
| 보낸 말 | **"네."** | **"좋아요."** |
| 과정 | 고민 없이 바로 | **"네." 를 지우고 바꿔서** |
| 이유 | 예의상이니까 | 예의가 아니니까 |

**컷 0에서는 「네.」가 최선이었고, 컷 14에서는 「네.」가 부족하다.**
같은 자리에서 한 단어가 바뀌는 것으로 관계의 전진이 보인다.
**컷 0을 안 보면 컷 14가 그냥 답장이 된다.**

### 소개팅이 두 번 언급되고 방향이 뒤집힌다
| 컷 | 누가 | 말 | 효과 |
|---|---|---|---|
| 9A | 서연 | "소개팅이었어요" | 민준이 굳는다 |
| 10 | **민준** | **"지난달에 소개받은 분이랑요"** | **서연이 굳는다** |

## 3-3. 제3화 — 진심 (8컷 · ~70초) ✅ 대본 있음, 생성 대기

**영상 전체의 심장.** 받아치던 사람이 멈춘다.

### 3화에서만 금지되는 것
| | 1~2화 | 3화 |
|---|---|---|
| 서연 V.O. | 계속 나옴 | **한 번도 안 나옴** |
| 민준 V.O. | 한 번도 없음 | **컷 6에서 딱 한 번** ★ |
| 리듬 붕괴 후 컷 | — | **자르지 않고 한 테이크로 버팀** |

⚠️ **서연의 V.O.가 3화에 한 번도 안 나오는 것이 핵심이다.**
말할 게 없어서가 아니라 정리가 안 돼서다. 관객은 그 부재를 알아챈다.

### 컷 3~5 — 죽 티키타카 → 리듬 붕괴 ★
```
서연: "왜 왔어요?"
민준: "아, 그… 이거 주려고요."
서연: "뭔데요."
민준: "죽이요."
서연: "…죽이요?"
민준: "네. 죽."
서연: "…아니 왜 죽을."
민준: "아플 때 먹는 거니까요."
서연: "저 안 아픈데요."
민준: "…"
(사이)
민준: "…아파 보이는데요."

(서연, 대답하지 못한다. 이 화에서 처음이다)

민준: "제가 말을 잘 못해서요. 자꾸 이상한 걸 사와요."
민준: "근데 앞으로도 계속 이럴 거예요."
```
**"…아파 보이는데요"에서 리듬이 깨진다.** 그 앞까지는 완벽한 티키타카다.
죽 얘기로 여덟 번을 주고받다가, 민준이 한 박자 늦게 원래 하려던 말이 아닌 말을 한다.

### 컷 6 — 손 / 웜톤 전환 ★★ 이 영상의 정점
```
민준 (V.O.): …어떡하지.
```
1~2화는 채도 낮은 쿨톤. **여기서, 손이 닿는 순간에만 웜톤으로 전환한다.**
영상 전체에서 단 한 번뿐이다.

### 컷 7 — 인터뷰 / 서연이 말을 못 한다
```
서연: "……"
서연: (웃음) "아, 이거 설명이 안 되는데."
서연: "그냥… 아 뭐라고 하지."
서연: "…죽 때문인가."
```

### 딜리버리 — 프로필은 그대로, 이 한 줄만 추가
```
DELIVERY (this scene only): The exchange runs as fast banter until
Min-jun's line lands a beat late and answers something she did not ask.
From that point Seo-yeon does not reply. The rhythm they have kept up
all episode simply stops, and neither of them restarts it.
```

## 3-4. 최종화 + 쿠키 ⬜ **미작성**

채팅으로 컷 리스트를 논의했으나 **파일로 남기지 않았다.** 처음부터 다시 써야 한다.
알려진 것: 쿠키에 **리모컨 씬**이 있고, 거기서 심장박동을 두 번째(마지막)로 쓴다.

---

# 4. 캐릭터 설정

## 4-1. 캐스팅 대비 설계 ★

**한 씬에 같이 나오는 인물끼리 최소 두 축 이상 벌어지게 잡았다.**

| 캐릭터 | 음역대 | 속도 | 질감 | 억양 |
|---|---|---|---|---|
| 서연 (26) | 중고음 | 고른 페이스 | 가볍고 건조 | 서울 표준 |
| 민준 (27) | 중저음 바리톤 | 느림·머뭇 | 부드럽고 눌림 | 서울 표준 |
| 지원 (26, 친구) | 고음 | 아주 빠름 | 숨섞임·웃음 | 서울 구어 |
| 준영 (28, 친구) | 중음 | 보통·짧게 끊음 | 맑고 앞으로 나옴 | 서울 표준 |
| 정 이모 (38, 주선자) | 중음 | 느긋함 | 따뜻·약한 콧소리 | **부산 사투리** |

- **서연 ↔ 지원**이 가장 가까운 쌍 — 음역대·속도·질감 세 축으로 벌려놨다.
- **민준 ↔ 준영** — 음역대(중저음↔중음), 속도(머뭇↔짧게 끊음), 질감(눌림↔맑음).
- **정 이모를 부산 사투리로 뺀 것**은 의도적. 서울말 여성이 하나 더 늘면 서연과 섞인다.
- ⚠️ **태호(28, 남자 조연 2)는 폐기됐다.** 조연을 1:1 대칭으로 줄였다.

## 4-2. 조연 1:1 대칭 구조 ★

**남자 조연을 준영 한 명으로 줄였다.** 방자·향단 포지션.

| | 지원 | 준영 |
|---|---|---|
| 짝 | 서연 | 민준 |
| 웃음 만드는 법 | **말로 찌른다** | **얼굴이 무너진다** |
| 대사량 | 많다 | 적다 |
| 음역대 | 고음 | 중음 |

**역할은 같고 온도만 반대다.** 크로스컷할 때 음역대가 매 컷 교대로 튀어서 편집 리듬이 저절로 생긴다.

**3샷을 2샷으로 줄인 이유** — `omni_reference`에 얼굴 셋을 물리면 드리프트 확률이 급격히 올라간다.
2샷은 1화 컷 6에서 이미 검증된 조건이다.

**잃은 것도 적어둔다** — 태호의 「확신 → 당황 → 붕괴」 3단 리듬,
「태호는 인터넷, 준영은 실전」 대비, 컷 12의 공 다툼. 총 5초쯤 짧아졌다.

## 4-3. 인물별 확정 스펙

### 서연 (신부 · 26 · 이 영상의 화자)
- 비주얼 키워드: **"순한 얼굴로 독한 말 하는 사람"**
- 얼굴: 작고 부드러운 계란형, 크고 둥근 아몬드형 눈, **눈꼬리가 살짝 내려간 사슴 인상**,
  작고 도톰한 입술, 매우 밝은 도자기 피부, **정면 기준 화면 오른쪽 볼에 작은 점 하나**
- 헤어: 검정에 가까운 짙은 브라운 긴 생머리, **에어리 시스루 뱅** (숱 있는 일자 뱅 아님)
- 체형: 아담하고 마른 체형
- 1화 의상: 크림 아이보리 립드 니트 가디건 + 화이트 이너 + 블랙 스키니 + 화이트 스니커즈
- **2화 의상: 차콜 리브드 니트 + 차콜 미디 A라인 스커트 + 블랙 앵클부츠 + 얇은 골드 체인**

> 처음엔 어려 보이는 원인을 스커트 길이로 봤는데 틀렸다. **실제 원인은 신발과 앞머리였다.**
> 미니스커트+스니커즈+일자뱅 = 교복 / 미니스커트+로퍼+시스루뱅 = 20대 중반.

### 민준 (신랑 · 27)
- 얼굴: 슬림 V라인 계란형, 아몬드형 눈에 뚜렷한 쌍꺼풀, 짙고 굵은 일자 눈썹,
  도톰한 입술, 웜 아이보리 피부
- 헤어: 검정에 가까운 중간 길이, 윗머리 볼륨 + 부드러운 웨이브, **한쪽으로 넘긴 앞머리**
- 체형: 키 크고 매우 마름, 좁은 어깨, 긴 다리, **약간 뻣뻣한 자세**
- 의상 4벌 (아래 5장 참조)

### 지원 (서연의 친구 · 26)
- 얼굴: 작고 둥근 하관, **크고 둥근 토끼눈 + 눈꼬리 처짐 + 애교살 두툼**, 짙고 굵은 눈썹,
  건강한 웜톤 피부, 딥로즈 매트 립
- 헤어: **밝은 갈색 하이 포니테일**, 이마 전부 노출, 관자놀이 잔머리 몇 가닥
- 체형: 키 크고 글래머
- 의상: 블랙 리브드 크롭탑 + 워시드 미드블루 오버핏 데님 재킷 + 블랙 와이드 카고
  + 청키 화이트 스니커즈 + 큰 실버 후프 + 레이어드 실버 체인 2줄
- **색: 데님 블루 — 캐스트에서 유일하게 색을 가진다**

> ⚠️ **얼굴과 목소리가 일부러 어긋나 있다.** 순한 처진 눈인데 목소리는 밝고 빠르다.
> **순하게 생긴 애가 제일 정확하게 찌른다.**

### 준영 (민준의 친구 · 28)
- 얼굴: 짧고 둥근 얼굴, 소프트한 볼, **큰 둥근 눈 + 눈꼬리 수평**, 순하게 웃는 인상
- 안경: **얇은 라운드 와이어 프레임**, 웜 실버 — 이 캐릭터의 최대 식별자
- 헤어: 중간 길이 다크 브라운, 부드러운 웨이브, 이마 위로 흘러내림
- 의상: **차콜 그레이 크루넥 스웨트셔츠** (후드·끈·포켓 없음) + 차콜 팬츠 + 화이트 캔버스, 모자 없음
- **색: 무채색** — 컷 2에서 민준 혼자만 색을 가지게 하기 위함

> ⚠️ **놀리지 않는다.** 그냥 사실을 말하는데 악의가 없어서 더 아프다.
> 비꼬는 톤을 넣는 순간 캐릭터가 죽는다.

### 정 이모 (주선자 · 38)
**목소리만 나온다. 화면에 안 잡히므로 캐릭터 시트가 필요 없다.**

## 4-4. 캐스트 전체 색 설계 ★

| 인물 | 색 |
|---|---|
| 서연 | 크림 아이보리 + 블랙 / 2화는 차콜 |
| 민준 (2~5컷) | **형광 주황** |
| 민준 (6컷~) | 크림 |
| 지원 | **데님 블루** |
| 준영 | 차콜 그레이 (무채색) |

**주연이 무채색·크림으로 묶이고, 조연 중 지원만 색을 가진다.**
컷 2에서는 민준의 형광 주황만 튄다 — 그게 그 컷의 개그다.

---

# 5. 확정된 에셋 — 레퍼런스 ID 표 ★

**컷 생성 시 반드시 여기 ID를 건다.**

| 태그 | 인물 / 의상 | ID | 상태 |
|---|---|---|---|
| `@char_MINJUN_base_v2` | 아이보리 셔츠 + 블랙 슬랙스 | job `67b1d302-0a28-4b4b-8ecb-6343f1eaecdd` | ✅ 얼굴 기준 |
| `@char_MINJUN_suit_v1` | **네이비 풀정장** | job `02b92aef-d68d-4ca7-bf19-d3e9454d3454` | ✅ 1화 전용 |
| `@char_MINJUN_knit_v1` | 크림 니트 + 차콜 슬랙스 | job `b436b93b-bf9e-4951-a386-0202f23748d5` | ✅ 2화 6컷~ |
| `@char_MINJUN_hike_v1` | **형광 주황 등산복 + 정장 바지 + 갈색 구두** | job `6d5eec88-7c34-4bb5-942c-133e1746c2cd` | ✅ 2화 1~5컷 |
| `@char_SEOYEON_v2` | 크림 가디건 (1화) | media `602a8bd9-97b3-4225-bb97-ac96c4ebfc0d` | ✅ |
| — | 서연 표정 4종 | media `60cd952d-46c4-4248-ae64-8c9b62153df4` | ✅ |
| `@char_SEOYEON_ep2_v1` | **차콜 니트 + 미디 스커트 (2화)** | ⬜ **ID 필요** | 이미지만 확정 |
| `@char_JIWON_v1` | 지원 3분할 기본 | media `ca093c40-0b72-42f6-86f9-361e75518119` | ✅ |
| — | 지원 얼굴 4방향 턴어라운드 | job `3302194d-081d-4f86-a89c-e35454958a20` | ✅ |
| — | 지원 표정 4종 | job `f08fb369-e2fb-41a7-8f58-2c4bcaeec685` | ✅ |
| `@char_JUNYOUNG_v1` | **준영 3분할 기본 (그레이 크루넥)** | ⬜ **ID 필요** | 이미지만 확정 |
| — | 준영 얼굴 4방향 턴어라운드 | job `60a574d7-07b1-4cfb-99a0-c9dfdb7b0c7c` | ✅ |
| — | 준영 표정 4종 | job `a3ec3059-eec3-4b10-b5d1-599238c10eb3` | ✅ |
| — | 준영 얼굴 레퍼런스 (구 시트) | media `e6834d7b-6bea-4b7a-976a-cb57541eb7f0` | ✅ 생성 성공 확인 |

⚠️ **폐기된 ID** — `96c95fc5-f281-4f49-b12b-07b11bf51a45` (준영 재업로드분).
**다섯 번 연속 생성 실패했다.** 쓰지 말 것.

⚠️ **민준은 2화 컷 6에서 옷을 갈아입으므로 레퍼런스도 갈아 건다.**
등산복 시트로 6컷 이후를 뽑으면 의상이 섞인다.

## 5-1. 표정 시트는 레퍼런스가 아니다 ★

**컷 생성에는 걸지 않는다.** 1화 10컷 전부 3분할 기본 시트 2개만 걸고 뽑았고
「얼굴 유지(레퍼런스 2인 동시) ✅」 검증까지 끝났다.
표정을 레퍼런스로 걸면 오히려 그 표정이 고정돼서 방해가 된다.
**표정은 영상 프롬프트 텍스트로 지정한다.**

표정 시트를 만든 이유는 다르다 — **컷 프롬프트를 쓸 때와 편집할 때 감정 톤을 눈으로
확인하기 위해서다.** 그래서 범용 희로애락이 아니라 실제 컷에 대응시켰다.

| | 지원 | 준영 |
|---|---|---|
| 1 | 원피스 들이밀며 장난스럽게 (컷 3) | 안경 너머 곁눈질, 어이없음 (컷 2) |
| 2 | 찌른 직후 아무렇지 않은 얼굴 (컷 3) | 참다가 새어나오는 실소 (컷 2) |
| 3 | **아무 말 없이 그냥 쳐다봄 (컷 6)** ★ | 미안한 듯 정확한 사실을 말함 (컷 4) |
| 4 | 놀리듯 웃으며 배웅 (컷 7) | **말문이 막힘 (컷 5)** ★ |

각자 ★ 하나가 그 인물의 핵심이다. 지원은 **말을 안 하는 얼굴**, 준영은 **대답을 못 하는 얼굴**이다.

## 5-2. 인터뷰 컷도 시트가 따로 필요 없다

1화 컷 9를 보면 인터뷰는 `neutral wall` + `soft even interview lighting`으로
**배경과 조명만 다르게** 처리하고 의상은 시트 그대로 쓴다. 검증된 방식이다.

---

# 6. 보이스 프로필 — 원문 (복붙용) ★

> **보이스 프로필 바이블 v2 적용.**
> **프로필은 에셋이다. 모든 씬 프롬프트에 원문을 통째로 복붙한다. 패러프레이즈 금지.**
> 수정이 필요하면 v2로 버전을 올리고, 이후 모든 씬에 v2만 쓴다.

## `@voice_SEOYEON_v1` — 신부 서연 (이 영상의 화자)

```
SEO-YEON: A 26-year-old South Korean woman with a light, mid-high,
slightly dry voice. Even-paced, casual Seoul-standard Korean in a
talking-to-a-close-friend cadence — unpolished, with small breaths
and half-laughs falling between phrases.
Definitely a native South Korean speaker; never a foreign, dubbed or
AI-narrator accent; never a broadcast-narrator, audiobook or
voice-actress reading tone; no regional dialect.
```

⚠️ 이 캐릭터의 최대 위험은 **낭독체**다. 영상 전체 내레이션을 맡기 때문에 모델이 자꾸
내레이터 톤으로 끌고 간다. 그래서 네거티브를 3중으로 걸었다.

## `@voice_MINJUN_v1` — 신랑 민준

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

## `@voice_JIWON_v1` — 친구 지원

```
JI-WON: A 26-year-old South Korean woman with a bright, high, slightly
breathy voice. Fast, bouncy casual Seoul Korean with rising sentence-end
intonation and quick, giggly bursts.
Definitely a native South Korean speaker; never a foreign, dubbed or
AI-narrator accent; never a calm or measured delivery; no regional dialect.
```

## `@voice_JUNYOUNG_v1` — 친구 준영 ★v2

```
JUN-YOUNG: A 28-year-old South Korean man with a clear, mid-range voice
that sits forward and light. Ordinary-paced Seoul Korean spoken in short
finished sentences, in a mild, unassuming cadence that states an
inconvenient fact without putting any edge on it.
Definitely a native South Korean speaker; never a foreign, dubbed or
AI-narrator accent; never a low, deep or authoritative delivery; never a
sarcastic, mocking or teasing tone; no regional dialect.
```

⚠️ **v1(낮은 베이스바리톤 deadpan)은 폐기됐다.** 확정된 얼굴이 동그란 안경에 순하게 웃는
인상이라 무심한 저음이 얼굴과 싸웠다. 나이도 33 → 28로 내렸다.
⚠️ `states an inconvenient fact without putting any edge on it` 가 이 캐릭터의 전부다.
⚠️ **민준과 겹치지 않게 주의한다.** 민준은 문장을 못 끝내고, 준영은 짧게 끝낸다.

## `@voice_JUNGIMO_v1` — 주선자 정 이모

```
JUNG-IMO: A 38-year-old South Korean woman with a warm, mid-range,
slightly nasal voice. Unhurried Busan (Gyeongsang) dialect with a
coaxing, over-confident salesperson cadence.
The dialect stays identical in every line; never drifts into standard
Seoul Korean; never a foreign, dubbed or AI-narrator accent.
```

## 홍자매 딜리버리 공통 문구 (1~2화 전 컷에 붙임)

```
DELIVERY (romcom register): Lines are traded quickly and lightly,
overlapping at the edges as in natural conversation. Delivery is
colloquial and unforced, never declarative or literary. Reactions land
fast. When a pause happens it is short and awkward rather than weighty,
and it is broken by speech rather than held.
```

## 변동층 — 씬마다 새로 쓰는 5가지

**고정층에는 감정을 절대 넣지 않는다.** 아래는 씬 프롬프트 쪽에 매번 새로 쓴다.

1. 이 씬의 감정 딜리버리
2. 물리 동작과 목소리의 관계 (걸으며 / 뛰며 / 울먹이며)
3. 발화 대상 잠금 (누구에게 하는 말인가)
4. 발화자 수 + 비언어 사운드 규격
5. **대사 볼륨** — 조용한 씬일수록 반드시 명시

## 3층 거리 규칙 ★

| 층 | 마이크 거리 | 처리 |
|---|---|---|
| 현장 대사 | 보통 | 공간 반사음 있음 |
| 인터뷰 컷 | 근접 | 건조, 룸톤만 |
| V.O. 내레이션 | 가장 근접 | 완전 건조 |

**이 거리 차이가 영상의 구조를 소리로 설명한다.** 섞이면 지금 어느 시점인지 헷갈린다.

## 출고 전 보이스 체크리스트

| | 확인 |
|---|---|
| F1 | 프로필 **원문**을 VOICES 섹션에 통째로 넣었는가 (태그만 참조하지 않았는가) |
| F2 | 각 프로필 끝에 `never` 문장이 붙어 있는가 |
| F3 | 프로필에 감정어가 안 들어갔는가 (감정은 DELIVERY에만) |
| F4 | 같은 씬 화자들이 최소 두 축 이상 벌어져 있는가 |
| F5 | 발화자 수를 명시했는가. 말 안 하는 인물의 소리를 규격화했는가 |
| F6 | 프로필 문구가 지난 씬과 **토씨까지 동일한가** |
| + | 대사 볼륨을 명시했는가 |

## 3화 전용 딜리버리 — 프로필은 그대로, 이것만 덧붙임

**S#3-4 · 신랑 고백 (최고 난도)**
```
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
⚠️ 고정층의 `halting`과 이 문장의 `hesitation drops away`가 정면으로 부딪힌다. **의도된 것이다.**
1~2화 내내 더듬던 사람이 여기서만 안 더듬는 것 — 그 차이가 들려야 3화가 산다.
**프로필 자체는 절대 수정하지 말고 딜리버리 문장으로만 덮는다.**

**S#3-3 · 신부 내레이션 (영상의 심장)**
```
DELIVERY: Quiet and held back. She is suppressing tears, not crying —
the voice thickens slightly and slows, but never breaks into sobbing.
No warmth is added; the restraint is what carries the emotion.
ADDRESSING: Spoken to an unseen interviewer.
SPEAKERS: One speaker only. Exact lines, no ad-libs.
PHYSICALITY: A held breath before the second sentence.
PROCESSING: Close-mic'd voice-over, completely dry.
```
⚠️ **울면 실패다. 우는 걸 참는 소리여야 한다.** 감정을 얹지 말고 빼는 방향으로 지시할 것.

## 사람이 직접 녹음할 경우

AI 생성이 아니라 신랑신부가 직접 녹음한다면 위 프로필은 **연기 지시서**로 쓴다.

- V.O.는 한 번에 다 읽지 말고 **구간별로 따로 녹음한다.** 감정이 이어지지 않는다.
- 이불 뒤집어쓰고 녹음하면 울림이 잡힌다. V.O.는 이걸로 충분하다.
- 휴대폰도 근접이면 쓸 만하다. 멀어지는 순간 폰 티가 난다.
- 전화 필터는 후반에서 EQ로 만든다. **실제로 전화로 녹음하지 말 것.**
- 서연 역에게는 **"읽지 말고 친구한테 얘기하듯"** 이 제일 잘 먹힌다.
- 민준 역에게는 **"잘하려고 하지 마세요"** 라고 해야 한다. 잘 읽으면 캐릭터가 죽는다.

---

# 7. 이미지 프롬프트 — 원문 (복붙용) ★

**모델**: `nano_banana_pro` · **비율**: `16:9` · 레퍼런스는 `image_references` 역할로 전달

## 7-1. 3분할 기본 시트 템플릿

**모든 캐릭터 시트가 이 골격을 쓴다.** `{}` 부분만 인물별로 갈아끼운다.

```
Three-panel character sheet of the EXACT SAME {MAN/WOMAN} as in the attached
reference image — same face, same eyes, same nose, same lips, same hair,
no change of facial identity. Only the outfit changes.

Warm beige subtly textured seamless studio background, professional character
sheet presentation, 3 panels divided by thin vertical dividers.

LEFT PANEL: full-body front-facing shot standing upright in a neutral straight
standing pose, both feet flat on the ground, full head-to-toe framing with the
whole body and both feet visible, head tilted slightly downward so the FACE IS
NOT VISIBLE.
CENTER PANEL: the same person, same outfit, full-body back view, standing, head
to toe, both feet visible.
RIGHT PANEL: tight front-facing close-up of the face and upper chest, cropped at
mid-chest so {의상의 목선 디테일} is clearly visible, calm neutral expression
looking directly at the camera.

IDENTITY, identical in all three panels: {얼굴 고정 문구}

HAIR, identical in all three panels: {헤어 고정 문구}

BODY: {체형 고정 문구}

WARDROBE, identical in all three panels: {의상}

LIGHTING: soft warm diffused studio lighting, gentle and even, identical
direction and tone across all three panels, everything in sharp focus front to
back.

QUALITY: high-end beauty editorial photography, Korean magazine quality,
cinematic realism, natural anatomy, 4K, sharp detail in the eyes and in the
{원단} textures.

NEGATIVE: {아래 7-5 참조}
```

## 7-2. 민준 등산복 시트 — 실제 사용 원문 ✅ 생성 성공

레퍼런스 `02b92aef-d68d-4ca7-bf19-d3e9454d3454` → 결과 job `6d5eec88-…`

```
Three-panel character sheet of the EXACT SAME MAN as in the attached reference
image — same face, same eyes, same nose, same lips, same hair, no change of
facial identity. Only the outfit changes.

Warm beige subtly textured seamless studio background, professional character
sheet presentation, 3 panels divided by thin vertical dividers.

LEFT PANEL: full-body front-facing shot standing upright in a neutral straight
standing pose, both feet flat on the ground, full head-to-toe framing with the
whole body and both feet visible, head tilted slightly downward so the FACE IS
NOT VISIBLE.
CENTER PANEL: the same man, same outfit, full-body back view, standing, head to
toe, both feet visible.
RIGHT PANEL: tight front-facing close-up of the same man's face and upper chest,
cropped at mid-chest so the jacket collar and zip are clearly visible, calm
neutral expression looking directly at the camera.

IDENTITY, identical in all three panels: an extremely handsome South Korean man
in his late 20s with a slim V-line oval face, a delicate but clearly defined
jawline and a narrow chin, high yet soft cheekbones. Almond eyes with clear
double eyelids, warm dark-brown irises and long dark lashes, a calm steady gaze.
Thick straight dark eyebrows set slightly low and close to the eyes. A straight
narrow nose bridge with a small refined tip. Soft full lips with a well-defined
cupid's bow and a natural muted-rose tone. Fair, smooth warm-ivory skin, clear
and blemish-free with only the very finest natural texture.

HAIR, identical in all three panels: medium-length near-black hair, voluminous
on top with soft loose waves and a fringe swept to one side across the forehead,
tapered short at the sides with the ears exposed, soft matte finish, styled and
static with no wind.

BODY: tall and very slim with narrow shoulders and long legs, standing with
slightly stiff posture, shoulders faintly tensed and arms held a little too
straight at the sides.

WARDROBE, identical in all three panels — each item is a genuine well-made
product of its own kind, worn together: a fluorescent hi-vis orange technical
hiking shell jacket in lightweight ripstop nylon, zipped up to mid-chest, with a
built-in hood lying flat at the back, elasticated cuffs and a drawcord hem, of
the quality of a serious outdoor brand; underneath it a plain white cotton
crewneck tee visible at the neckline; mid-grey tailored wool suit trousers with
a sharp pressed centre crease down each leg, sitting at the natural waist and
breaking cleanly at the ankle; polished brown leather derby dress shoes. No
watch, no bag, no backpack, no cap, no accessories, no patterns, no logos.

LIGHTING: soft warm diffused studio lighting, gentle and even, identical
direction and tone across all three panels, everything in sharp focus front to
back.

QUALITY: high-end beauty editorial photography, Korean magazine quality,
cinematic realism, natural anatomy, 4K, sharp detail in the eyes, in the nylon
sheen of the jacket and in the wool weave of the trousers.

NEGATIVE: no change of facial identity from the reference image, no cheap or
worn or dirty clothing, no torn or wrinkled fabric, no ill-fitting or baggy
trousers, no jeans, no chinos, no cargo trousers, no tracksuit bottoms, no
sneakers, no hiking boots, no sandals, no muted or dull orange, no red, no
patterned or colour-blocked jacket, no fleece, no puffer or padded jacket, no
raincoat, no backpack, no hiking poles, no cap or hat, no sunglasses, no rounder
or younger babyface, no heavier or muscular build, no facial hair or stubble, no
glasses, no earrings, no visible tattoos, no straight flat hair, no tight curls,
no wind-blown hair, no outdoor or mountain background, no golden-hour lighting,
no rim light, no bokeh, no shallow depth of field, no blurred background, no
text, no watermark, no logos, no frame borders, exactly one person per panel, no
other people, no duplicate figures beyond the three specified views, no
mannequin, no reflections, no props, no furniture, no background objects, empty
seamless studio, left and center panels standing full-body head-to-toe not
cropped not sitting, right panel a close-up not a full body, no plastic or waxy
CGI skin.
```

⚠️ `no cheap or worn or dirty clothing` 이 핵심이다. 이게 없으면 모델이 「형광 주황
등산복」을 촌스러움 신호로 읽고 **옷 전체를 싸구려로 만든다.**
민준의 첫 의상은 **「못생긴 옷」이 아니라 「조합이 틀린 옷」**이다. 각각은 제대로 된
고급품이어야 조합이 웃긴다.

## 7-3. 준영 3분할 기본 시트 — 그레이 크루넥 (외부 생성으로 통과)

레퍼런스 `e6834d7b-6bea-4b7a-976a-cb57541eb7f0`

```
Three-panel character sheet of the EXACT SAME MAN as in the attached reference
image — same face, same eyes, same nose, same lips, same round wire glasses,
same hair, same build, same height, same skin tone. Do not change his face at
all.

Warm beige subtly textured seamless studio background, professional character
sheet presentation, 3 panels divided by thin vertical dividers.

LEFT PANEL: full-body front-facing shot standing upright in a neutral straight
standing pose, both feet flat on the ground, full head-to-toe framing with the
whole body and both feet visible, head tilted slightly downward so the FACE IS
NOT VISIBLE.
CENTER PANEL: the same man, same outfit, full-body back view, standing, head to
toe, both feet visible.
RIGHT PANEL: tight front-facing close-up of the same man's face and upper chest,
cropped at mid-chest so the ribbed crew collar is clearly visible, a calm
relaxed expression with the mouth closed, looking directly at the camera.

IDENTITY, identical in all three panels: a South Korean man in his late 20s with
a short rounded face, soft full cheeks and a gentle short jawline. Large round
wide-open eyes with clearly visible double eyelid creases, large dark brown
irises, outer corners level with the inner corners. Softly arched dark eyebrows.
A small straight nose with a rounded tip. Thin lips resting in a slight natural
upward curve. Fair clear skin with fine natural texture, clean-shaven. Thin
round wire-frame metal glasses in a warm silver tone, sitting level on the nose,
worn in all three panels, with clear flat lenses — no tint, no glare, no
reflection — so the eyes stay fully visible.

HAIR, identical in all three panels: medium-length dark brown hair, soft and
slightly wavy with natural volume, falling loosely over the forehead and
covering part of the ears, soft matte finish, styled and static with no wind.
Bare head, no headwear of any kind.

BODY: average height with a slim build, standing relaxed with the arms hanging
at the sides.

WARDROBE, identical in all three panels: a plain warm mid-grey cotton crew-neck
sweatshirt in a comfortable regular fit, with a ribbed round crew collar sitting
close at the base of the neck, plain set-in long sleeves reaching the wrist with
ribbed cuffs, and a plain ribbed hem — completely plain, with no hood, no
drawstrings, no pocket, no zipper and no buttons; charcoal-grey cotton trousers,
straight and loose through the leg to the ankle; white canvas low-top sneakers
with a rubber toe cap. No cap, no watch, no bag, no patterns, no logos.

LIGHTING: soft warm diffused studio lighting, gentle and even, identical
direction and tone across all three panels, everything in sharp focus front to
back.

QUALITY: high-end editorial photography, Korean magazine quality, casual modern
styling, photorealistic, cinematic realism, natural correct human anatomy, 4K,
sharp detail in the eyes behind the lenses and in the cotton jersey texture.

NEGATIVE: no change of facial identity from the reference image, no different
person, no hoodie, no hood, no drawstrings, no kangaroo pocket, no zipper, no
buttons, no collar, no polo collar, no v-neck, no turtleneck, no corduroy, no
overshirt, no cardigan, no knit sweater, no jacket, no blazer, no denim, no
jeans, no cap or hat, no beanie, no mustard or yellow or ochre or orange
clothing, no burgundy or red clothing, no cream or ivory clothing, no green or
mint or teal clothing, no removal of the glasses, no thick black square glasses,
no lens glare, no reflection on the lenses, no small eyes, no narrow or slanted
eyes, no long face, no pointed chin, no facial hair or stubble, no slicked-back
hair, no wide grin, no visible teeth, no wind-blown hair, no golden-hour
lighting, no rim light, no bokeh, no shallow depth of field, no blurred
background, no grey seamless background, no text, no watermark, no logos, no
frame borders, exactly one person per panel, no other people, no duplicate
figures beyond the three specified views, no four-panel layout, no mannequin, no
props, no furniture, no background objects, empty seamless studio, left and
center panels standing full-body head-to-toe not cropped not sitting, right
panel a close-up not a full body, no plastic or waxy CGI skin.
```

⚠️ `no hoodie, no hood, no drawstrings, no kangaroo pocket` 가 이번 판의 핵심이다.
**회색 상의를 지시하면 모델이 후디로 흘러간다.**

## 7-4. 얼굴 4방향 턴어라운드 — 실제 사용 원문 ✅ 생성 성공

준영 예시 (레퍼런스 `e6834d7b-…` → job `60a574d7-…`).
지원은 같은 골격에 얼굴/헤어 문구만 갈아끼웠다 (job `3302194d-…`).

```
Head turnaround sheet of the EXACT SAME MAN as in the attached reference image —
same face, same eyes, same nose, same lips, same glasses, same hair, same skin
tone, no change of identity.

Warm beige subtly textured seamless background, 4-panel composition divided by
thin vertical dividers, showing a 4-way turnaround of the same person's head:

1) full profile, 90 degree side view, facing frame left
2) three-quarter 45 degree view
3) straight front view
4) full back view showing the back of the head

Cropped at the collarbone in every panel so only the head, neck and the top of
the shoulders are visible. Calm neutral expression throughout.

FACE, identical in all four panels: {얼굴 고정 문구}

HAIR, identical in all four panels: {헤어 고정 문구}
The back view shows the full crown and the natural hairline at the nape.

Wardrobe visible: a plain crew neckline only, the same in all four panels.

LIGHTING: soft frontal diffused light, identical direction and tone across all
four panels.

Keep hairstyle, skin tone, glasses shape and facial identity fully identical
across all four panels, and align head height and scale across the four panels.

NEGATIVE: no change of facial identity between panels, no different person, no
removal of the glasses, no lens glare, no cap or hat, no small eyes, no narrow
eyes, no long face, no pointed chin, no slicked-back hair, no smile, no text, no
watermark, no frame borders, no bokeh, no shallow depth of field, exactly one
person per panel, no other people, no props, no background objects, head and
shoulders only, no plastic or waxy CGI skin.
```

⚠️ **모자는 빼고 뽑는다.** 턴어라운드의 목적은 네 각도에서 두상과 헤어라인을 잡는 것인데,
캡이 정수리와 뒷머리를 가리면 후면 패널이 쓸모없어진다. 캡은 컷 프롬프트에서 씌운다.
⚠️ 안경 캐릭터는 `clear flat lenses so the eyes stay visible` + `no lens glare` 필수.
없으면 렌즈 반사로 눈이 안 보인다.

## 7-5. 네거티브 표준 세트

**모든 시트에 공통**
```
no text, no watermark, no logos, no frame borders, no bokeh, no shallow depth of
field, no blurred background, no wind-blown hair, no golden-hour lighting, no
rim light, exactly one person per panel, no other people, no duplicate figures
beyond the specified views, no mannequin, no reflections, no props, no
furniture, no background objects, empty seamless studio, no plastic or waxy CGI
skin
```

**레이아웃 잠금 (3분할)**
```
left and center panels standing full-body head-to-toe not cropped not sitting,
right panel a close-up not a full body, no four-panel layout
```

**정체성 잠금**
```
no change of facial identity from the reference image, no different person
```

---

# 8. 영상 프롬프트 — 원문 (복붙용) ★

## 8-1. 검증된 생성 조건 ✅

**1화 컷 6을 실제 생성해서 확인했다. 수정 없이 확정.** job `29f0a60e-bff1-4599-86e2-2c8cd967e1b4`

| 항목 | 값 |
|---|---|
| 모델 | `seedance_2_5` |
| 모드 | `omni_reference` |
| 비율 | `16:9` |
| 길이 | 10초 |
| 해상도 | 1080p (크레딧 부족 시 720p) |
| 오디오 | `generate_audio: true` |

| 검증 항목 | 결과 |
|---|---|
| BGM 차단 (`no background music, no score, no soundtrack`) | ✅ |
| 대사 겹침 (OVERLAP 블록) | ✅ |
| **얼굴 유지 (레퍼런스 2인 동시)** | ✅ |
| 앰비언스 소거 (손 닿는 순간) | ✅ |

## 8-2. 컷 프롬프트 골격

```
SUBJECT: {인물 태그} {행동}
CAMERA: {카메라 워크}
LIGHTING: {조명 + 그레이딩}

VOICES:
[{보이스 프로필 원문 통째로}]
[{두 번째 인물 프로필 원문 통째로}]
[홍자매 딜리버리 공통 문구]

DELIVERY: {이 씬의 감정 — 영어로}
ADDRESSING: {누구에게 하는 말인가}
SPEAKERS: {발화자 수}. Exact lines, no ad-libs, no extra voices.
DIALOGUE VOLUME: {볼륨 명시}

DIALOGUE (Korean):
{대사 — 한글 그대로, 이스케이프 금지}

SOUND: {현장음}. No music, no score.
```

## 8-3. 실제 사용 원문 — 1화 컷 6 (검증 컷) ✅

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

## 8-4. 공통 룩 블록 — 전 컷에 붙임

```
LOOK: Contemporary Seoul, autumn. Naturalistic cinematic photography,
muted slightly desaturated cool color grading. 35mm lens feel.
NEGATIVE: no background music, no score, no soundtrack, no on-screen
text, no subtitles, no watermark, no logos.
```

⚠️ **이탈리안 식당은 조명은 따뜻하되 그레이딩은 쿨하게.**
**웜톤 전환은 3화 컷 6(손) 단 한 번뿐이다.**

## 8-5. 말 겹침 지시 (필요한 컷에만)

```
OVERLAP: The two lines are spoken simultaneously and collide. Neither
line is cleanly audible over the other. Both stop abruptly at the same
moment, followed by silence.
```

## 8-6. 인터뷰 컷 처리

의상 시트는 그대로 쓰고 **배경과 조명만 바꾼다.**
```
SUBJECT: {인물} seated on a plain chair against a neutral wall, present
day, talking to an unseen interviewer.
CAMERA: static medium close-up, eyeline slightly off-lens.
LIGHTING: soft even interview lighting, neutral grade — visibly
different from the scene shots.
PROCESSING: Close-mic'd, completely dry, no room reverb.
ADDRESSING: To the unseen interviewer, never to the camera.
```

---

# 9. 파이프라인 실전 지식 — 겪은 함정들 ★

**같은 실수를 반복하지 않기 위해 남긴다.**

## 9-1. 한글 이스케이프 사고 (가장 비쌌던 실수)

프롬프트를 쓰면서 한글을 `\uXXXX`로 변환해 넣었다가 **글자가 틀린 채로 영상 3개가 생성됐다.**
`리`(리)를 쓰며 `맬`을 의도, `거`(거)를 쓰며 `끼`를 의도, `므`(므)를 쓰며 `믄`을 의도.

**해법: 한글을 그대로 타이핑하고, 제출 후 에코된 프롬프트에서 대사를 눈으로 확인한다.**

## 9-2. 형용사가 구조 스펙을 이긴다 ★★

**`extremely handsome`을 넣으면 모델이 학습된 K-pop 미남 프로토타입으로 수렴한다.**
그 프로토타입은 **긴 V라인 얼굴 + 아몬드 눈 + 마른 장신**이다.
「짧고 각진 얼굴 + 큰 둥근 눈 + 작고 다부짐」을 아무리 써도 형용사가 이긴다.

| 원하는 것 | 쓰면 안 되는 말 | 대신 쓸 것 |
|---|---|---|
| 잘생김 | `extremely handsome` | 이목구비 스펙만 나열 |
| 섹시함 | `sexy`, `voluptuous` | 구조 (크롭탑 + 로우라이즈 + 핏) |
| 웃기게 생김 | `funny-looking`, `goofy`, `ugly` | 부위 스펙 (비대칭·눈썹·눈-눈썹 거리) |
| 평범함 | `plain`, `average-looking` | **쓰지 말 것 — 얼굴이 뭉개진다** |

## 9-3. 키는 두상 비율로만 지정된다

3분할 시트에는 비교 대상이 없어서 `short`라고 써도 모델이 판단할 근거가 없다.
```
the total standing height is about six and a half head-lengths, not seven or eight
```
이렇게 **등신 수로 박아야** 먹힌다.

## 9-4. 안전 필터는 부정문을 이해하지 못한다 ★

`no cleavage, no plunging neckline, no push-up shaping, no underwear visible,
no swimwear, no bodycon, no sultry, no pin-up, no oiled skin` —
전부 **막으려고** 넣은 건데 필터는 문자열을 통째로 스캔한다. **생성이 차단됐다.**

**해법: 부정을 긍정 스펙으로 바꾼다.**
- `no cleavage` → `a high straight crew neckline sitting at the base of the throat`
- `no pin-up posing` → `a neutral standing reference pose, arms down and away from the sides`

## 9-5. 서로 모순되는 지시는 모델이 하나를 버린다

`pushed back off the shoulders so it hangs behind the arms` (어깨 뒤로 넘김)
\+ `sleeves pushed up to the forearm` (소매를 걷음 = 팔이 소매 안에 있음)
→ **물리적으로 불가능.** 모델이 후자를 택해 재킷을 정상 착용했고 상체가 다 가려졌다.

## 9-6. 실루엣은 노출이 아니라 핏에서 나온다

오버핏 재킷 + 로우라이즈 와이드는 실루엣이 통으로 떨어져서 허리·골반을 지정해도 안 보인다.
**재킷을 소매로 허리에 묶으면** 상체가 드러나고 골반선이 강조된다.

## 9-7. 얼굴 하나를 바꾸려면 세 군데를 동시에 건드려야 한다

「얼굴을 짧게」는 한 군데만 바꾸면 무시된다. 세 개를 같이 지정해야 움직인다.
1. 하관 길이 — `the distance from the base of the nose to the chin is brief`
2. 턱끝 — `slightly pointed chin` 같은 **반대 지시를 먼저 제거**
3. 세로:가로 비율 — `the width across the cheekbones is nearly equal to the height from hairline to chin`

보너스: `nose sitting low on the face` + `lips positioned close to the chin` 로
**이목구비 위치를 내리는 방식**이 턱만 깎는 것보다 자연스럽다.

## 9-8. 유아 비율 5종 세트 경고

하관 짧게 + 둥근 얼굴 + 애교살 + 처진 눈 + **큰 눈**을 다 지정하면 인형/애니 얼굴이 나온다.
성인 표식을 반드시 같이 넣는다 — `clearly an adult woman in her mid-20s, not a teenager`
\+ 네거티브 `no doll-like face, no anime or cartoon eyes, no baby or child-like proportions`

## 9-9. 준영 전신 시트 서버 차단 (미해결)

준영 3분할 전신 시트를 **다섯 번 시도해 전부 실패**했다.

| 시도 | 결과 |
|---|---|
| 긴 네거티브 리스트 | 실패 |
| 네거티브 대폭 축소 | 실패 |
| 레퍼런스를 job_id로 교체 | 실패 |
| 프롬프트 최소화 | 실패 |
| 준영 **얼굴/상반신** 시트 (턴어라운드·표정) | **성공** |
| 민준 전신 시트 (같은 구조) | **성공** |

**프롬프트 내용도 길이도 원인이 아니다.** 결국 사용자가 외부에서 같은 프롬프트로
생성해 통과시켰다. **같은 증상이 나오면 프롬프트를 고치느라 시간 쓰지 말고 바깥에서 돌린다.**

## 9-10. 폐기된 media_id

`96c95fc5-f281-4f49-b12b-07b11bf51a45` (준영 재업로드분) — 다섯 번 연속 실패.
같은 원본의 `e6834d7b-…` 로 바꾸니 즉시 통과했다. **업로드 레코드 자체가 깨질 수 있다.**

## 9-11. 이미지 확인 채널이 둘로 갈린다 ★

| 하려는 것 | 필요한 것 |
|---|---|
| 에이전트가 눈으로 보고 평가 | **채팅 첨부** |
| 생성 레퍼런스로 걸기 | **위젯 업로드 (media_id)** |

**둘은 배타적이다.** 채팅 첨부는 보이지만 못 걸고, 업로드된 media는 걸 수 있지만
CDN 차단으로 못 본다. **둘 다 필요하면 양쪽에 다 줘야 한다.**
> 이걸 몰라서 준영 의상을 두 번 잘못 기록했다(머스터드 → 실제로는 그레이 크루넥).

## 9-12. Higgsfield에서 직접 생성했다면 업로드 불필요

그쪽 결과는 이미 `job_id`가 있다. 그 ID를 그대로 레퍼런스로 걸면 된다.
업로드는 **외부 파일**일 때만 필요하다.

---

# 10. 아직 결정하지 않은 사항 ⬜

## 10-1. 확정 필요 — 작업이 막혀 있음

| 항목 | 상태 | 막는 것 |
|---|---|---|
| **서연 2화 룩 job ID** | 이미지는 확정, ID 없음 | 2화 전 컷 생성 |
| **준영 3분할 기본 시트 job ID** | 이미지는 확정, ID 없음 | 2화 옷가게 컷 |
| **최종화 대본** | 미작성 | 4부작 완성 |
| **쿠키 대본** | 미작성 | 리모컨 씬 + 두 번째 심장박동 |

## 10-2. 미결 판단

**① 식전영상으로도 쓸 것인가**
`CLAUDE.md` 에는 아직 식전영상으로 되어 있다. 쓰레드 드라마로만 가면 상관없지만,
결혼식장에서도 튼다면 **지원의 크롭탑이 어른들 앞에서 상영된다.** 판단 필요.

**② 컷 2의 색 물림**
민준 형광 주황 ↔ 준영 차콜 그레이. 준영이 무채색이라 문제없다고 판단했지만
**컷 2를 처음 뽑을 때 실제로 확인한다.**

**③ 지원 표정 시트 1·2번**
결과가 서로 비슷하게 나왔다(둘 다 옅은 미소). 3번(무표정)·4번(웃음)이 양 끝을
잡아주므로 지침으로는 쓸 수 있다고 보고 재생성하지 않았다. **필요하면 다시 뽑는다.**

**④ 음악**
`docs/suno-music.md` 에 「한 멜로디 두 편곡」안이 있다.
1화는 통통 튀는 편곡, 3화는 덜어낸 리프라이즈. **아직 실제 생성 안 함.**
⚠️ 시나리오에는 절대 음악을 넣지 않는다 (규칙 ②). 음악은 편집 단계에서 사용자가 얹는다.

**⑤ 자막**
`docs/subtitles/` 에 KO/EN 번역표가 있다. **SRT 파일은 편집 타임라인이 잠긴 뒤에 만든다.**
⚠️ `망했다` 는 1화·2화 양쪽에서 반드시 `I'm done for` 로 통일한다 (콜백이라서).

**⑥ 1화 컷 1 사투리 오타**
`그라므` → `그라믄`. 재생성 비용 때문에 미뤄뒀다.

---

# 11. 다음에 해야 할 작업

## 우선순위 1 — 2화 컷 생성 (막혀 있음)

1. **서연 2화 룩 / 준영 그레이 시트 job ID 확보** ← 이게 없으면 시작 못 함
2. `docs/episode2-hong.md` 레퍼런스 표에 ID 채우기
3. **컷 2부터 생성** — 등산복 시트와 준영 시트를 동시에 검증하고 색 물림도 바로 확인된다
4. 검증되면 나머지 15컷 순차 생성

**생성 조건 (1화에서 검증됨)**
```
모델: seedance_2_5
모드: omni_reference
비율: 16:9
길이: 10초
해상도: 1080p
오디오: generate_audio: true
```

⚠️ **민준은 컷 6에서 레퍼런스를 갈아 건다.** 1~5컷은 등산복 시트, 6컷 이후는 크림 니트 시트.
⚠️ **한글 대사는 이스케이프 없이 직접 입력하고, 제출 후 에코된 프롬프트에서 눈으로 확인한다.**

## 우선순위 2 — 최종화 + 쿠키 대본

채팅으로만 논의하고 파일로 남기지 않았다. **처음부터 다시 써야 한다.**
알려진 것 — 쿠키에 **리모컨 씬**이 있고 거기서 심장박동을 두 번째(마지막)로 쓴다.

지켜야 할 것:
- 홍자매 톤 유지
- 3화에서 넘어온 화자 구조 (민준이 말하기 시작한 상태)
- 웜톤은 3화 컷 6 이후 유지

## 우선순위 3 — 3화 컷 생성

대본은 `docs/episode3-hong.md` 에 있다. 2화가 끝나면 바로 갈 수 있다.

⚠️ **3화는 1~2화와 규칙이 다르다.**
- 서연 V.O. **0회** (한 번도 안 나온다)
- 민준 V.O. **컷 6에서 딱 1회** — `…어떡하지.`
- 리듬 붕괴 후 **컷을 자르지 않고 한 테이크로 버틴다**
- **컷 6(손)에서 웜톤으로 전환** — 영상 전체에서 유일한 전환

## 우선순위 4 — 후반

1. 음악 생성 (`docs/suno-music.md` 프롬프트 사용)
2. 편집 타임라인 확정
3. SRT 자막 (KO/EN)
4. 1화 컷 1 사투리 오타 수정

---

# 12. 파일 지도

| 파일 | 내용 |
|---|---|
| `CLAUDE.md` | **절대 규칙 6개.** 작업 전 반드시 읽는다 |
| `HANDOFF.md` | **이 문서.** 전체 인수인계 |
| `docs/episode1-hong.md` | 1화 컷 리스트 (**채택본**) + 파이프라인 검증 기록 |
| `docs/episode1-prompts-ready.md` | 1화 복붙용 프롬프트 + 대사 정오표 |
| `docs/episode1-delivery.md` | 1화 생성 결과 10컷 + 남은 이슈 |
| `docs/episode1-makjang.md` | 1화 임성한 버전 (**보류 · 내부용**) |
| `docs/episode2-hong.md` | **2화 확정본** (16컷 · 126초) |
| `docs/episode3-hong.md` | 3화 컷 리스트 (8컷) |
| `docs/voice-profiles.md` | **보이스 프로필 원문 + 바이블** |
| `docs/character-reference-groom.md` | 민준 시트 4벌 + 얼굴/헤어 고정 문구 |
| `docs/character-reference-bride.md` | 서연 시트 + 얼굴/헤어 고정 문구 |
| `docs/character-reference-support.md` | **조연(지원·준영) 시트 + 실패 기록** |
| `docs/suno-music.md` | 음악 브리프 (한 멜로디 두 편곡) |
| `docs/subtitles/` | KO/EN 번역표 |
| `docs/wedding-video-scenario.md` | 최초 4부작 시나리오 (초기 버전) |

---

# 13. 새 세션에서 시작할 때

```
1. CLAUDE.md 를 읽는다 (절대 규칙 6개)
2. 이 문서의 5장(레퍼런스 ID 표)과 9장(실전 함정)을 읽는다
3. 작업할 화의 docs/episodeN-hong.md 를 읽는다
4. 생성 전에 프롬프트를 사용자에게 보여주고 승인받는다
```

**가장 자주 사고가 나는 지점 세 개**
1. 한글 이스케이프 → **반드시 한글 직접 입력 + 에코 확인**
2. 형용사가 구조 스펙을 이김 → **`handsome` / `sexy` / `funny-looking` 쓰지 말 것**
3. 이미지를 보는 채널과 거는 채널이 다름 → **채팅 첨부 ≠ media_id**
