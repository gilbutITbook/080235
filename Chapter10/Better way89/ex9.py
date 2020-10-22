import warnings
import logging
import io


def require(name, value, default):
    if value is not None:
        return value
    warnings.warn(
        f'{name}이(가) 곧 필수가 됩니다. 코드를 변경해 주세요',
        DeprecationWarning)
    return default


with warnings.catch_warnings(record=True) as found_warnings:
    found = require('my_arg', None, 'fake units')
    expected = 'fake units'
    assert found == expected

assert len(found_warnings) == 1
single_warning = found_warnings[0]
assert str(single_warning.message) == (
    'my_arg이(가) 곧 필수가 됩니다. 코드를 변경해 주세요')
assert single_warning.category == DeprecationWarning
