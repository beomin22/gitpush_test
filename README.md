# first_git_project

숫자 리스트의 평균과 최댓값을 구하는 간단한 유틸리티입니다.

## 사용법

```python
from math_util import average

average([1, 2, 3, 4, 5])  # 3.0
```

`numbers`가 빈 리스트이거나 `None`이면 `ValueError`를 발생시킵니다.

```python
from list_util import find_max

find_max([1, 5, 3])  # 5
```

`numbers`가 빈 리스트이거나 `None`이면 `ValueError`를 발생시킵니다.

## 테스트

이 프로젝트는 TDD(테스트 주도 개발) 방식으로 작성되었습니다.

```bash
pytest test_math_util.py -v
pytest test_list_util.py -v
```
