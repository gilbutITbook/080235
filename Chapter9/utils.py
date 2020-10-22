#!/usr/bin/env python3.8
def to_str(data):
    if isinstance(data, str):
        return data
    elif isinstance(data, bytes):
        return data.decode('utf-8')
    else:
        raise TypeError('str이나 bytes를 전달해야 합니다, '
                        '찾은 값: %r' % data)
