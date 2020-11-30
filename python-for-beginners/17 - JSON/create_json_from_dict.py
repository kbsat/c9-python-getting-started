import json

# 딕셔너리 객체 생성
person_dict = {'first': 'Christopher', 'last': 'Harrison'}
# 필요하면 딕셔너리에 key/value 쌍 추가
person_dict['City'] = 'Seattle'

# 딕셔너리를 JSON 객체로 변환
person_json = json.dumps(person_dict)

# JSON 객체 출력
print(person_json)
