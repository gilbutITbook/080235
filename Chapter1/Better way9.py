###
### 아이템 9
###

for i in range(3):
    print('Loop', i)
else:
    print('Else block!')


for i in range(3):
    print('Loop', i)
    if i == 1:
        break
else:
    print('Else block!')


for x in []:
    print('이 줄은 실행되지 않음')
else:
    print('For Else block!')

while False:
    print('이 줄은 실행되지 않음')
else:
    print('While Else block!')

a = 4
b = 9
for i in range(2, min(a, b) + 1):
    print('검사 중', i)
    if a % i == 0 and b % i == 0:
        print('서로소 아님')
        break
else:
    print('서로소')


def coprime(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True

assert coprime(4, 9)
assert not coprime(3, 6)

def coprime_alternate(a, b):
    is_coprime = True
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            is_coprime = False
            break
    return is_coprime

assert coprime_alternate(4, 9)
assert not coprime_alternate(3, 6)
