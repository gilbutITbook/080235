import my_module
import logging

try:
    # API 코드 버그로 인한 오류가 나야 함
    weight = my_module.determine_weight(0, 1)
except my_module.InvalidDensityError:
    weight = 0
except my_module.Error:
    logging.exception('호출 코드에 버그가 있음')
except Exception:
    logging.exception('API 코드에 버그가 있음!')
    raise # 예외를 호출자쪽으로 다시 발생시킴
