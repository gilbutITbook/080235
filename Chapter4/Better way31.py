
#
# 아이템 31
#
def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

#
visits = [15, 35, 80]
percentages = normalize(visits)
print(percentages)
assert sum(percentages) == 100.0

#
def read_visits(data_path):
    with open(data_path) as f:
        for line in f:
            yield int(line)

#
it = read_visits('my_numbers.txt')
percentages = normalize(it)
print(percentages)

#
it = read_visits('my_numbers.txt')
print(list(it))
print(list(it)) # 이미 모든 원소를 다 소진했다

#
def normalize_copy(numbers):
    numbers_copy = list(numbers) # 이터레이터 복사
    total = sum(numbers_copy)
    result = []
    for value in numbers_copy:
        percent = 100 * value / total
        result.append(percent)
    return result

#
it = read_visits('my_numbers.txt')
percentages = normalize_copy(it)
print(percentages)
assert sum(percentages) == 100.0

#
def normalize_func(get_iter):
    total = sum(get_iter())  # 새 이터레이터
    result = []
    for value in get_iter(): # 새 이터레이터
        percent = 100 * value / total
        result.append(percent)
    return result

#
path = 'my_numbers.txt'
percentages = normalize_func(lambda: read_visits(path))
print(percentages)
assert sum(percentages) == 100.0

#
class ReadVisits:
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)

#
visits = ReadVisits(path)
percentages = normalize(visits)
print(percentages)
assert sum(percentages) == 100.0

#
def normalize_defensive(numbers):
    if iter(numbers) is numbers: # 이터레이터 -- 나쁨!
        raise TypeError('컨테이너를 제공해야 합니다')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

#
from collections.abc import Iterator

def normalize_defensive(numbers):
    if isinstance(numbers, Iterator): # 반복 가능한 이터레이터인지 검사하는 다른 방법
        raise TypeError('컨테이너를 제공해야 합니다')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

#
visits = [15, 35, 80]
percentages = normalize_defensive(visits)
assert sum(percentages) == 100.0

visits = ReadVisits(path)
percentages = normalize_defensive(visits)
assert sum(percentages) == 100.0

#
visits = [15, 35, 80]
it = iter(visits)
# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#normalize_defensive(it)
