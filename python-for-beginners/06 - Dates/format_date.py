# 현재 날짜와 시간을 얻기 위해 우리는 datetime 라이브러리를 사용해야합니다.
from datetime import datetime

# now 함수는 현재 날짜와 시간을 datetime 객체로 반환합니다.
today = datetime.now()

# day, month, year, hour, minute, second 함수를 이용하세요.
# 이 함수들은 날짜의 한 부분만을 보여줍니다.
# 위 함수들은 모두 정수 타입을 반환합니다.
# 다른 문자열과 연결하기 전에 문자열로 변환해야합니다.
print('Day: ' + str(today.day))
print('Month: ' + str(today.month))
print('Year: ' + str(today.year))

print('Hour: ' + str(today.hour))
print('Minute: ' + str(today.minute))
print('Second: ' + str(today.second))
