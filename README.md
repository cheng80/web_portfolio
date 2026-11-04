# 김택권 포트폴리오

기존 산출물은 `Front_Portfolio/`에 **프론트엔드 버전**으로 보존하고, `Unity_Portfolio/`는 **유니티 전반의 개발 경험을 우선하는 버전**으로 관리합니다. 각 버전은 웹, 슬라이드와 PDF를 제공합니다.

## 현재 구조

```txt
index.html                 # 프론트엔드 웹/슬라이드, Unity 웹/슬라이드의 4개 바로가기
Front_Portfolio/
  index.html               # 프론트엔드 버전 안내
  web-starter/             # 웹 HTML/CSS, 스크린샷, 참고 JSON
  portfolio-ppt/           # 23장 슬라이드, PDF, 생성 스크립트
  assets/reference/        # 디자인 참고 자료와 Stone Match 촬영본
  docs/                    # 원본 PDF, 제작 지침, 검증 기록
  DESIGN.md                # 프론트엔드 버전 디자인 기준
  README.md                # 폴더별 수정과 실행 안내
  tmp/                     # 기존 PDF 추출 자료
  _archive/conversations/  # 이전 문구 윤문 작업 기록, Git 제외
Unity_Portfolio/
  index.html               # Unity 버전 안내
  web-starter/             # Unity 우선 웹과 전용 이미지
  portfolio-ppt/           # 23장 슬라이드와 Unity PDF
  docs/                    # 원본 자료, 내용 근거와 작업 지침
  DESIGN.md                # Unity 버전 구성 기준
  README.md                # Unity 버전 실행 안내
web-starter/index.html     # 이전 웹 주소에서 새 위치로 이동
portfolio-ppt/index.html   # 이전 슬라이드 주소에서 새 위치로 이동
.github/workflows/         # 저장소 전체 GitHub Pages 배포
```

## 실행

저장소 루트에서 실행합니다.

```sh
python3 -m http.server 4173
```

- 저장소 안내: http://localhost:4173/
- 프론트엔드 버전: http://localhost:4173/Front_Portfolio/
- 웹: http://localhost:4173/Front_Portfolio/web-starter/
- 프론트엔드 슬라이드: http://localhost:4173/Front_Portfolio/portfolio-ppt/
- Unity 웹: http://localhost:4173/Unity_Portfolio/web-starter/
- Unity 슬라이드: http://localhost:4173/Unity_Portfolio/portfolio-ppt/

PDF 갱신은 저장소 루트에서 다음 명령을 사용합니다.

```sh
node Front_Portfolio/portfolio-ppt/scripts/render-image-pdf.mjs
node Unity_Portfolio/portfolio-ppt/scripts/render-image-pdf.mjs
```

실행 조건과 수정 기준은 [Unity 버전 안내](Unity_Portfolio/README.md), [프론트엔드 버전 안내](Front_Portfolio/README.md), 후속 작업 지침은 [Unity 시작 프롬프트](Unity_Portfolio/docs/CODEX_START_PROMPT.md)와 [프론트엔드 시작 프롬프트](Front_Portfolio/docs/CODEX_START_PROMPT.md)를 확인합니다. 저장소 루트의 안내와 배포 설정은 공통으로 관리하고, 버전별 HTML/CSS와 PDF는 해당 폴더에서 관리합니다.

## 배포 주소와 호환 경로

기본 공개 주소는 `https://cheng80.github.io/web_portfolio/`로 유지합니다. 메인은 프론트엔드 웹, 프론트엔드 슬라이드, Unity 웹, Unity 슬라이드로 직접 연결합니다.

- 프론트엔드 웹: `Front_Portfolio/web-starter/`
- 프론트엔드 슬라이드: `Front_Portfolio/portfolio-ppt/`
- Unity 웹: `Unity_Portfolio/web-starter/`
- Unity 슬라이드: `Unity_Portfolio/portfolio-ppt/`

기존 `web-starter/`와 `portfolio-ppt/` 주소는 프론트엔드 버전으로 이동하며 쿼리와 슬라이드 앵커를 유지합니다. 기존 공개 경로와 저장소 이름은 변경하지 않습니다. `main`에 반영하면 기존 GitHub Pages 워크플로가 저장소의 웹 HTML, 슬라이드, 이미지와 PDF를 함께 배포합니다.

## 이전 작업 기록

기존 `_workspace/`의 2026-07-16 윤문 작업 2건은 `Front_Portfolio/_archive/conversations/`에 원문 그대로 옮겼습니다. 실행 시 참조하지 않는 로컬 기록이며 `.gitignore`로 제외합니다. 삭제하지 않았습니다.

## 두 버전의 공통 내용

프론트엔드와 Unity 버전은 소개와 강조 순서가 다릅니다. 공통 프로젝트 본문, 출시 상태, 링크, 이미지와 AI 활용 사례 4개는 같은 최신 내용으로 유지합니다. 우주좀비 상세 사례도 양쪽에 포함하며 두 슬라이드는 각각 23장입니다.

최근 게임과 AI 사례의 순서는 Rummi Poker → Stone Match → AI 활용 4개 사례 → 순서대로 탭탭이며 웹과 슬라이드에 동일하게 적용합니다.
