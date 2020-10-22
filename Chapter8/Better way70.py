#
# 아이템 70
#
def insertion_sort(data):
    result = []
    for value in data:
        insert_value(result, value)
    return result

def insert_value(array, value):
    for i, existing in enumerate(array):
        if existing > value:
            array.insert(i, value)
            return
    array.append(value)

from random import randint

max_size = 10**4
data = [randint(0, max_size) for _ in range(max_size)]
test = lambda: insertion_sort(data)

from cProfile import Profile

profiler = Profile()
profiler.runcall(test)

from pstats import Stats

stats = Stats(profiler)
stats.strip_dirs()
stats.sort_stats('cumulative')   # 누적 통계
stats.print_stats()

#
def insertion_sort(data):
    result = []
    for value in data:
        insert_value(result, value)
    return result

from bisect import bisect_left

def insert_value(array, value):
    i = bisect_left(array, value)
    array.insert(i, value)

from random import randint

max_size = 10**4
data = [randint(0, max_size) for _ in range(max_size)]
test = lambda: insertion_sort(data)

from cProfile import Profile

profiler = Profile()
profiler.runcall(test)

from pstats import Stats

stats = Stats(profiler)
stats.strip_dirs()
stats.sort_stats('cumulative')   # 누적 통계
stats.print_stats()

#
def my_utility(a, b):
    c = 1
    for i in range(100):
        c += a * b

def first_func():
    for _ in range(1000):
        my_utility(4, 5)

def second_func():
    for _ in range(10):
        my_utility(1, 3)

def my_program():
    for _ in range(20):
        first_func()
        second_func()

