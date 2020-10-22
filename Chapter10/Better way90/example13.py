# from __future__ import annotations를 통해 전방참조 문제 해결하기
from __future__ import annotations


class FirstClass:
    def __init__(self, value: SecondClass) -> None:  # OK
        self.value = value


class SecondClass:
    def __init__(self, value: int) -> None:
        self.value = value


second = SecondClass(5)
first = FirstClass(second)

# $ python3 -m mypy --strict example13.py도 오류가 발생하지 않고,
# 그냥 프로그램을 실행해도 오류가 발생하지 않음
