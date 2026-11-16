# 다음 작업자를 위한 핸드오프

상태 확인일: **2026-11-16**. 경로와 명령은 모두 저장소 루트 기준이다.

## 지금 상태

김택권의 경력과 프로젝트를 소개하는 정적 HTML/CSS 포트폴리오다. 프론트엔드 우선 버전과 Unity 우선 버전을 각각 웹과 23장 슬라이드로 제공하며, 슬라이드에서 이미지 기반 PDF 2종을 생성한다. React/Vite 앱이 아니며 정적 사이트 준비와 검증에는 Python 표준 라이브러리만 사용한다.

- 프론트엔드와 Unity 웹 및 슬라이드에 FastAPI, SQL, Firebase(FCM), Supabase(PostgreSQL), GA4, Sentry, Cloudflare Pages, JavaScript 등 개인 프로젝트 기술과 Stone Match 운영 대시보드 경험을 반영했다. 두 슬라이드의 23장 구성은 유지했다. 최신 공개 상태와 배포 커밋은 [GitHub Pages 실행 기록](https://github.com/cheng80/web_portfolio/actions/workflows/pages.yml?query=branch%3Amain)에서 확인한다.
- Unity 슬라이드 1~6페이지 문구와 16:9 제출용 PDF 23쪽은 `b0df14d`에서 갱신했다. 변경 페이지에 잘림과 겹침이 없었다.
- 프론트엔드 웹의 첫 화면, 기술 카드, 대표 앱과 회사 프로젝트 소개를 갱신했다. 슬라이드 1, 3, 4, 18, 19페이지를 대조하고 16:9 PDF 23쪽을 다시 생성해 상위 폴더 사본도 교체했다. 변경 페이지에 잘림과 겹침이 없었고 사이트 테스트 4개가 통과했다.
- 앞선 소개 문구 수정에서 Unity 웹의 첫 화면과 회사 프로젝트 소개는 기존 문구를 유지했다.
- 기술 스택과 Stone Match를 갱신한 두 제출용 PDF는 23쪽, 16:9를 확인했다. 각 3장과 프론트엔드 12장, Unity 10장의 렌더에 잘림과 겹침이 없었다. 상위 폴더 사본은 SHA-256으로 일치 여부를 확인했고, Google Drive는 기존 링크를 유지한 채 두 파일을 교체해 파일 크기와 수정 시각을 다시 확인했다.
- **기존 로컬 변경:** `.nojekyll` 삭제와 `Front_Portfolio/docs/`의 잡코리아 이력서 PDF 수정이 미커밋 상태다. 관련 없는 작업에 포함하거나 임의로 복원하지 말고, 그 시점의 Git 상태와 사용자 지시를 확인한다.
- 이 문서는 상태 기록이다. 다시 열었을 때 `git status -sb`, `git log -5 --oneline`을 먼저 확인한다.

## 먼저 읽을 문서

| 문서 | 용도 |
| --- | --- |
| [README.md](README.md) | 구조, 소스와 공개 경로, 실행과 배포 |
| [AGENTS.md](AGENTS.md) | Codex 공통 작업 규칙 |
| [프론트엔드 시작 지침](Front_Portfolio/docs/CODEX_START_PROMPT.md) | 프론트엔드 수정 기준과 자료 우선순위 |
| [Unity 시작 지침](Unity_Portfolio/docs/CODEX_START_PROMPT.md) | Unity 강조 범위와 수정 기준 |
| [문구 검증 기록](Front_Portfolio/docs/HTML_CLAIM_AUDIT.md) | 경력, 프로젝트와 출시 상태의 확인 근거 |
| [Unity 내용 근거](Unity_Portfolio/docs/CONTENT_SOURCES.md) | 회사 콘텐츠, 우주좀비와 하드웨어 근거 |
| [AI 사례 근거](Front_Portfolio/docs/AI_WORKFLOW_SOURCES.md) | 실제 도구, 더미/주석 이미지와 주장 범위 |

`CODEX_PORTFOLIO_WEB_REDESIGN.md`, `RESOURCE_MANIFEST.md`와 `DESIGN.md`에는 초기 제작 계획도 남아 있다. 현재 구조와 충돌하는 React 전환 안내, 초기 장수와 출시 상태를 그대로 되살리지 않는다. 원본 사실은 각 버전 `docs/`의 이력서와 포트폴리오 PDF, 최신 사용자 제공 자료로 확인한다.

## 어디를 수정하는가

| 대상 | 본문 | 스타일 |
| --- | --- | --- |
| 메인 4개 연결 | `index.html` | 같은 파일의 `<style>` |
| 프론트엔드 웹 | `Front_Portfolio/web-starter/index.html` | 같은 폴더의 `styles.css` |
| 프론트엔드 슬라이드 | `Front_Portfolio/portfolio-ppt/index.html` | 같은 폴더의 `portfolio-ppt.css` |
| Unity 웹 | `Unity_Portfolio/web-starter/index.html` | 같은 폴더의 `styles.css` |
| Unity 슬라이드 | `Unity_Portfolio/portfolio-ppt/index.html` | 같은 폴더의 `portfolio-ppt.css` |

각 페이지의 `assets/`는 독립적으로 관리한다. 공통 이미지를 바꾸면 네 위치를 대조한다. AI 사례의 전용 CSS, 설명용 SVG와 카드 이미지는 각 `assets/ai-workflow/`에 있다. 참고 JSON은 실행 시 사용하지 않으며, HTML은 직접 수정한다.

`Front_Portfolio/index.html`은 프론트엔드만 로컬 실행할 때의 안내다. 공개 메인은 루트 `index.html`이며, 소스 폴더 전체를 배포하는 구조로 되돌리지 않는다.

## 유지할 확정 내용

- 총 개발 경력은 **2026-05-30 기준 13년 4개월**이다. 현재 날짜로 늘리거나 Unity 단일 기술의 경력으로 표현하지 않는다.
- 두 버전의 차이는 소개와 강조 순서다. 공통 상세 슬라이드 19장의 본문, 링크와 이미지는 같으며 AI 사례 4장도 이 19장에 포함된다.
- 프론트엔드는 앱 4종과 관광 챗봇을 먼저 소개한다. Unity는 회사 콘텐츠, 우주좀비, 하드웨어 연동을 먼저 소개한다. 우주좀비는 하드웨어 연동 바로 앞이다.
- 첫 화면과 경력 소개는 결과 보고 문체보다 개발 경험을 중심으로 쓴다. 프론트엔드는 앱과 웹 경험을 앞에 두고, AI 활용은 개발 프로세스 개선과 테스트 및 배포 관리, RAG 기반 챗봇 경험으로 설명한다. 관광 챗봇은 로컬 실행형 프로토타입이다.
- 두 슬라이드의 회사 프로젝트 소개는 그로비교육의 상호작용 설계와 서비스 운영, 천재교육 / 천재교과서의 교육도서와 교보재 연동 및 앱 출시와 유지보수 경험으로 정리했다. 프론트엔드 웹도 해당 카드 묶음에 문구를 반영했다.
- 최근 게임과 AI의 순서는 **Rummi Poker → Stone Match → AI 사례 4개 → 순서대로 탭탭**이다. 웹과 슬라이드에 함께 적용되어 있다.
- AI 사례 순서는 **종합 소개 → 자동 플레이 검증 도구 → 밸런스 시뮬레이터와 분석 도구 → 카드 아트 제작**이다. 프론트엔드 슬라이드 13~16장, Unity 11~14장이다. 웹에서는 `#ai-workflow` 안의 `[data-ai-case]` 4개이며, 값은 순서대로 `overview`, `bots`, `balance`, `art`다.
- 종합 소개의 명칭은 `에이전트 오케스트레이션`, `자동 플레이 검증 도구 제작`, `자동 배포 환경 구축`이다. 밸런스 사례는 도구의 기능을 설명하며 가상의 통계표와 개선 수치를 사용하지 않는다.
- Stone Match 색 인식 이미지는 설명용 더미다. Rummi Poker 봇 이미지는 실제 전투 화면에 설명 표시를 더한 예시다. 이를 실제 봇 실행 캡처나 성과 측정 결과로 소개하지 않는다.
- Stone Match 두 번째 사진은 **레벨 모드의 토르 망치 효과** 촬영본이다. 시간 모드 하이퍼 큐브 촬영본도 `Front_Portfolio/assets/reference/stone-match/`에 보존했다.
- AI 사례의 하단에는 `AI 활용 범위`만 표시한다. `내 역할`, 녹색 출처와 사족을 다시 추가하지 않는다. 확정 시안 4장은 `Front_Portfolio/assets/reference/ai-workflow/`에 있다.
- 이름은 웹과 슬라이드 양쪽에서 축소했다. Unity 소개는 게임과 인터랙티브 콘텐츠 전반이며, `2D` 표기는 우주좀비의 개별 구현 사실에만 남겼다. 포트폴리오 문구에는 가운뎃점을 쓰지 않는다.
- 양쪽 웹의 `#ai-rag .ai-infographic`는 **901px 이상에서 너비 75%**, 모바일에서는 전체 너비다. `transform: scale()`로 영역 높이를 남기지 않는다. 뒤 화면과의 간격은 24px이다. 이 수정은 웹에만 적용했고 슬라이드/PDF는 별도 레이아웃을 유지한다.

슬라이드 순서를 바꾸면 목차, 빠른 이동 링크와 `.slide-no`를 함께 수정한다. 장수가 달라지면 검증 코드의 23장 기대값과 관련 문서, PDF도 갱신한다. 특정 페이지 번호를 프로젝트 스타일 선택자로 사용하지 않는다.

## 채용 사이트 이력서 갱신

2026-11-15에 잡코리아와 사람인의 이력서를 저장하고 작성완료했다. Ego의 이력서 보기 화면 두 곳에서 최종본을 확인했다. 이후 개인 프로젝트 기술과 Stone Match 운영 대시보드 경험을 포트폴리오에도 반영했다. 채용 사이트 이력서는 새로 내보내지 않았다.

- 자기소개서 제목은 `서비스의 문제를 풀고, 팀의 개발 방식까지 개선해 온 개발자`다. 소제목 없이 네 문단으로 두고, 역할에서 문제와 해결 방식으로 넘어가는 지점에 줄바꿈을 넣었다. 마무리는 팀과 해결책의 선택 이유와 검증 방법을 나누는 데 초점을 둔다.
- 두 경력기술서의 맨 위에 `[개인 프로젝트]`를 추가했다. TagDo / HabitCell, Stone Match 운영 대시보드, SyncFlow, 무장애 관광 챗봇을 결과와 출시 상태 위주로 목록에 넣고, 기존 회사 경력은 유지했다. Stone Match의 기술 표기는 [문구 검증 기록](Front_Portfolio/docs/HTML_CLAIM_AUDIT.md#stone-match-운영-대시보드-근거-2026-11-15)을 따른다.
- 잡코리아는 스킬 20개 한도에서 Supabase, GA4, Sentry를 추가했다. PostgreSQL과 Cloudflare Pages는 경력기술서에 적었다. 사람인은 이 세 기술과 SQL, PostgreSQL, Cloudflare Pages를 스킬에 추가했다.
- 사람인은 학력 두 건, 취업캠프의 Swift iOS, LLM 및 RAG, 경력 최신순 정렬을 확인했다. 재직월, 부서명과 첨부는 유지했고 TIQ는 추가하지 않았다. 사람인에 표시되는 합계는 13년 6개월이며, 포트폴리오의 13년 4개월 기준을 바꾸지 않는다.

잡코리아와 사람인에는 항목별 저장과 전체 작성완료가 별도로 있다. 수정할 때는 사용자 지시에 맞춰 그 범위까지만 진행한다. 작성완료를 요청받으면 완료 화면을 확인한 뒤 이력서 보기에서 실제 반영 내용을 대조한다.

## 실행과 검증

```sh
python3 scripts/build-site.py
python3 -m unittest discover -s tests -v
python3 -m http.server 4173 --directory _site
```

첫 명령이 `_site/`를 새로 만든다. 소스를 수정하면 다시 실행한다. 테스트는 준비된 `_site/`를 검사하므로 준비 명령보다 먼저 실행하지 않는다. 로컬 확인 주소는 [README의 실행 안내](README.md#실행)를 따른다.

테스트 4개는 메인 연결, 기존 주소의 직접 본문 제공과 슬라이드 장수, 로컬 파일/앵커, 배포 파일 구성을 확인한다. 문구의 사실성, 시각적 잘림과 PDF의 최신성까지 자동 보장하지는 않는다. 레이아웃을 바꾸면 웹의 데스크톱/모바일과 슬라이드 16:9를 별도로 확인한다. 웹 촬영과 검증은 Ego Lite 백그라운드를 우선한다.

CSS를 바꾸면 해당 HTML의 `styles.css?v=...` 또는 `portfolio-ppt.css?v=...` 버전도 갱신한다. GitHub Pages와 브라우저 캐시로 이전 화면이 남을 수 있으므로 배포 후 최신 파일과 화면을 확인한다.

## PDF 갱신

```sh
node Front_Portfolio/portfolio-ppt/scripts/render-image-pdf.mjs
node Unity_Portfolio/portfolio-ppt/scripts/render-image-pdf.mjs
```

출력은 각 `portfolio-ppt/output/`의 제출용 PDF다. 원본 문서는 `docs/`에 보존한다. 정적 사이트 준비와 GitHub Pages 워크플로는 **이미 있는 PDF를 복사할 뿐 새로 생성하지 않는다**. 슬라이드를 수정했다면 PDF 생성 후 배포 파일을 다시 준비해야 한다.

렌더러는 현재 macOS Google Chrome 경로를 사용하고, 전역 `fetch`와 `WebSocket`을 지원하는 Node.js와 Pillow를 사용할 수 있는 `python3`가 필요하다. Python은 렌더러가 실행하는 PATH의 `python3`를 사용한다.

```sh
node -p "JSON.stringify({fetch:typeof fetch,WebSocket:typeof WebSocket})"
python3 -c "from PIL import Image; print(Image.__version__)"
```

환경이 맞지 않으면 Codex의 `load_workspace_dependencies` 도구로 사용 가능한 런타임을 확인한다. PDF 생성은 기존 렌더러를 우선 사용한다. PDF는 이미지 기반이므로 페이지 수와 텍스트 추출만 확인하지 말고, 렌더한 이미지로 변경 페이지의 잘림과 겹침을 확인한다.

최종 제출용 PDF를 생성하고 검증하면 해당 버전의 사본을 아래 두 곳에서 함께 갱신한다. 검증용 임시 렌더는 복사하거나 업로드하지 않는다.

1. 프로젝트 상위 폴더: 검증된 `output/`의 PDF로 동명 사본을 교체하고 SHA-256으로 일치 여부를 확인한다.
2. Google Drive: `git config --local --get portfolio.pdfDriveFolder`로 지정 폴더를 확인한다. 폴더 안의 동명 제출용 PDF를 찾고 기존 파일의 새 버전으로 업로드해 링크를 유지한다. 갱신한 파일을 다시 확인하고 대상이나 권한을 확인할 수 없으면 보고한다. 폴더 주소는 공개 저장소에 커밋하지 않는다.
3. GitHub Pages 배포 후 공개 PDF와 Google Drive 사본의 실제 파일을 읽어 `output/` 및 상위 폴더 사본과 SHA-256을 대조한다. 일치 여부를 배포 커밋과 함께 기록한다.

### 공개 PDF와 사본 대조 기록

2026-11-15, 커밋 `15b5bc1`의 [GitHub Pages 배포](https://github.com/cheng80/web_portfolio/actions/runs/43667238071) 후 프론트엔드와 Unity PDF의 실제 파일을 대조했다. 각 버전에서 프로젝트 `output/`, 프로젝트 상위 폴더, Google Drive, 공개 사이트의 SHA-256이 모두 일치했다.
문서 커밋 `9295f3c`의 [자동 배포](https://github.com/cheng80/web_portfolio/actions/runs/43668642418) 후에도 두 공개 PDF의 SHA-256이 프로젝트 상위 폴더 및 Google Drive 사본과 각각 일치함을 재확인했다.

| 버전 | 파일 크기(바이트) | SHA-256 |
| --- | ---: | --- |
| 프론트엔드 | 5,993,064 | `172519fae7d05a6781f20fe151e87576019603361a1cf79ecd452601978ffb5a` |
| Unity | 6,012,064 | `8178d68547238c2b3207c546b561a60e2a08a2d0e0e314d4abd04aefea637a66` |

## 배포와 기존 주소

원격 저장소는 `cheng80/web_portfolio`, 배포 브랜치는 `main`이다. 공개 주소 4개와 소스의 매핑은 [README의 배포 안내](README.md#배포-주소와-소스-경로)를 따른다.

워크플로는 `scripts/build-site.py` 실행 → 테스트 → `_site/` 업로드 → GitHub Pages 배포 순서다. 프론트엔드는 기존 `/web-starter/`, `/portfolio-ppt/`에서 본문이 바로 열려야 한다. `/Front_Portfolio/...`는 공개 주소가 아니다. 메인에는 프론트엔드 웹/슬라이드와 Unity 웹/슬라이드 4개를 직접 연결한다.

[기존 배포 실행](https://github.com/cheng80/web_portfolio/actions/runs/43662160628)은 재시도 때 같은 이름의 배포 파일이 두 개 생겨 실패했다. 이제 업로드와 배포 단계 모두 `github-pages-${{ github.run_attempt }}`를 사용한다. 같은 실행을 재시도해도 `github-pages-1`, `github-pages-2`처럼 이름이 달라져 현재 시도의 파일만 배포한다.

사용자가 커밋과 푸시를 요청하면 관련 파일만 stage하고 staged diff와 검증 결과를 확인한다. 한국어로 커밋하고 푸시한 뒤 Actions 성공과 실제 주소를 확인한다. 이전 대화의 게시 요청을 이후 모든 변경의 게시 승인으로 확대하지 않는다.

## 최근 점검과 자료 보존

2026-11-15 문서 인계 정리에서는 배포 파일 생성, 테스트 4개, 안내 문서 7개의 로컬 링크 33개를 확인했다. 두 슬라이드의 공통 본문 19장과 상위 폴더의 제출용 PDF 2종도 프로젝트 파일과 대조했다. 화면 렌더링과 배포 파일 전체 대조는 이번 문서 작업에서 반복하지 않았다.

기술 스택 추가 후에는 Ego에서 웹 1440px 및 390px 화면과 두 16:9 슬라이드를 확인했다. 최신 PDF로 배포 파일을 다시 준비했고 테스트 4개가 통과했다.

프론트엔드 슬라이드 3장의 `Team / Ops` 카드와 Unity 슬라이드 3장의 `Production` 카드는 `Cloudflare Pages;`를 세미콜론까지 한 줄로 표시한다.

줄바꿈 점검에서 찾은 항목은 프론트엔드 2, 3, 17, 21장과 Unity 3, 8, 15장에 반영했다. 기술명과 요약 단어를 한 줄에 묶고, Unity 3장의 협업과 운영 및 백엔드와 데이터베이스 목록 사이에 세미콜론을 넣었다. 순서대로 탭탭의 엔진 표기는 두 버전에서 `Flutter 기반 Flame 엔진`으로 통일했다.

후속 웹 점검의 줄바꿈 수정과 두 분석 카드의 `Cloudflare Pages;`는 웹 커밋 `caee0b9`에 반영했다. 대응하는 기술 표기와 줄바꿈을 두 슬라이드에 맞추고, 변경 페이지를 렌더링해 확인한 23쪽 PDF 2종을 함께 관리한다. 상위 폴더와 Google Drive 사본도 최신본으로 교체했다.

`5064bbd` 기준의 이전 전체 점검에서 다음을 확인했다. 새 수정 후에는 영향 범위를 다시 검증한다.

- 공통 상세 슬라이드 19장과 네 산출물의 AI 사례 4개 본문, 링크와 이미지 일치.
- 프로젝트 순서, 경력 표기, 이름 축소, 설명용 이미지와 AI 하단 문구 반영.
- 웹 데스크톱/모바일의 RAG 배율과 간격 정상, 깨진 이미지와 슬라이드 밖 글자 넘침 없음.
- PDF 2종 각각 23쪽, 공통 페이지 구성 일치.
- 배포 파일 194개가 준비된 파일과 일치하고 메인 4개 연결 정상.

검증용 `_site/`, 임시 캡처와 PDF 렌더는 점검 후 정리했다. `Front_Portfolio/_archive/`는 Git에서 제외한 로컬 대화, 문구 검토와 실행 근거다. 새 clone에는 없어도 정상이며 추적 중인 근거 문서로 작업을 이어갈 수 있다. 승인된 참고 이미지와 원본 PDF는 삭제하지 않는다.

다음 작업에서 구성이나 기준이 달라지거나 미완료 항목이 남으면 이 문서의 기준 커밋, 완료 내용, 남은 작업과 실제 검증을 갱신한다. 검증하지 않은 결과를 과거 점검 기록으로 대신하지 않는다.
