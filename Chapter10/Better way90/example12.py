# 전방참조를 해결하기 위해 타입 애너테이션에 클래스 이름이 아니라 문제열 쓰기
class FirstClass:
    def __init__(self, value: 'SecondClass') -> None:
        self.value = value


class SecondClass:
    def __init__(self, value: int) -> None:
        self.value = value


second = SecondClass(5)
first = FirstClass(second)

# $ python3 -m mypy --strict example12.py도 오류가 발생하지 않고,
# 그냥 프로그램을 실행해도 오류가 발생하지 않음


