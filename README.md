# 김택권 포트폴리오

기존 산출물은 `Front_Portfolio/`에 **프론트엔드 버전**으로 보존하고, `Unity_Portfolio/`는 **유니티 전반의 개발 경험을 우선하는 버전**으로 관리합니다. 각 버전은 웹, 슬라이드와 PDF를 제공합니다.

## 현재 구조

```txt
index.html                 # 프론트엔드 웹/슬라이드, Unity 웹/슬라이드의 4개 바로가기
Front_Portfolio/
  index.html               # 프론트엔드 버전 안내
  web-starter/             # 웹 HTML/CSS, 스크린샷, 참고 JSON
  portfolio-ppt/           # 23장 슬라이드, PDF, 생성 스크립트
  assets/reference/        # 디자인 참고 자료, 확정 AI 시안과 Stone Match 촬영본
  docs/                    # 원본 PDF, 제작 지침, 검증 기록
  DESIGN.md                # 프론트엔드 버전 디자인 기준
  README.md                # 폴더별 수정과 실행 안내
  _archive/                # 이전 대화, 문구 검토와 실행 근거, Git 제외
Unity_Portfolio/
  index.html               # Unity 버전 안내
  web-starter/             # Unity 우선 웹과 전용 이미지
  portfolio-ppt/           # 23장 슬라이드와 Unity PDF
  docs/                    # 원본 자료, 내용 근거와 작업 지침
  DESIGN.md                # Unity 버전 구성 기준
  README.md                # Unity 버전 실행 안내
scripts/build-site.py      # 소스를 공개 경로에 맞춰 _site/로 복사
tests/test_site_build.py   # 공개 경로, 파일과 앵커 검증
_site/                    # 배포 파일과 로컬 미리보기, Git 제외
.github/workflows/         # _site/만 GitHub Pages 배포
```

## 실행

저장소 루트에서 배포 파일을 준비한 뒤 실행합니다. 소스를 수정하면 준비 명령을 다시 실행합니다.

```sh
python3 scripts/build-site.py
python3 -m http.server 4173 --directory _site
```

- 저장소 안내: http://localhost:4173/
- 프론트엔드 웹: http://localhost:4173/web-starter/
- 프론트엔드 슬라이드: http://localhost:4173/portfolio-ppt/
- Unity 웹: http://localhost:4173/Unity_Portfolio/web-starter/
- Unity 슬라이드: http://localhost:4173/Unity_Portfolio/portfolio-ppt/

PDF 갱신은 저장소 루트에서 다음 명령을 사용합니다.

```sh
node Front_Portfolio/portfolio-ppt/scripts/render-image-pdf.mjs
node Unity_Portfolio/portfolio-ppt/scripts/render-image-pdf.mjs
```

실행 조건과 수정 기준은 [Unity 버전 안내](Unity_Portfolio/README.md), [프론트엔드 버전 안내](Front_Portfolio/README.md), 후속 작업 지침은 [Unity 시작 프롬프트](Unity_Portfolio/docs/CODEX_START_PROMPT.md)와 [프론트엔드 시작 프롬프트](Front_Portfolio/docs/CODEX_START_PROMPT.md)를 확인합니다. 저장소 루트의 안내와 배포 설정은 공통으로 관리하고, 버전별 HTML/CSS와 PDF는 해당 폴더에서 관리합니다.

## 배포 주소와 소스 경로

기본 공개 주소는 `https://cheng80.github.io/web_portfolio/`로 유지합니다. 메인은 프론트엔드 웹, 프론트엔드 슬라이드, Unity 웹, Unity 슬라이드로 직접 연결합니다.

- 프론트엔드 웹: `web-starter/`
- 프론트엔드 슬라이드: `portfolio-ppt/`
- Unity 웹: `Unity_Portfolio/web-starter/`
- Unity 슬라이드: `Unity_Portfolio/portfolio-ppt/`

`Front_Portfolio/`는 소스 관리용 폴더입니다. 배포 준비 스크립트가 이 폴더의 웹과 슬라이드를 `_site/web-starter/`, `_site/portfolio-ppt/`로 복사하므로 기존 주소에서 본문이 바로 열립니다. 주소 이동용 HTML은 사용하지 않습니다. Unity 버전은 기존 `Unity_Portfolio/` 공개 경로를 유지합니다.

`main`에 반영하면 GitHub Pages 워크플로가 배포 파일을 준비하고 검증한 뒤 `_site/`만 배포합니다. 웹과 슬라이드의 HTML/CSS, 이미지와 제출용 PDF가 포함되며 원본 문서와 제작용 파일은 소스 폴더에 보존합니다. `_site/`는 자동 생성물이므로 직접 수정하지 않습니다.

배포 전 검증은 다음 명령으로 실행합니다.

```sh
python3 scripts/build-site.py
python3 -m unittest discover -s tests -v
```

## 이전 작업 기록

이전 윤문 대화는 `Front_Portfolio/_archive/conversations/`, 문구 검토 결과는 `Front_Portfolio/_archive/reviews/`, 밸런스 도구의 실제 실행 근거는 `Front_Portfolio/_archive/evidence/`에 보존합니다. 실행 시 참조하지 않는 로컬 기록이며 `.gitignore`로 제외합니다. 확정 AI 시안 4장은 `Front_Portfolio/assets/reference/ai-workflow/`에서 관리합니다.

작업용 `_workspace/`, 브라우저 검증 캡처와 로그, PDF 추출 임시본과 사용하지 않는 중간 이미지는 정리했습니다. 원본 PDF, 최종 웹과 슬라이드, 제출용 PDF와 생성 스크립트는 유지합니다.

## 두 버전의 공통 내용

프론트엔드와 Unity 버전은 소개와 강조 순서가 다릅니다. 공통 프로젝트 본문, 출시 상태, 링크, 이미지와 AI 활용 사례 4개는 같은 최신 내용으로 유지합니다. 우주좀비 상세 사례도 양쪽에 포함하며 두 슬라이드는 각각 23장입니다.

최근 게임과 AI 사례의 순서는 Rummi Poker → Stone Match → AI 활용 4개 사례 → 순서대로 탭탭이며 웹과 슬라이드에 동일하게 적용합니다.
