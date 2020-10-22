
#
# 아이템 29
#
stock = {
    '못': 125,
    '나사못': 35,
    '나비너트': 8,
    '와셔': 24,
}

order = ['나사못', '나비너트', '클립']

def get_batches(count, size):
    return count // size

result = {}
for name in order:
    count = stock.get(name, 0)
    batches = get_batches(count, 8)
    if batches:
        result[name] = batches

print(result)

#
found = {name: get_batches(stock.get(name, 0), 8)
         for name in order
         if get_batches(stock.get(name, 0), 8)}
print(found)

#
has_bug = {name: get_batches(stock.get(name, 0), 4)
           for name in order
           if get_batches(stock.get(name, 0), 8)}

print('예상:', found)
print('실졔: ', has_bug)

#
found = {name: batches for name in order
         if (batches := get_batches(stock.get(name, 0), 8))}

# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#result = {name: (tenth := count // 10)
#          for name, count in stock.items() if tenth > 0}

#
result = {name: tenth for name, count in stock.items()
          if (tenth := count // 10) > 0}
print(result)

#
half = [(last := count // 2) for count in stock.values()]
print(f'{half}의 마지막 원소는 {last}')

#
for count in stock.values(): # 루프 변수가 누출됨
    pass

print(f'{list(stock.values())}의 마지막 원소는 {count}')

#
half = [count // 2 for count in stock.values()]
print(half)  # 작동함
print(count) # 루프 변수가 누출되지 않기 때문에 예외가 발생함

#
stock = {
    '못': 125,
    '나사못': 35,
    '나비너트': 8,
    '와셔': 24,
}

order = ['나사못', '나비너트', '클립']

found = ((name, batches) for name in order
         if (batches := get_batches(stock.get(name, 0), 8)))
print(next(found))
print(next(found))
