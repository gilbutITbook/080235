# 제네릭 타입 애너테이션이 있는 코드
from typing import Callable, List, TypeVar

Value = TypeVar('Value')
Func = Callable[[Value, Value], Value]

def combine(func: Func[Value], values: List[Value]) -> Value:
    assert len(values) > 0
    result = values[0]
    for next_value in values[1:]:
        result = func(result, next_value)
    return result

Real = TypeVar('Real', int, float)

def add(x: Real, y: Real) -> Real:
    return x + y

inputs = [1, 2, 3, 4j]  # 아이고!: 복소수를 넣었다
result = combine(add, inputs)
assert result == 10

# $ python3 -m mypy --strict example7.py 로 정적 분석 오류를 볼 수 있음