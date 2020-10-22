#!/usr/bin/env python3.8
# top_n.py
import tracemalloc

tracemalloc.start(10)                     # 스택 깊이 설정
time1 = tracemalloc.take_snapshot()       # 이전 스냅샷

import waste_memory

x = waste_memory.run() # Usage to debug
time2 = tracemalloc.take_snapshot()       # 이후 스냅샷

stats = time2.compare_to(time1, 'lineno') # 두 스냅샷을 비교
for stat in stats[:3]:
    print(stat)
