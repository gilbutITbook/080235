from typing import Optional

def get_or_default(value: Optional[int],
                   default: int) -> int:
    if value is not None:
        return value
    return value # 아이고!: "default"를 반환해야 하는데 "value"를 반환했다

found = get_or_default(3, 5)
assert found == 3

found = get_or_default(None, 5)
assert found == 5, found  # 실패함

# $ python3 -m mypy --strict example9.py 로 정적 분석 오류를 볼 수 있음
