#!/usr/bin/env python3.8
# using_gc.py
import gc

found_objects = gc.get_objects()
print('이전:', len(found_objects))

import waste_memory

hold_reference = waste_memory.run()

found_objects = gc.get_objects()
print('이후: ', len(found_objects))
for obj in found_objects[:3]:
    print(repr(obj)[:100])
