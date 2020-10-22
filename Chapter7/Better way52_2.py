import subprocess

# 윈도우에서는 sleep이 없는 경우 제대로 작동하지 않을 수 있다.
proc = subprocess.Popen(['sleep', '1'])
while proc.poll() is None:
    print('작업중...')
    # 시간이 걸리는 작업을 여기서 수행한다

print('종료 상태', proc.poll())


