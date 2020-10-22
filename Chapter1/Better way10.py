###
### 아이템 10
###

fresh_fruit = {
    '사과': 10,
    '바나나': 8,
    '레몬': 5,
}

def make_lemonade(count):
    n = 1
    print(f'레몬 {count*n} 개로 레모네이드 {count//n} 개를 만듭니다.')
    fresh_fruit['레몬'] -= (count * n)
    print(f'레몬이 {fresh_fruit["레몬"]} 개 남았습니다.')

def out_of_stock():
    print(f'제료가 부족합니다. 재료를 보충해 주세요.')

count = fresh_fruit.get('레몬', 0)
if count:
    make_lemonade(count)
else:
    out_of_stock()

fresh_fruit['레몬'] = 5  # 테스트를 위해 갯수 리셋
if count := fresh_fruit.get('lemon', 0):
    make_lemonade(count)
else:
    out_of_stock()

def make_cider(count):
    n = 4

    print(f'사과 {count} 개로 사과주스 {count//n} 개를 만듭니다.')
    fresh_fruit['사과'] -= (n *(count//n))
    print(f'사과가 {fresh_fruit["사과"]} 개 남았습니다.')

fresh_fruit['사과'] = 10  # 테스트를 위해 갯수 리셋

count = fresh_fruit.get('사과', 0)
if count >= 4:
    make_cider(count)
else:
    out_of_stock()


fresh_fruit['사과'] = 10  # 테스트를 위해 갯수 리셋

if (count := fresh_fruit.get('사과', 0)) >= 4:
    make_cider(count)
else:
    out_of_stock()

def slice_bananas(count):
    print(f'바나나 {count} 개를 슬라이스합니다.')
    fresh_fruit['바나나'] -=  count
    return count

class OutOfBananas(Exception):
    pass

def make_smoothies(count):
    n=2
    if count > n:
        print(f'바나나 슬라이스 {count} 개로 스무디 {count//n} 개를 만듭니다.')
        print(f'바나나가 {fresh_fruit["바나나"]} 개 남았습니다.')
    else:
        raise OutOfBananas

pieces = 0
count = fresh_fruit.get('바나나', 0)
if count >= 2:
    pieces = slice_bananas(count)

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()

fresh_fruit['바나나'] = 8  # 테스트를 위해 갯수 리셋

count = fresh_fruit.get('바나나', 0)
if count >= 2:
    pieces = slice_bananas(count)
else:
    pieces = 0

fresh_fruit['바나나'] = 8  # 테스트를 위해 갯수 리셋

pieces = 0
if (count := fresh_fruit.get('바나나', 0)) >= 2:
    pieces = slice_bananas(count)

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()

fresh_fruit['바나나'] = 8  # 테스트를 위해 갯수 리셋

if (count := fresh_fruit.get('바나나', 0)) >= 2:
    pieces = slice_bananas(count)
else:
    pieces = 0

try:
    smoothies = make_smoothies(pieces)
except OutOfBananas:
    out_of_stock()

count = fresh_fruit.get('banana', 0)

fresh_fruit['바나나'] = 8  # 테스트를 위해 갯수 리셋

if count >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
else:
    count = fresh_fruit.get('사과', 0)
    if count >= 4:
        to_enjoy = make_cider(count)
    else:
        count = fresh_fruit.get('레몬', 0)
        if count:
            to_enjoy = make_lemonade(count)
        else:
            to_enjoy = '아무것도 없음'

if (count := fresh_fruit.get('바나나', 0)) >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
elif (count := fresh_fruit.get('사과', 0)) >= 4:
    to_enjoy = make_cider(count)
elif count := fresh_fruit.get('레몬', 0):
    to_enjoy = make_lemonade(count)
else:
    to_enjoy = '아무것도 없음'

import random

def pick_fruit():
    if random.randint(1,10) > 2:   # 80% 확률로 새 과일 보충
        return {
            '사과': random.randint(0,10),
            '바나나': random.randint(0,10),
            '레몬': random.randint(0,10),
        }
    else:
        return None

def make_juice(fruit, count):
    if fruit == '사과':
        return [('사과주스', count/4)]
    elif fruit == '바나나':
        return [('바나나스무디',count/2)]
    elif fruit == '레몬':
        return [('레모네이드',count/1)]
    else:
        return []


bottles = []
fresh_fruit = pick_fruit()
while fresh_fruit:
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)
    fresh_fruit = pick_fruit()

print(bottles)

bottles = []
while True: # 무한루프
    fresh_fruit = pick_fruit()
    if not fresh_fruit: # 중간에서 끝내기
        break

    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)

print(bottles)

bottles = []
while fresh_fruit := pick_fruit():
    for fruit, count in fresh_fruit.items():
        batch = make_juice(fruit, count)
        bottles.extend(batch)

print(bottles)
