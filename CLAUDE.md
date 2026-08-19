# Project Guidelines

## Tech Stack
- Python 3, Pytest

## Harness Rules
1. 코드를 작성하기 전에 반드시 `pytest`로 실행할 수 있는 테스트 파일(`test_*.py`)을 먼저 작성하라.
2. 테스트 코드는 정상적인 케이스뿐만 아니라 결측치(None)나 빈 리스트가 들어오는 엣지 케이스를 반드시 포함하라.
3. 테스트 작성 후 `pytest`를 실행하여 의도적으로 에러(Red)가 발생하는지 확인하라.
4. 실패를 확인한 후, 본 코드를 작성하여 테스트를 모두 통과(Green)시켜라.