import subprocess

# 윈도우에서는 sleep이 없으면 제대로 작동하지 않을 수 있다.
proc = subprocess.Popen(['sleep', '10'])
try:
    proc.communicate(timeout=0.1)
except subprocess.TimeoutExpired:
    proc.terminate()
    proc.wait()

print('종료 상태', proc.poll())
