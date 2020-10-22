#ex6.py
import warnings
try:
    warnings.warn('이 사용법은 향후 금지될 예정입니다',
                  DeprecationWarning)
except DeprecationWarning:
    print("DeprecationWarning이 예외로 발생")
    pass # 예외가 발생하리라 예상함
