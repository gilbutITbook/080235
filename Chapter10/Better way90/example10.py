# 타입 애너테이션이 없는 코드
class FirstClass:
    def __init__(self, value):
        self.value = value


class SecondClass:
    def __init__(self, value):
        self.value = value


second = SecondClass(5)
first = FirstClass(second)
