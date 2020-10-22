
#
# 아이템 34
#

import math

def wave(amplitude, steps):
    step_size = 2 * math.pi / steps   # 2라디안/단계 수
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        yield output

#
def transmit(output):
    if output is None:
        print(f'출력: None')
    else:
        print(f'출력: {output:>5.1f}')

def run(it):
    for output in it:
        transmit(output)

run(wave(3.0, 8))

#
def my_generator():
    received = yield 1
    print(f'받은 값 = {received}')

it = iter(my_generator())
output = next(it)  # 첫 번째 제너레이터 출력을 얻는다
print(f'출력값 = {output}')

try:
    next(it)  # 종료될 때까지 제너레이터를 실행한다
except StopIteration:
    pass

#
it = iter(my_generator())
output = it.send(None)     # 첫 번째 제너레이터 출력을 얻는다
print(f'출력값 = {output}')

try:
    it.send('안녕!')    # 값을 제너레이터에 넣는다
except StopIteration:
    pass

#
import math
def wave_modulating(steps):
    step_size = 2 * math.pi / steps
    amplitude = yield                # 초기 진폭을 받는다
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        amplitude = yield output     # 다음 진폭을 받는다

#
def run_modulating(it):
    amplitudes = [
        None, 7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    for amplitude in amplitudes:
        output = it.send(amplitude)
        transmit(output)

run_modulating(wave_modulating(12))

#
def complex_wave():
    yield from wave(7.0, 3)
    yield from wave(2.0, 4)
    yield from wave(10.0, 5)

run(complex_wave())

#
def complex_wave_modulating():
    yield from wave_modulating(3)
    yield from wave_modulating(4)
    yield from wave_modulating(5)

run_modulating(complex_wave_modulating())

#
def wave_cascading(amplitude_it, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        amplitude = next(amplitude_it) # 다음 입력 받기
        output = amplitude * fraction
        yield output

#
def complex_wave_cascading(amplitude_it):
    yield from wave_cascading(amplitude_it, 3)
    yield from wave_cascading(amplitude_it, 4)
    yield from wave_cascading(amplitude_it, 5)

#
def run_cascading():
    amplitudes = [7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    it = complex_wave_cascading(iter(amplitudes))
    for amplitude in amplitudes:
        output = next(it)
        transmit(output)

run_cascading()
