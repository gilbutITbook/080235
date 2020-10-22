#
# Item 20
#
def careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

#
x, y = 1, 0
result = careful_divide(x, y)
if result is None:
    print('잘못된 입력')

#
x, y = 0, 5
result = careful_divide(x, y)
if not result:
    print('잘못된 입력') # 이 코드가 실행되는데, 사실 이 코드가 실행되면 안된다!


#
def careful_divide(a, b):
    try:
        return True, a / b
    except ZeroDivisionError:
        return False, None

#
success, result = careful_divide(x, y)
if not success:
    print('잘못된 입력')

#
_, result = careful_divide(x, y)
if not success:
    print('잘못된 입력')

#
def careful_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('잘못된 입력')

#
x, y = 5, 2
try:
    result = careful_divide(x, y)
except ValueError:
    print('잘못된 입력')
else:
    print('결과는 %.1f 입니다' % result)

#
def careful_divide(a: float, b: float) -> float:
    """a를 b로 나눈다.

    Raises:
        ValueError: b가 0이어서 나눗셈을 할 수 없을 때
    """
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('잘못된 입력')
