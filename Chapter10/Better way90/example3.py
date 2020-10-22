class Counter:
    # 일부러 타입 애너테이션을 안 붙임
    def __init__(self):
        self.value = 0

    # 일부러 타입 애너테이션을 안 붙임
    def add(self, offset):
        value += offset

    def get(self) -> int:
        self.value

# add 호출시 UnboundLocalError 발생
counter = Counter()
counter.add(5)
