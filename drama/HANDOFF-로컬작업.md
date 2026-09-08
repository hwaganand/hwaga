# 로컬 작업 인계서

**대본은 12화까지 다 끝났다. 여기서부터는 로컬 Claude Code + `hamlog-ai-drama-pipeline` 플러그인으로 제작 단계를 진행한다.**

웹 세션(Claude Code on the web)에는 플러그인이 없어서 대본까지만 만들었다.
이 파일은 그 작업을 로컬로 넘기기 위한 인계서다.

---

## 0. 시작 전에 — 스킬 규격부터 읽어라

**이게 첫 번째 할 일이다. 건너뛰지 마라.**

```
hamlog-ai-drama-pipeline 플러그인의 4개 스킬 내용을 읽고,
각각 어떤 입력을 받아 어떤 형식으로 출력하는지 정리해서 보여줘
```

| 스킬 | 예상 용도 |
|---|---|
| `drama-ops` | 제작 전반 운영 |
| `ai-character-drama` | 캐릭터 설정·일관성 |
| `screenplay-pipeline` | 대본 → 컷 분해 |
| `seedance-cut-prompt` | 컷 → Seedance 프롬프트 |

### ⚠️ 충돌 시 규칙
**스킬 규격이 이 레포의 기존 파일 형식과 다르면, 스킬이 이긴다.**
`drama/` 안의 md 파일들은 플러그인이 있는 걸 모르고 손으로 쓴 것이다.
내용(연출 의도, 대사, 톤)은 살리고 **형식은 스킬 규격으로 갈아끼운다.**

특히 `drama/cuts/1화-컷01.md`는 확실히 규격 밖이다. 이 파일 안에도 경고를 적어뒀다.

---

## 1. 지금 상태

### ✅ 끝난 것
| 항목 | 파일 |
|---|---|
| 시리즈 바이블 | `drama/00-시리즈바이블.md` |
| **1~12화 대본 전편** | `drama/01화-*.md` ~ `12화-부장.md` |
| 시즌 구성표 | `drama/시즌1-구성표.md` |
| 캐릭터 4인 레퍼런스 프롬프트 | `drama/codex-handoff/prompts/01~04-*.md` |
| 오정우 얼굴 **확정** | 아래 참조 |
| 제작 체크리스트 | `drama/제작-체크리스트.md` |

### ❌ 안 된 것
- 나머지 3인(박정만·한대성·이서진) 레퍼런스 이미지
- **배경 레퍼런스 3종** (회의실·사무실·고깃집)
- 컷 프롬프트 (1화 컷1만 있고 그마저 규격 밖)
- 영상·음성 생성 일체

### 오정우 얼굴 — 확정됨
Topview GPT Image 2로 생성한 3분할 시트.
**크림 니트 카디건 + 둥근 얇은 은테 안경 + 흰 카라셔츠 + 검은 줄 사원증**
- 원본 URL: `https://api.topview.ai/s/0wkV7Duy` (2736×1536)
- Higgsfield media_id: `36e9d7bf-bd6a-4066-a460-e057aed32cc1` (시트 전체)

원래 설정(회색 와이셔츠, 안경 없음)에서 벗어났지만 그대로 채택했다.
**안경은 1화 컷1의 3초 훅 연출로 흡수했다** — 형광등 반사가 안경알에서 걷히며 눈이 드러나는 컷.

---

## 2. 작업 순서

### Phase 1 — 미해결 이슈 3건 (제일 먼저)

**1-1. 이서진 의상 변경**
정우가 크림 카디건이 되면서 이서진 설정(오버사이즈 베이지 카디건)과 겹친다.
→ **네이비 후드집업 + 청바지**로 변경.
`drama/codex-handoff/prompts/04-이서진.md` 의 의상 문구를 전부 교체.

**1-2. 안경 구분**
정우·박부장 둘 다 안경이다. 실루엣으로 구분이 안 된다.
→ 정우 = `round thin silver-rimmed glasses` (둥근 얇은 은테, 이미 확정된 얼굴 그대로)
→ 박부장 = `thin rectangular silver-rimmed glasses` (얇은 **사각** 은테)
`prompts/02-박정만.md` 의 안경 문구를 전부 `rectangular`로 교체.

**1-3. 얼굴 레퍼런스 크롭**
지금 있는 건 3분할 시트 전체다. 그대로 참조로 쓰면 모델이 3분할 구도를 따라하거나 전신샷을 낸다.
→ **오른쪽 1/3(x축 1824~2736)만 크롭**해서 `face-ref.png`로 저장.
```python
from PIL import Image
im = Image.open("sheet1-body.png")
w, h = im.size
im.crop((int(w*2/3), 0, w, h)).save("face-ref.png")
```

### Phase 2 — 캐릭터 레퍼런스 나머지 3인
`drama/codex-handoff/CLAUDE.md` 에 절차가 다 적혀 있다. 그대로 따르되,
**`ai-character-drama` 스킬 규격이 있으면 그쪽을 우선한다.**

