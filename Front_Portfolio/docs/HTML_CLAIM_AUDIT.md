# HTML Claim Audit

Date: 2026-05-31  
Scope: `web-starter/index.html` visible claims  
Purpose: prevent design-driven fabricated portfolio content.

## Source Priority

1. Latest resume: `docs/김택권_잡코리아 이력서_20260530.pdf`
2. Existing portfolio PDF: `docs/김택권 포트폴리오.pdf`
3. User-provided supplemental links:
   - `https://github.com/cheng80/rummipoker`
   - `https://bicfest.org/enroll/view/3405`
   - `https://cheng80.myqnapcloud.com/rummipoker/`
   - `https://github.com/cheng80/chatbot_rag_app`

Existing HTML is not a source of truth.

## Immediate Fixes Applied

| Existing HTML claim | Issue | New wording | Source basis |
|---|---|---|---|
| `14년 이상` | Latest resume says total career `13년 4개월`; portfolio PDF says `14년 이상`. Latest resume wins for current summary. | `13년 4개월` | Latest resume |
| `Flutter 앱 4종` | Could imply four launched/operated Flutter apps. Latest resume says three mobile apps launched and operated; portfolio PDF lists four app-store registration projects including release-preparing projects. | `앱 프로젝트 4종` | Portfolio PDF, with status labels required |

## Safe Claims

These are supported by the source documents and may remain in the deck.

| Claim | Source |
|---|---|
| Name `김택권` | Portfolio PDF, latest resume |
| Phone `010-2626-2131` | Portfolio PDF, latest resume |
| Email `cheng80@naver.com` | Portfolio PDF, latest resume |
| GitHub `github.com/cheng80` | Portfolio PDF |
| 2022.04 - 2024.02 Grovy Education | Portfolio PDF, latest resume |
| 2016.01 - 2022.04 Chunjae Education / Chunjae Textbook combined period | Portfolio PDF |
| 2020.12 - 2022.04 Chunjae Textbook media team part lead | Latest resume |
| 2016.01 - 2020.12 Chunjae Education media team part lead | Latest resume |
| `80여종 이상의 앱 제작, 출시 및 유지보수` | Latest resume |
| TagDo description, stack, links | Portfolio PDF |
| HabitCell description, stack, links | Portfolio PDF, with PDF title conflict corrected from TOC/features |
| GlucoInsight description, stack, links, `출시 준비중(심사중)` | Portfolio PDF |
| SyncFlow description, stack, GitHub, `출시 준비중` | Portfolio PDF |
| 순서대로 탭탭 Flutter/Flame web demo and GitHub | Portfolio PDF |
| Grovy / Chunjae project descriptions and video links | Portfolio PDF |
| Hardware serial, Arduino, ESP32, MQTT-SSL evidence | Portfolio PDF |

## Claims Requiring Careful Labels

| Topic | Safe treatment |
|---|---|
| Flutter launched app count | Use latest resume wording only when saying launched/operated: `세 개의 모바일 앱`. Use portfolio PDF wording when saying app projects: `앱스토어 등록 프로젝트 4개`. |
| GlucoInsight | Label as `출시 준비중(심사중)` unless a newer source is provided. |
| SyncFlow | Label as `출시 준비중`. |
| AI/RAG | Present as current project and training evidence. Do not claim years of production AI/RAG experience. |
| Rummi Poker BIC | Say `BIC 출품` only. Do not say selected, awarded, exhibited, or winner unless later verified. |
| Rummi Poker playable build | Use `Playable Web build` with the user-provided URL. |

## Remove / Avoid

Do not add the following unless a source is later provided:

- download counts
- revenue
- user counts, except where latest resume explicitly says `회원수 7000명` for 우주좀비
- ranking, except where latest resume explicitly says `2주간 유료 매출 2위` for 우주좀비
- awards, except latest resume education/award entries and user-provided BIC submission link
- AI/RAG production-years claims
- generic claims like "expert", "top-tier", "high-performance" without evidence

## Implementation Rule

Before editing visible portfolio text, tag each claim mentally as:

```text
PDF source
Latest resume source
User-provided supplemental source
Derived phrasing from source facts
Unknown / remove
```

`Unknown / remove` claims must not ship.


## Stone Match 추가 근거 (2026-11-04)

사용자가 지정한 `jewelmatch` 프로젝트를 Rummi Poker 다음에 추가했다. 외부 표시명은 프로젝트 지침에 따라 `Stone Match`로 사용한다.

- 소스: `https://github.com/cheng80/jewelmatch`, 로컬 확인 기준 커밋 `5a502bb`.
- 로컬 원본: `/Users/cheng80/Desktop/Anther_Works/Flutter_Project/FlutterFrame_work/jewelmatch`.
- 게임 정의: `docs/01_PRODUCT_SPEC.md`, `lib/game/jewel_game_mode.dart`, `lib/game/match_board_logic.dart`에서 8×8 매치 3, 무한/레벨/타임 모드, 콤보와 특수 보석을 확인했다.
- 백엔드: `lib/services/backend/backend_selector.dart`와 `docs/progress/HANDOFF_2026-10-28_INTOSS.md`에서 PocketBase 랭킹 연동을 확인했다.
- 앱인토스: 위 인계 문서와 광고 서비스의 구현 근거로 `광고 연동 구현`으로 표시한다. 스토어 출시나 토스 정식 출시를 의미하지 않는다.
- 웹 주소: `docs/04_DEVELOPMENT_WORKFLOW.md`에 기록된 `https://cheng80.myqnapcloud.com/match/`를 사용한다.
- 타이틀 스크린샷: 사용자가 지정한 `docs/assets/release/intoss/screenshot_portrait_01_title_636x1048.png`를 사용한다. 두 번째 사진은 아래의 새 레벨 모드 촬영본으로 교체했다. 두 사진 모두 636×1048 비율과 동일한 프레임으로 표시한다.
- 출시 상태, 사용자 수, 성과 수치, 성능 개선 수치와 수상 이력은 추가하지 않는다.


### 레벨 / 타임 모드 이펙트 촬영 (2026-11-04)

- 사용자 요청에 따라 Ego Lite 백그라운드 촬영으로 만들었다. 타이머와 애니메이션 시점을 고정한 디버그 픽스처를 사용했다.
- 원본 게임 `lib/`를 `tmp/portfolio-capture-20261104/fixture-lib/`로 복사하고 촬영 전용 훅만 추가해 로컬 빌드했다. 원본 게임 코드는 수정하지 않았다.
- 하이퍼 큐브와 토르 망치를 장착하고, 원래 `useTestItem` / `handleBoardTap` 경로로 아이템을 사용했다. 실제 게임의 렌더링을 캡처했으며 이미지를 합성하지 않았다.
- 레벨 화면: 사용자가 선택한 토르 망치의 십자번개 장면이다. `assets/reference/stone-match/stone-match-level-thor-hammer.png`에 보존하고 웹과 슬라이드의 `stone-match-gameplay.png`로 복사했다.
- 타임 화면: 하이퍼 큐브의 에너지와 보석 파편 장면을 `assets/reference/stone-match/stone-match-time-hyper-cube.png`에 보존했다. 현재 포트폴리오의 두 번째 사진은 레벨 화면을 사용한다.
- 두 촬영본은 636×1048 PNG다. 고정 시드, 레벨, 시간, 아이템 재고를 사용한 연출용 자료이며 실제 사용자 플레이 기록이나 성능 측정 근거로 사용하지 않는다.
