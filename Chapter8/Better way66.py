#
# 아이템 66
#
import logging

def my_function():
    logging.debug('디버깅 데이터')
    logging.error('이 부분은 오류 로그')
    logging.debug('추가 디버깅 데이터')

from contextlib import contextmanager

@contextmanager
def debug_logging(level):
    logger = logging.getLogger()
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield
    finally:
        logger.setLevel(old_level)

with debug_logging(logging.DEBUG):
    print('* 내부:')
    my_function()

print('* 외부:')
my_function()

#
with open('my_output.txt', 'w') as handle:
    handle.write('데이터입니다!')

@contextmanager
def log_level(level, name):
    logger = logging.getLogger(name)
    old_level = logger.getEffectiveLevel()
    logger.setLevel(level)
    try:
        yield logger
    finally:
        logger.setLevel(old_level)

# 맨 처음 log_level을 사용해 로그를 출력하는 경우
# 메시지가 표시되지 않는 경우가 있음
# 이럴때 메인 스레드에서 우선 아래 문장을 실행하면 정상작동함
logging.basicConfig()

with log_level(logging.DEBUG, 'my-log') as logger:
    logger.debug(f'대상: {logger.name}!')
    logging.debug('이 메시지는 출력되지 않습니다')

logger = logging.getLogger('my-log')
logger.debug('디버그 메시지는 출력되지 않습니다')
logger.error('오류 메시지는 출력됩니다')

with log_level(logging.DEBUG, 'other-log') as logger:
    logger.debug(f'대상: {logger.name}!')
    logging.debug('이 메시지는 출력되지 않습니다')

