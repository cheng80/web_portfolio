# 김택권 포트폴리오

기존 산출물을 `Front_Portfolio/`에 모아 **프론트엔드 버전**으로 보존합니다. 유니티 전반의 개발 경험을 우선하는 별도 버전은 이 정리 이후에 구성합니다.

## 현재 구조

```txt
index.html                 # 프론트엔드 웹과 슬라이드로 이동하는 저장소 안내
Front_Portfolio/
  index.html               # 프론트엔드 버전 안내
  web-starter/             # 웹 HTML/CSS, 스크린샷, 참고 JSON
  portfolio-ppt/           # 18장 슬라이드, PDF, 생성 스크립트
  assets/reference/        # 디자인 참고 자료와 Stone Match 촬영본
  docs/                    # 원본 PDF, 제작 지침, 검증 기록
  DESIGN.md                # 프론트엔드 버전 디자인 기준
  README.md                # 폴더별 수정과 실행 안내
  tmp/                     # 기존 PDF 추출 자료
  _archive/conversations/  # 이전 문구 윤문 작업 기록, Git 제외
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
- 슬라이드: http://localhost:4173/Front_Portfolio/portfolio-ppt/

PDF 갱신은 저장소 루트에서 다음 명령을 사용합니다.

```sh
node Front_Portfolio/portfolio-ppt/scripts/render-image-pdf.mjs
```

실행 조건과 수정 기준은 [프론트엔드 버전 안내](Front_Portfolio/README.md), 후속 작업 지침은 [시작 프롬프트](Front_Portfolio/docs/CODEX_START_PROMPT.md)를 확인합니다. 저장소 루트의 안내와 배포 설정은 공통으로 관리하고, 버전별 HTML/CSS와 PDF는 해당 폴더에서 관리합니다.

## 이전 작업 기록

기존 `_workspace/`의 2026-07-16 윤문 작업 2건은 `Front_Portfolio/_archive/conversations/`에 원문 그대로 옮겼습니다. 실행 시 참조하지 않는 로컬 기록이며 `.gitignore`로 제외합니다. 삭제하지 않았습니다.
