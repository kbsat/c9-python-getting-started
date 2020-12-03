# sort 메소드가 정렬할 때 사용할 presenter 필드를 모르기 때문에
# 이 코드는 에러를 반환합니다.
presenters = [
    {'name': 'Susan', 'age': 50},
    {'name': 'Christopher', 'age': 47}
]

presenters.sort()
print(presenters)
