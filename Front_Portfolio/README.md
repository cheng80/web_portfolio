# 김택권 프론트엔드 포트폴리오

기존 이력서와 포트폴리오 PDF를 바탕으로 만든 정적 HTML/CSS 사이트입니다. 루트 안내 페이지에서 스크롤형 웹 포트폴리오와 23장 구성의 16:9 슬라이드 포트폴리오로 이동할 수 있습니다.

## 로컬 실행

아래 상대경로와 명령은 `Front_Portfolio/`를 작업 루트로 사용합니다. 저장소 루트에서는 먼저 `cd Front_Portfolio`로 이동합니다. Python 3으로 실행하며 별도의 패키지 설치나 빌드 과정은 없습니다.

```sh
python3 -m http.server 4173
```

- 안내 페이지: http://localhost:4173/
- 웹 포트폴리오: http://localhost:4173/web-starter/
- 슬라이드 포트폴리오: http://localhost:4173/portfolio-ppt/

## 프로젝트 구조

```txt
index.html                         # 두 포트폴리오로 이동하는 안내 페이지
web-starter/
  index.html                       # 스크롤형 포트폴리오 본문
  styles.css                       # 웹 포트폴리오 스타일
  assets/                          # 스크린샷과 아이콘
  src/data/portfolio-data.json      # 참고용 데이터 초안
  package.json                     # 웹 폴더만 제공하는 serve 명령
portfolio-ppt/
  index.html                       # 23장 슬라이드 본문
  portfolio-ppt.css                # 화면 및 인쇄 스타일
  assets/                          # 슬라이드용 스크린샷과 아이콘
  scripts/render-image-pdf.mjs      # 슬라이드 이미지 기반 PDF 생성
  output/                          # 생성된 16:9 PDF
assets/reference/                  # 디자인 참고 자료, 확정 AI 시안과 촬영본
docs/                              # 원본 PDF, 제작 지침, 검증 기록
DESIGN.md                          # 디자인 및 콘텐츠 작성 기준
_archive/                          # 이전 대화, 문구 검토와 실행 근거, Git 제외
```

## 수정 방법과 자료 기준

- 페이지 문구와 링크는 각 `index.html`에서 직접 수정합니다. 스타일은 각 페이지의 CSS에서 관리합니다.
- `portfolio-data.json`은 페이지에서 불러오지 않는 참고용 데이터입니다. HTML에 자동 반영되지 않으므로 관련 내용을 함께 확인합니다.
- 웹과 슬라이드의 이미지 폴더는 별도로 관리합니다. 양쪽에서 사용하는 이미지를 바꿀 때는 각각 반영합니다.
- 원본 포트폴리오: `docs/김택권 포트폴리오.pdf`
- 이력서: `docs/김택권_잡코리아 이력서.pdf`
- 총 개발 경력은 이력서의 2026-05-30 기준인 **13년 4개월**로 통일합니다. 현재 날짜로 자동 계산하지 않습니다.
- 정보가 충돌하면 최신 이력서와 사용자가 제공한 최신 근거를 우선합니다. 세부 기준은 `docs/HTML_CLAIM_AUDIT.md`를 확인합니다.
- HTML의 문구는 편집 가능한 텍스트로 유지하고, 프로젝트 사실·수치·출시 상태·링크를 임의로 추가하지 않습니다.
- 후속 작업의 시작 지침은 `docs/CODEX_START_PROMPT.md`, 디자인 기준은 `DESIGN.md`를 사용합니다.

## PDF 갱신

슬라이드 내용을 수정한 뒤 `Front_Portfolio/`에서 실행합니다.

```sh
node portfolio-ppt/scripts/render-image-pdf.mjs
```

현재 스크립트는 macOS의 `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`, 전역 `fetch`와 `WebSocket`을 지원하는 Node.js, Python 3 및 Pillow가 필요합니다.

결과는 `portfolio-ppt/output/김택권_포트폴리오_16x9.pdf`입니다. 슬라이드를 이미지로 캡처해 만든 PDF이며, 편집 원본은 HTML/CSS입니다. PDF는 HTML 수정 시 자동 갱신되지 않습니다.

## 배포

`main` 브랜치에 push하거나 GitHub Actions에서 수동 실행하면 저장소 루트의 `scripts/build-site.py`가 배포 파일을 `_site/`에 준비하고 검증 후 배포합니다. 공개 주소는 기존 `/web-starter/`와 `/portfolio-ppt/`를 사용하며 해당 주소에서 본문이 바로 열립니다. `Front_Portfolio/`는 소스 관리용이며 배포 파일을 직접 수정하지 않습니다.

전체 포트폴리오를 배포 구조로 미리 보려면 저장소 루트에서 `python3 scripts/build-site.py`를 실행한 뒤 `python3 -m http.server 4173 --directory _site`로 확인합니다. 소스를 수정하면 준비 명령을 다시 실행합니다.

## 연락처

- 전화번호: 010-2626-2131
- 이메일: cheng80@naver.com
- GitHub: https://github.com/cheng80

## 이전 대화 기록

`_archive/conversations/2026-07-16-001/`은 슬라이드, `2026-07-16-002/`는 웹 문구 윤문 기록입니다. 입력 원문, 수정본, 검토 JSON을 보존하며 현재 실행 파일로 사용하지 않습니다. 이 폴더는 Git에서 제외합니다. 현재 내용의 기준은 각 포트폴리오의 HTML과 원본 자료입니다.

2026-11-04 문구 검토 결과는 `_archive/reviews/`, 밸런스 도구의 실제 실행 근거는 `_archive/evidence/`에 보존합니다. 확정 AI 시안 4장은 `assets/reference/ai-workflow/`에 보관하며, 작업용 미리보기와 로그, PDF 추출 임시본은 유지하지 않습니다.

## AI 활용 개발 사례

웹은 게임 섹션 다음, 슬라이드는 Stone Match 다음에 종합 소개, 자동 플레이 검증, 밸런스 분석 도구, 카드 아트 순서로 배치합니다. 제목과 본문은 편집 가능한 HTML이며, 각 하단에는 AI 활용 범위만 표시합니다. 밸런스 통계나 개선 수치는 사용하지 않습니다.

각 페이지의 `assets/ai-workflow/`는 CSS, 설명용 SVG와 실제 생성 카드 이미지를 담습니다. 웹 폴더 단독 실행과 슬라이드 PDF 생성을 위해 양쪽에 같은 자료를 보존합니다. 이미지와 내용의 근거는 `docs/AI_WORKFLOW_SOURCES.md`에 정리했습니다.
