# 전방참조 문제
class FirstClass:
    def __init__(self, value: SecondClass) -> None:
        self.value = value


class SecondClass:
    def __init__(self, value: int) -> None:
        self.value = value


second = SecondClass(5)
first = FirstClass(second)

# $ python3 -m mypy --strict example11.py을 하면
# 정적 분석으로는 오류를 볼 수 없음
# 하지만 실행하면 3번째 줄의 SecondClass가 미정의 상태라서 오류 발생