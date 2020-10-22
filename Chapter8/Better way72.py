#
# 아이템 72
#
data = list(range(10**5))
index = data.index(91234)
assert index == 91234

def find_closest(sequence, goal):
    for index, value in enumerate(sequence):
        if goal < value:
            return index
    raise ValueError(f'범위를 벗어남: {goal}')

index = find_closest(data, 91234.56)
assert index == 91235

from bisect import bisect_left

index = bisect_left(data, 91234) # 정확히 일치
assert index == 91234

index = bisect_left(data, 91234.56) # 근접한 값과 일치
assert index == 91235

index = bisect_left(data, 91234.23) # 근접한 값과 일치(찾는 값 이상의 값 중 근접한 값을 찾음)
assert index == 91235

import random
import timeit

size = 10 ** 5
iterations = 1000

data = list(range(size))
to_lookup = [random.randint(0, size)
             for _ in range(iterations)]

def run_linear(data, to_lookup):
    for index in to_lookup:
        data.index(index)

def run_bisect(data, to_lookup):
    for index in to_lookup:
        bisect_left(data, index)

baseline = timeit.timeit(
    stmt='run_linear(data, to_lookup)',
    globals=globals(),
    number=10)
print(f'선형 검색: {baseline:.6f}초')

comparison = timeit.timeit(
    stmt='run_bisect(data, to_lookup)',
    globals=globals(),
    number=10)
print(f'이진 검색: {comparison:.6f}초')

slowdown = 1 + ((baseline - comparison) / comparison)
print(f'선형 검색이 {slowdown:.1f}배 더 걸림')

