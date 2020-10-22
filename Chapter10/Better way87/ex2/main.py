import my_module
import logging

try:
    # 오류가 나야 함
    weight = my_module.determine_weight(1, -1)
except my_module.Error:
    logging.exception('예상치 못한 오류')
