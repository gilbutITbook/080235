class Counter:
    def __init__(self) -> None:
        self.value: int = 0  # 필드/변수 애너테이션

    def add(self, offset: int) -> None:
        value += offset      # 아이고! "self."를 안 씀

    def get(self) -> int:
        self.value           # 아이고! "return"을 안 씀

counter = Counter()
counter.add(5)
counter.add(3)
assert counter.get() == 8

# python3 -m mypy --strict example5.py 하면 정적 검사 오류를 볼 수 있음