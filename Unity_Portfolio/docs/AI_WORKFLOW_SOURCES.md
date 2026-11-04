# AI 활용 개발 사례 근거

사용자가 검토한 시안의 문구를 웹과 슬라이드에 반영했다. 순서는 종합 소개, 자동 플레이 검증, 밸런스 분석 도구, 카드 아트다. 문구는 Claude Opus 5.5의 high 설정으로 검토했으며 AI 활용 범위는 사용자의 개발 전반 AI 활용 진술과 아래 실제 도구를 기준으로 작성했다.

## Stone Match

원본 저장소는 `cheng80/jewelmatch`다.

- `docs/plans/PLAN-009-telemetry-foundation.md`: Codex의 작업 조정, Claude의 병렬 구현과 통합, 별도 읽기 전용 검수 기록.
- `tools/play_bot_vision.mjs`: 화면 픽셀 색 분류, 교환 탐색과 입력, 점수 안정화 확인.
- `tools/deploy_match_web.sh`: 웹 빌드, 소스맵 등록, NAS 업로드, 배포 응답 확인. 푸시 기반 CI나 자동 밸런스 최적화로 소개하지 않는다.
- 색 인식 SVG는 알고리즘을 설명하는 테스트 보드이며 실제 실행 캡처로 소개하지 않는다. 그림 안의 더미 화면 표기를 유지한다.

## Rummi Poker

원본 저장소는 `cheng80/rummipoker`이며 로컬 폴더명은 `flame_binggo_card`다.

- `tools/full_run_bot.sh`: 전투, 정산, 상점 진행과 체크포인트 재개 도구.
- 루미 포커 SVG는 보존된 실제 전투 화면에 설명 표시를 더한 이미지다. 원본 화면을 바꾸지 않았으며 실제 봇 실행 캡처로 소개하지 않는다. 그림 안의 주석 예시 표기를 유지한다.
- `tools/sim/run_balance_sim.dart`: 게임 규칙과 카드 데이터를 재사용하는 조건별 반복 실행기.
- `tools/sim/report_balance_summary_ko.py`: 결과 집계와 한국어 리포트 생성기.
- `test/tools/sim/balance_sim_test.dart`, `balance_sim_report_test.dart`, `balance_sim_ko_report_test.dart`: 입력 조건, 같은 시드 재현, 집계와 리포트 검증 코드.
- 밸런스 사례는 제작한 도구의 기능만 설명한다. 가상 통계, 제한된 신규 실행 결과, 개선 수치를 성과로 사용하지 않는다.
- `tools/imagegen/build_card_image_prompt_manifest.py`, `run_card_emblem_batch.sh`, `build_card_emblem_preview_html.py`: 카드별 프롬프트, 일괄 생성, 미리보기 도구.
- `docs/tools/card_assets/CARD_ITEM_ILLUSTRATION_GUIDE.md`: 카드 크기와 이미지 배치 지침.
- `output/imagegen/card_emblems_builtin/all/`의 생성 이미지 97개와 `all_thumb54/`의 축소본이 보존되어 있다. 전부 게임에 반영되었다고 주장하지 않는다.

## 공통 자료

`web-starter/assets/ai-workflow/`와 `portfolio-ppt/assets/ai-workflow/`에 같은 자료를 보존한다. 실제 카드 이미지와 축소본 8개, 설명용 SVG 2개, 전용 CSS가 들어 있다. 다른 버전이나 `_workspace`를 실행 시 참조하지 않는다. 각 하단에는 해당 사례의 AI 활용 범위만 표시한다.
