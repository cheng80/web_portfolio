# 김택권 Unity 포트폴리오

Unity 전반의 클라이언트 개발 경험을 우선하는 정적 HTML/CSS 버전입니다. Unity 게임, 콘텐츠 제작, 모바일 출시와 라이브서비스, AR, 하드웨어 연동을 먼저 소개합니다. 최근 Flutter 게임과 앱, AI/RAG는 개발 범위를 넓힌 사례로 뒤에 배치합니다.

## 실행

저장소 루트에서 실행합니다. 패키지 설치나 빌드는 필요하지 않습니다.

```sh
python3 -m http.server 4173
```

- 버전 안내: http://localhost:4173/Unity_Portfolio/
- 웹: http://localhost:4173/Unity_Portfolio/web-starter/
- 슬라이드: http://localhost:4173/Unity_Portfolio/portfolio-ppt/

## 구조

```txt
index.html                       # Unity 버전 안내
web-starter/
  index.html                     # Unity 우선 웹
  styles.css                     # 웹 스타일
  assets/                        # 버전 전용 이미지와 아이콘
  src/data/portfolio-data.json    # 참고 데이터, HTML과 자동 동기화되지 않음
portfolio-ppt/
  index.html                     # 23장, 16:9 슬라이드
  portfolio-ppt.css              # 화면 및 인쇄 스타일
  assets/                        # 버전 전용 이미지와 아이콘
  scripts/render-image-pdf.mjs    # 기존 렌더러를 바탕으로 한 PDF 생성
  output/                        # Unity 버전 제출용 PDF

docs/                            # 원본 이력서/PDF와 내용 근거
DESIGN.md                        # 구성 및 표현 기준
```

웹은 Unity 역량, 회사 콘텐츠, 우주좀비, 장치 연동, 경력, Flutter 게임, AI 활용 개발, 앱, AI/RAG 순서입니다. 우주좀비는 2015년의 이전 작업으로 하드웨어 연동 바로 앞에 배치합니다. 슬라이드 1~8장은 표지, 요약, 역량, 목차, 그로비교육, 천재교육/천재교과서, 우주좀비, 하드웨어 연동입니다. 9~10장은 Rummi Poker와 Stone Match, 11~14장은 AI 활용 개발 사례입니다. 15~23장은 순서대로 탭탭, 앱 4종, 관광 챗봇 2장, 아카이브, 링크입니다.

## PDF 생성

저장소 루트에서 실행합니다.

```sh
node Unity_Portfolio/portfolio-ppt/scripts/render-image-pdf.mjs
```

출력은 `portfolio-ppt/output/김택권_Unity_포트폴리오_16x9.pdf`입니다. macOS의 Google Chrome, 전역 `fetch`와 `WebSocket`을 지원하는 Node.js, Python 3 및 Pillow가 필요합니다. 이미지 기반 PDF이며 편집 원본은 HTML/CSS입니다.

## 내용과 수정 기준

- 현재 총 경력은 이력서의 2026-05-30 기준인 `13년 4개월`입니다. 총 경력을 Unity 단일 기술의 경력으로 표현하지 않습니다.
- 원본 이력서: `docs/김택권_잡코리아 이력서.pdf`
- 원본 포트폴리오: `docs/김택권 포트폴리오.pdf`
- 세부 근거: `docs/CONTENT_SOURCES.md`
- 각 HTML/CSS와 이미지 폴더는 이 버전에서 독립적으로 관리합니다. 프론트엔드 버전은 `../Front_Portfolio/`에 보존합니다.
- Unity 경력과 Flutter/Flame 게임의 기술을 구분합니다. 프로젝트의 날짜, 상태, 역할, 링크는 자료로 확인된 값을 사용합니다.

## AI 활용 개발 사례

웹은 게임 섹션 다음, 슬라이드는 Stone Match 다음에 종합 소개, 자동 플레이 검증, 밸런스 분석 도구, 카드 아트 순서로 배치합니다. 제목과 본문은 편집 가능한 HTML이며, 각 하단에는 AI 활용 범위만 표시합니다. 밸런스 통계나 개선 수치는 사용하지 않습니다.

각 페이지의 `assets/ai-workflow/`는 CSS, 설명용 SVG와 실제 생성 카드 이미지를 담습니다. 웹 폴더 단독 실행과 슬라이드 PDF 생성을 위해 양쪽에 같은 자료를 보존합니다. 이미지와 내용의 근거는 `docs/AI_WORKFLOW_SOURCES.md`에 정리했습니다.
