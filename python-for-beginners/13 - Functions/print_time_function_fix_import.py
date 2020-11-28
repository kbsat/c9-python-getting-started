# datetime.now()의 호출을 간단하게 만들기 위해
# datetime 라이브러리에서 datetime 클래스를 가져옵니다.
from datetime import datetime

# print_time 함수를 생성합니다.
# print_time 함수는 메세지와 현재 시간을 출력합니다.


def print_time():
    print('task completed')
    print(datetime.now())
    print()


first_name = 'Susan'
# print_time 함수를 호출하여 메세지와 현재 시간을 출력합니다.
print_time()

for x in range(0, 10):
    print(x)
# print_time 함수를 호출하여 메세지와 현재 시간을 출력합니다.
print_time()
