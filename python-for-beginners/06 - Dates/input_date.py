# datetime, timedelta 모듈을 가져옵니다.
from datetime import datetime, timedelta

# 사용자에게 날짜를 물을때 정해진 date 형식을 알려야합니다.
birthday = input('When is your birthday (dd/mm/yyyy)? ')

# date 값을 가지고 있는 문자열을 date 객체로 변환시킬 때
# 반드시 예상되는 date 형식을 지정해야합니다.
# date가 예상되는 형식이 아닐 경우 Python은 예외를 일으킵니다.
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')

print('Birthday: ' + str(birthday_date))

# 문자열에서 date 객체로 변환했기 때문에
# 객체를 이용하여 timedelta와 같은 date,time 함수들을 사용할 수 있습니다.
one_day = timedelta(days=1)
birthday_eve = birthday_date - one_day
print('Day before birthday: ' + str(birthday_eve))
