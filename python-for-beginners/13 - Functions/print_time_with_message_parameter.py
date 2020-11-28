from datetime import datetime

# 현재 시간 및 작업 이름을 인쇄하는 함수 정의
# 함수는 다음의 인자를 받습니다 :
#   task_name: 화면에 표시할 작업의 이름


def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()


first_name = 'Susan'
# print_time() 함수를 호출하여 메세지와 현재 시간을 출력합니다.
# 완료된 작업의 이름을 전달
print_time('first name assigned')

for x in range(0, 10):
    print(x)
# print_time() 함수를 호출하여 메세지와 현재 시간을 출력합니다.
# 완료된 작업의 이름을 전달
print_time('loop completed')
