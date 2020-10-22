# utils.py
from .models import Projectile

__all__ = ['simulate_collision']


def _dot_product(a, b):
    return a*b   # 실제 내적은 이런식으로 계산하지 않음에 유의


def simulate_collision(a, b):
    ...
    return (a,b)   # 그냥 (반환 값 타입을 맞추기 위해) 두 값을 반환
