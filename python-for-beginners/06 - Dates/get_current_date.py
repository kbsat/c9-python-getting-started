# 현재 날짜와 시간을 얻기 위해 우리는 datetime 라이브러리를 사용해야합니다.
from datetime import datetime

current_date = datetime.now()
# now 함수는 현재 날짜와 시간을 datetime 객체로 반환합니다.

# 다른 문자열과 연결시키기 위해서 datetime 객체를 문자열로 변환시켜야합니다.
print('Today is: ' + str(current_date))
