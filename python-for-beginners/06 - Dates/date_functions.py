# 현재 날짜와 시간을 얻기 위해 우리는 datetime 라이브러리를 사용해야합니다.
from datetime import datetime, timedelta
# now 함수는 현재 날짜와 시간을 datetime 객체로 반환합니다.
today = datetime.now()

print('Today is: ' + str(today))
# 일, 주 등을 날짜에서 더하거나 빼기 위해 timedelta를 이용할 수 있습니다.
one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesterday was: ' + str(yesterday))

one_week = timedelta(weeks=1)
last_week = today - one_week
print('Last week was: ' + str(last_week))
