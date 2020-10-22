# NegativeDensityError를 정의한 모듈의 이름을 편의상 my_module2로 바꿈.
import my_module2
import logging


try:
    #
    weight = my_module2.determine_weight(1, -1)
except my_module2.NegativeDensityError as exc:
    raise ValueError('밀도로 음수가 아닌 값을 제공해야 합니다') from exc
except my_module2.InvalidDensityError:
    weight = 0
except my_module2.Error:
    logging.exception('호출 코드에 버그가 있음')
except Exception:
    logging.exception('API 코드에 버그가 있음!')
    raise # 예외를 호출자쪽으로 다시 발생시킴
