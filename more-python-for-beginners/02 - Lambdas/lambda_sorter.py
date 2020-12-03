# 알파벳 순서로 정렬하기
presenters = [
    {'name': 'Susan', 'age': 50},
    {'name': 'Christopher', 'age': 47}
]

presenters.sort(key=lambda item: item['name'])
print('-- alphabetically --')
print(presenters)

# 이름의 길이로 정렬하기 (짧은 것에서부터 긴 것으로)
presenters.sort(key=lambda item: len(item['name']))
print('-- length --')
print(presenters)
