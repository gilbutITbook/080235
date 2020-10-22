def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i

import time

numbers = [2139079, 1214759, 1516637, 1852285]
start = time.time()

for number in numbers:
    list(factorize(number))

end = time.time()
delta = end - start
print(f'총 {delta:.3f} 초 걸림')
