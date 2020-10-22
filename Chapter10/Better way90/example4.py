class Counter:
    # 일부러 타입 애너테이션을 안 붙임
    def __init__(self):
        self.value = 0

    # 일부러 타입 애너테이션을 안 붙임
    def add(self, offset):
        value += offset

    def get(self) -> int:
        self.value

# get 호출시 AssertionError 발생
counter = Counter()
found = counter.get()
assert found == 0, found