생성 도구는 둘 중 편한 쪽:
- `codex-imagegen` 스킬 → ChatGPT 구독 쿼터, API 키 불필요, 참조 이미지 1~16장 지원
  ```bash
  ~/.claude/skills/codex-imagegen/codex-imagegen.sh "프롬프트" /출력.png /참조.png
  ```
- Topview (크레딧 약 470 남음, 1장 3.2)

### Phase 3 — 배경 레퍼런스 3종 ★ 빠뜨리기 쉬움
**없으면 컷마다 회의실 모양이 달라져서 같은 공간으로 안 보인다.**
1화는 대부분 회의실이라 최소한 회의실은 필수.

| 배경 | 영어 프롬프트 |
|---|---|
| 회의실 | `mid-size Korean corporate meeting room, long table, projector screen, vertical blinds, fluorescent ceiling lights, muted desaturated color grade` |
| 사무실 | `open-plan Korean office, cubicle partitions, stacked documents, dual monitors, late evening with most lights off, muted desaturated color grade` |
| 고깃집 | `Korean BBQ restaurant, grill embedded in table, soju bottles, warm orange light, slightly crowded, muted desaturated color grade` |

각 3앵글씩 뽑아두면 컷마다 재사용된다.

### Phase 4 — 1화 컷 프롬프트
```
seedance-cut-prompt 스킬로 drama/01화-기획안.md 의 컷 12개 프롬프트를 만들어줘.
컷1은 drama/cuts/1화-컷01.md 에 연출 의도가 있으니 그 내용을 반영하되 형식은 스킬 규격으로.
```

### Phase 5 — 생성 → 편집
`drama/제작-체크리스트.md` 참조.

---

## 3. 영상 생성 파라미터 (Higgsfield / Seedance)

| 항목 | 값 |
|---|---|
| model | `seedance_2_5` |
| mode | `omni_reference` |
| medias role | `image_references` |
| aspect_ratio | `9:16` |
| duration | `4` (3초 컷 기준, 편집에서 트림) |
| generate_audio | **`false`** |

**`generate_audio`는 반드시 false.** AI 오디오는 쓸 수 없다. 사운드는 편집에서 붙인다.

### 비용 (4초 1컷 기준)
| 해상도 | 크레딧 |
|---|---|
| 1080p | 36 |
| 720p | 26 |
| 480p | 10 |

**12화 × 컷 10개 = 120컷을 1080p로 다 뽑으면 4,320 크레딧이다. 감당 안 된다.**

### 해결책 — 정지컷 혼용
- **대사 컷** → 영상
- **속마음 내레이션 컷** → 정지 이미지 + 아주 느린 줌인 (100% → 104%)

"속으로만 이긴다"가 컨셉이라 **정지 화면이 연출로도 먹힌다.** 비용은 1/10로 떨어진다.
화당 영상 4컷 + 정지 6컷 정도로 잡으면 현실적이다.

---

## 4. 절대 지킬 것 (톤 규칙)

1. **사이다 금지.** 정우는 매 화 표면적으로는 진다
2. **마지막 5초 = "속으로만 이겼다"**
3. **악당 없음.** 박부장도 위에서는 똑같이 당한다
4. **실존 회사·업종·제품 언급 금지**
5. **정치 용어 직접 사용 금지**

### 자막 규칙
- 화면 상단 30% 고정, 굵은 고딕, 한 줄 최대 16자
- **일반 대사 = 흰색 / 속마음 = 노란색**, 속마음에 괄호 붙이지 말 것
- 무음 시청 대응 (시청자 70%가 소리 끄고 본다)

### 12화 촬영 시 특별 지시
**12화 회의실 장면은 1화와 같은 앵글·조명·컷 길이로 맞춘다.**
같은 질문("이거 누가 만들었어?"), 같은 0.5초 정적. 대답만 다르다.
이게 시즌 전체의 회수 지점이라 여기서 앵글이 틀어지면 효과가 죽는다.

---

## 5. 복붙용 — 로컬 Claude Code에 순서대로

```
1) hamlog-ai-drama-pipeline 스킬 4개 읽고 각각 뭐 하는 건지 정리해줘

2) drama/HANDOFF-로컬작업.md 의 Phase 1 미해결 이슈 3건 처리해줘

3) ai-character-drama 규격으로 박정만·한대성·이서진 레퍼런스 시트 만들어줘.
   오정우는 이미 확정됐으니 건드리지 마

4) 배경 레퍼런스 3종을 각 3앵글씩 뽑아줘

5) seedance-cut-prompt로 1화 컷 프롬프트 전부 만들어줘.
   대사 컷은 영상, 속마음 컷은 정지 이미지로 구분해서
```

---

## 6. 판단 지표 — 5화까지 보고 결정

| 지표 | 기준 |
|---|---|
| 3초 시청 유지율 | 70% 이상 |
| 완주율 | 50% 이상 |
| 댓글 "우리 회사도" 류 | 전체 30% 이상 |
| 구독 전환 | 조회 1000당 3명 |

**4개 중 3개 미달이면 6화 안 만들고 접는다.**
5화 엔딩("모르겠어")이 열린 결말로 성립하게 써놨으니 억지로 마무리 안 해도 된다.

통과하면 6화부터 이어가되, **매 5화 단위로 다시 본다.**
