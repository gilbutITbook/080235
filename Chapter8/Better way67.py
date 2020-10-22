#
# 아이템 67
#

# 타임존 설정을 해야 아래 예제들이 정상 작동함
# 주의: 윈도우에서는 작동하지 않음!
import os,time
os.environ['TZ'] = 'KST-09' # -는 본초자오선 동쪽을 뜻함
time.tzset()

import time

now = 1598523184
local_tuple = time.localtime(now)
time_format = '%Y-%m-%d %H:%M:%S'
time_str = time.strftime(time_format, local_tuple)
print(time_str)

time_tuple = time.strptime(time_str, time_format)
utc_now = time.mktime(time_tuple)
print(utc_now)

parse_format = '%Y-%m-%d %H:%M:%S %Z'    # %Z는 시간대를 뜻함
depart_icn = '2020-08-27 19:13:04 KST'
time_tuple = time.strptime(depart_icn, parse_format)
time_str = time.strftime(time_format, time_tuple)
print(time_str)

arrival_sfo = '2020-08-28 04:13:04 PDT'
# 오류가 나는 부분. 오류를 보고 싶으면 커멘트를 해제할것
#time_tuple = time.strptime(arrival_sfo, time_format)

#
from datetime import datetime, timezone

now = datetime(2020, 8, 27, 10, 13, 4)      # 시간대 설정이 안된 시간을 만듦
now_utc = now.replace(tzinfo=timezone.utc)   # 시간대를 UTC로 강제 지정
now_local = now_utc.astimezone()             # UTC 시간을 디폴트 시간대로 변환
print(now_local)

time_str = '2020-08-27 19:13:04'
now = datetime.strptime(time_str, time_format)   # 시간대 설정이 안된 시간으로 문자열을 구문분석
time_tuple = now.timetuple()                     # 유닉스 시간 구조체로 변환
utc_now = time.mktime(time_tuple)                # 구조체로부터 유닉스 타임스탬프 생성
print(utc_now)

#
import pytz

arrival_sfo = '2020-08-28 04:13:04'
sfo_dt_naive = datetime.strptime(arrival_sfo, time_format)   # 시간대가 설정되지 않은 시간
eastern = pytz.timezone('US/Pacific')                        # 샌프란시스코의 시간대
sfo_dt = eastern.localize(sfo_dt_naive)                      # 시간대를 샌프란시스코 시간대로 변경
utc_dt = pytz.utc.normalize(sfo_dt.astimezone(pytz.utc))     # UTC로 변경
print(utc_dt)

korea = pytz.timezone('Asia/Seoul')
korea_dt = korea.normalize(utc_dt.astimezone(korea))
print(korea_dt)

nepal = pytz.timezone('Asia/Katmandu')
nepal_dt = nepal.normalize(utc_dt.astimezone(nepal))
print(nepal_dt)

