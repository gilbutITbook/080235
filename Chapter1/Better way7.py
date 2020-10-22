###
### 아이템 7
###

from random import randint

random_bits = 0
for i in range(32):
    if randint(0, 1):
        random_bits |= 1 << i

print(bin(random_bits))

flavor_list = ['바닐라', '초콜릿', '피칸', '딸기']
for flavor in flavor_list:
    print(f'{flavor} 맛있어요.')

for i in range(len(flavor_list)):
    flavor = flavor_list[i]
    print(f'{i + 1}: {flavor}')

it = enumerate(flavor_list)
print(next(it))
print(next(it))

for i, flavor in enumerate(flavor_list):
    print(f'{i + 1}: {flavor}')

for i, flavor in enumerate(flavor_list, 1):
    print(f'{i}: {flavor}')
