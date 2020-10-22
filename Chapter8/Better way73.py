#
# 아이템 73
#
import timeit
import random

class Book:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date

def add_book(queue, book):
    queue.append(book)
    queue.sort(key=lambda x: x.due_date, reverse=True)

queue = []
add_book(queue, Book('돈키호테', '2020-06-07'))
add_book(queue, Book('프랑켄슈타인', '2020-06-05'))
add_book(queue, Book('레미제라블', '2020-06-08'))
add_book(queue, Book('전쟁과 평화', '2020-06-03'))

class NoOverdueBooks(Exception):
    pass

def next_overdue_book(queue, now):
    if queue:
        book = queue[-1]
        if book.due_date < now:
            queue.pop()
            return book

    raise NoOverdueBooks

now = '2020-06-10'
found = next_overdue_book(queue, now)
print(found.title)
found = next_overdue_book(queue, now)
print(found.title)

def return_book(queue, book):
    queue.remove(book)

queue = []
book = Book('보물섬', '2020-06-04')

add_book(queue, book)
print('반납 전:', [x.title for x in queue])

return_book(queue, book)
print('반납 후:', [x.title for x in queue])

try:
    next_overdue_book(queue, now)
except NoOverdueBooks:
    pass         # 이 문장이 실행되리라 예상함
else:
    assert False # 이 문장은 결코 실행되지 않음

#
def print_results(count, tests):
    avg_iteration = sum(tests) / len(tests)
    print(f'\n원소 수: {count:>5,} 걸린시간: {avg_iteration:.6f}초')
    return count, avg_iteration


def list_overdue_benchmark(count):
    def prepare():
        to_add = list(range(count))
        random.shuffle(to_add)
        return [], to_add

    def run(queue, to_add):
        for i in to_add:
            queue.append(i)
            queue.sort(reverse=True)

        while queue:
            queue.pop()

    tests = timeit.repeat(
        setup='queue, to_add = prepare()',
        stmt=f'run(queue, to_add)',
        globals=locals(),
        repeat=100,
        number=1)

    return print_results(count, tests)

def print_delta(before, after):
    before_count, before_time = before
    after_count, after_time = after
    growth = 1 + (after_count - before_count) / before_count
    slowdown = 1 + (after_time - before_time) / before_time
    print(f'데이터 크기 {growth:>4.1f}배, 걸린 시간 {slowdown:>4.1f}배')

baseline = list_overdue_benchmark(500)
for count in (1_000, 1_500, 2_000):
    comparison = list_overdue_benchmark(count)
    print_delta(baseline, comparison)

#
def list_return_benchmark(count):
    def prepare():
        queue = list(range(count))
        random.shuffle(queue)
        to_return = list(range(count))
        random.shuffle(to_return)
        return queue, to_return

    def run(queue, to_return):
        for i in to_return:
            queue.remove(i)

    tests = timeit.repeat(
        setup='queue, to_return = prepare()',
        stmt=f'run(queue, to_return)',
        globals=locals(),
        repeat=100,
        number=1)

    return print_results(count, tests)

baseline = list_return_benchmark(500)
for count in (1_000, 1_500, 2_000):
    comparison = list_return_benchmark(count)
    print_delta(baseline, comparison)

#
from heapq import heappush

def add_book(queue, book):
    heappush(queue, book)

queue = []
# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#add_book(queue, Book('작은 아씨들', '2020-06-05'))
#add_book(queue, Book('타임 머신', '2020-05-30'))

import functools


@functools.total_ordering
class Book:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date

    def __lt__(self, other):
        return self.due_date < other.due_date

queue = []
add_book(queue, Book('오만과 편견', '2020-06-01'))
add_book(queue, Book('타임 머신', '2020-05-30'))
add_book(queue, Book('죄와 벌', '2020-06-06'))
add_book(queue, Book('폭풍의 언덕', '2020-06-12'))

queue = [
    Book('오만과 편견', '2020-06-01'),
    Book('타임 머신', '2020-05-30'),
    Book('죄와 벌', '2020-06-06'),
    Book('폭풍의 언덕', '2020-06-12'),
]
queue.sort()

from heapq import heapify

queue = [
    Book('오만과 편견', '2020-06-01'),
    Book('타임 머신', '2020-05-30'),
    Book('죄와 벌', '2020-06-06'),
    Book('폭풍의 언덕', '2020-06-12'),
]
heapify(queue)

from heapq import heappop

def next_overdue_book(queue, now):
    if queue:
        book = queue[0]  # 만기가 가장 이른 책이 맨 앞에 있다
        if book.due_date < now:
            heappop(queue)  # 연체된 책을 제거한다
            return book

    raise NoOverdueBooks

now = '2020-06-02'

book = next_overdue_book(queue, now)
print(book.title)

book = next_overdue_book(queue, now)
print(book.title)

try:
    next_overdue_book(queue, now)
except NoOverdueBooks:
    pass              # 이 문장이 실행되리라 예상함
else:
    assert False      # 이 문장은 결코 실행되지 않음

#
def heap_overdue_benchmark(count):
    def prepare():
        to_add = list(range(count))
        random.shuffle(to_add)
        return [], to_add

    def run(queue, to_add):
        for i in to_add:
            heappush(queue, i)
        while queue:
            heappop(queue)

    tests = timeit.repeat(
        setup='queue, to_add = prepare()',
        stmt=f'run(queue, to_add)',
        globals=locals(),
        repeat=100,
        number=1)

    return print_results(count, tests)

baseline = heap_overdue_benchmark(500)
for count in (1_000, 1_500, 2_000):
    comparison = heap_overdue_benchmark(count)
    print_delta(baseline, comparison)

#
@functools.total_ordering
class Book:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date
        self.returned = False       # 새로운 필드

    def __lt__(self, other):
        return self.due_date < other.due_date

def next_overdue_book(queue, now):
    while queue:
        book = queue[0]
        if book.returned:
            heappop(queue)
            continue

        if book.due_date < now:
            heappop(queue)
            return book

        break

    raise NoOverdueBooks

def return_book(queue, book):
    book.returned = True

