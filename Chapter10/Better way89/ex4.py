# 키에 해당하는 단위로 돼 있는 값을
# SI단위계 단위로 바꿀 때 곱해야 하는 숫자를 저장하는 딕셔너리
CONVERSIONS = {
    'mph': 1.60934 / 3600 * 1000,  # 마일/초 -> 미터/초
    '시간': 3600,  # 시간 -> 초
    '마일': 1.60934 * 1000,  # 마일 -> 미터
    '미터': 1,  # 미터 -> 미터
    'm/s': 1,  # 미터/초 -> 미터/초
    '초': 1,  # 초 -> 초
}

def convert(value, units):
    rate = CONVERSIONS[units]
    return rate * value

def localize(value, units):
    rate = CONVERSIONS[units]
    return value / rate

import warnings
def require(name, value, default):
    if value is not None:
        return value
    warnings.warn(
        f'{name}이(가) 곧 필수가 됩니다. 코드를 변경해 주세요',
        DeprecationWarning,
        stacklevel=3)
    return default

def print_distance(speed, duration, *,
                   speed_units=None,
                   time_units=None,
                   distance_units=None):
    speed_units = require('speed_units', speed_units, 'mph')
    time_units = require('time_units', time_units, '시간')
    distance_units = require(
        'distance_units', distance_units, '마일')

    norm_speed = convert(speed, speed_units)
    norm_duration = convert(duration, time_units)
    norm_distance = norm_speed * norm_duration
    distance = localize(norm_distance, distance_units)
    print(f'{distance} {distance_units}')


import contextlib
import io

fake_stderr = io.StringIO()
with contextlib.redirect_stderr(fake_stderr):
    print_distance(1000, 3,
                   speed_units='미터',
                   time_units='초')

print(fake_stderr.getvalue())
