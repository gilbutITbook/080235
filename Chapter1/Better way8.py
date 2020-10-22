
###
### 아이템 8
###


names = ['Cecilia', '남궁민수', '毛泽东']
counts = [len(n) for n in names]
print(counts)

longest_name = None
max_count = 0

for i in range(len(names)):
    count = counts[i]
    if count > max_count:
        longest_name = names[i]
        max_count = count

print(longest_name)

longest_name = None
max_count = 0

for i, name in enumerate(names):
    count = counts[i]
    if count > max_count:
        longest_name = name
        max_count = count

print(longest_name)

longest_name = None
max_count = 0

for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count

print(longest_name)

names.append('Rosalind')
for name, count in zip(names, counts):
    print(name)

import itertools
for name, count in itertools.zip_longest(names, counts):
    print(f'{name}: {count}')

