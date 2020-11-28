from datetime import datetime

# 우리가 다른 메세지를 출력하기를 원한다면
# 우리는 함수를 재사용할 수 있을까?
first_name = 'Susan'
print('first name assigned')
print(datetime.now())
print()

for x in range(0, 10):
    print(x)
print('loop completed')
print(datetime.now())
print()
