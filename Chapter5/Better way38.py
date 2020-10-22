#
# 아이템 38
#
names = ['소크라테스', '아르키메데스', '플라톤', '아리스토텔레스']
names.sort(key=len)
print(names)

def log_missing():
    print('키 추가됨')
    return 0

from collections import defaultdict
current = {'초록': 12, '파랑': 3}
increments = [
    ('빨강', 5),
    ('파랑', 17),
    ('주황', 9),
]
result = defaultdict(log_missing, current)
print('이전:', dict(result))
for key, amount in increments:
    result[key] += amount
print('이후:', dict(result))

#
def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count  # 상태가 있는 클로저
        added_count += 1
        return 0

    result = defaultdict(missing, current)
    for key, amount in increments:
        result[key] += amount

    return result, added_count

result, count = increment_with_report(current, increments)
assert count == 2

#
class CountMissing:
    def __init__(self):
        self.added = 0

    def missing(self):
        self.added += 1
        return 0

counter = CountMissing()
result = defaultdict(counter.missing, current) # 메서드 참조
for key, amount in increments:
    result[key] += amount
assert counter.added == 2

#
class BetterCountMissing:
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0


counter = BetterCountMissing()
assert counter() == 0
assert callable(counter)

#
counter = BetterCountMissing()
result = defaultdict(counter, current) # __call__에 의존함
for key, amount in increments:
    result[key] += amount
assert counter.added == 2


