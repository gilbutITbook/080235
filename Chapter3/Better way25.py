
#
# 아이템 25
#
def safe_division(number, divisor,
                  ignore_overflow,
                  ignore_zero_division):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

#
result = safe_division(1.0, 10**500, True, False)
print(result)

result = safe_division(1.0, 0, False, True)
print(result)

#
def safe_division_b(number, divisor,
                    ignore_overflow=False,       # 변경
                    ignore_zero_division=False): # 변경
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

result = safe_division_b(1.0, 10**500, ignore_overflow=True)
print(result)

result = safe_division_b(1.0, 0, ignore_zero_division=True)
print(result)

assert safe_division_b(1.0, 10**500, True, False) == 0

#
def safe_division_c(number, divisor, *,         # 변경
                    ignore_overflow=False,
                    ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#safe_division_c(1.0, 10**500, True, False)

result = safe_division_c(1.0, 0, ignore_zero_division=True)
assert result == float('inf')

try:
    result = safe_division_c(1.0, 0)
except ZeroDivisionError:
    pass # 예상대로 작동함

assert safe_division_c(number=2, divisor=5) == 0.4
assert safe_division_c(divisor=5, number=2) == 0.4
assert safe_division_c(2, divisor=5) == 0.4

def safe_division_c(numerator, denominator, *,    # 변경
                    ignore_overflow=False,
                    ignore_zero_division=False):
    try:
        return numerator / denominator
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#safe_division_c(number=2, divisor=5)

#
def safe_division_d(numerator, denominator, /, *, # 변경
                    ignore_overflow=False,
                    ignore_zero_division=False):
    try:
        return numerator / denominator
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

assert safe_division_d(2, 5) == 0.4

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#safe_division_d(numerator=2, denominator=5)

#
def safe_division_e(numerator, denominator, /,
                    ndigits=10, *,                 # 변경
                    ignore_overflow=False,
                    ignore_zero_division=False):
    try:
        fraction = numerator / denominator         # 변경
        return round(fraction, ndigits)            # 변경
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise

result = safe_division_e(22, 7)
print(result)

result = safe_division_e(22, 7, 5)
print(result)

result = safe_division_e(22, 7, ndigits=2)
print(result)
