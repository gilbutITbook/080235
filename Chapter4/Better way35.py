
#
# 아이템 35
#
class MyError(Exception):
    pass

def my_generator():
    yield 1
    yield 2
    yield 3

it = my_generator()
print(next(it))  # 1을 내놓음
print(next(it))  # 2를 내놓음
# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#print(it.throw(MyError('test error')))

#
def my_generator():
    yield 1
    try:
        yield 2
    except MyError:
        print('MyError 발생!')
    else:
        yield 3
    yield 4

it = my_generator()
print(next(it))  # 1을 내놓음
print(next(it))  # 2를 내놓음
print(it.throw(MyError('test error')))

#
class Reset(Exception):
    pass

def timer(period):
    current = period
    while current:
        current -= 1
        try:
            yield current
        except Reset:
            current = period

#
RESETS = [
    False, False, False, True, False, True, False,
    False, False, False, False, False, False, False]

def check_for_reset():
    # 외부 이벤트를 폴링한다
    return RESETS.pop(0)

def announce(remaining):
    print(f'{remaining} 틱 남음')

def run():
    it = timer(4)
    while True:
        try:
            if check_for_reset():
                current = it.throw(Reset())
            else:
                current = next(it)
        except StopIteration:
            break
        else:
            announce(current)

#
class Timer:
    def __init__(self, period):
        self.current = period
        self.period = period

    def reset(self):
        self.current = self.period

    def __iter__(self):
        while self.current:
            self.current -= 1
            yield self.current

#
def run():
    timer = Timer(4)
    for current in timer:
        if check_for_reset():
            timer.reset()
        announce(current)

run()
