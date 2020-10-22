# my_module.py
class Error(Exception):
    """이 모듈에서 발생할 모든 예외의 상위 클래스."""


class InvalidDensityError(Error):
    """밀도 값이 잘못된 경우."""


class InvalidVolumeError(Error):
    """부피 값이 잘못된 경우."""


def determine_weight(volume, density):
    if density < 0:
        raise InvalidDensityError('밀도는 0보다 커야 합니다')
    if volume < 0:
        raise InvalidVolumeError('부피는 0보다 커야 합니다')
    if volume == 0:
        density / volume
