
#
# 아이템 22
#
def log(message, values):
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')

log('내 숫자는 ', [1, 2])
log('안녕 ', [])

#
def log(message, *values):  # 달라진 유일한 부분
    if not values:
        print(message)
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{message}: {values_str}')

log('내 숫자는 ', [1, 2])
log('안녕 ', [])  # 훨씬 좋다

#
favorites = [7, 33, 99]
log('좋아하는 숫자는', *favorites)

#
def my_generator():
    for i in range(10):
        yield i

def my_func(*args):
    print(args)

it = my_generator()
my_func(*it)

#
def log(sequence, message, *values):
    if not values:
        print(f'{sequence} - {message}')
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{sequence} - {message}: {values_str}')

log(1, '좋아하는 숫자는', 7, 33)   # 새 코드에서 가변 인자를 사용. 문제 없음
log(1, '안녕')                   # 새 코드에서 가변 인자 없이 메시지만 사용. 문제 없음
log('좋아하는 숫자는', 7, 33)      # 예전 방식 코드는 깨짐
