#
# 아이템 16
#
counters = {
    '품퍼니켈': 2,
    '사워도우': 1,
}

key = '밀'

if key in counters:
    count = counters[key]
else:
    count = 0

counters[key] = count + 1

try:
    count = counters[key]
except KeyError:
    count = 0

counters[key] = count + 1

count = counters.get(key, 0)
counters[key] = count + 1

if key not in counters:
    counters[key] = 0

counters[key] += 1

if key in counters:
    counters[key] += 1
else:
    counters[key] = 1

try:
    counters[key] += 1
except KeyError:
    counters[key] = 1

votes = {
    '바게트': ['철수', '순이'],
    '치아바타': ['하니', '유리'],
}
key = '브리오슈'
who = '단이'

if key in votes:
    names = votes[key]
else:
    votes[key] = names = []

names.append(who)
print(votes)

try:
    names = votes[key]
except KeyError:
    votes[key] = names = []

names.append(who)

names = votes.get(key)
if names is None:
    votes[key] = names = []

names.append(who)

if (names := votes.get(key)) is None:
    votes[key] = names = []

names.append(who)

names = votes.setdefault(key, [])
names.append(who)

data = {}
key = 'foo'
value = []
data.setdefault(key, value)
print('이전:', data)
value.append('hello')
print('이후: ', data)

count = counters.setdefault(key, 0)
counters[key] = count + 1
