#
# 아이템 69
#
rate = 1.45
seconds = 3*60 + 42
cost = rate * seconds / 60
print(cost)

print(round(cost, 2))

from decimal import Decimal

rate = Decimal('1.45')
seconds = Decimal(3*60 + 42)
cost = rate * seconds / Decimal(60)
print(cost)

print(Decimal('1.45'))
print(Decimal(1.45))

print('456')
print(456)

rate = Decimal('0.05')
seconds = Decimal('5')
small_cost = rate * seconds / Decimal(60)
print(small_cost)

print(round(small_cost, 2))

from decimal import ROUND_UP
rounded = cost.quantize(Decimal('0.01'), rounding=ROUND_UP)
print(f'반올림 전: {cost} 반올림 후: {rounded}')

rounded = small_cost.quantize(Decimal('0.01'),
                              rounding=ROUND_UP)
print(f'반올림 전: {small_cost} 반올림 후: {rounded}')

