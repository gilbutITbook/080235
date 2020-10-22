import subprocess

# 파이썬 3.6이나 그 이전 버전에서는 제대로 작동하지 않는다.(capture_output을 사용할 수 없음)
# 윈도우에서는 echo가 없는 경우 제대로 작동하지 않을 수 있다.
result = subprocess.run(['echo', '자식프로세스가 보내는 인사!'], capture_output=True, encoding='utf-8')

result.check_returncode() # 예외가 발생하지 않으면 문제 없이 잘 종료한 것이다
print(result.stdout) #
