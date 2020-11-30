import json

# 딕셔너리 객체 생성
person_dict = {'first': 'Christopher', 'last': 'Harrison'}
# 필요하면 딕셔너리에 key/value 쌍 추가
person_dict['City'] = 'Seattle'

# 직원 딕셔너리 생성
# 직원 딕셔너리에 program manager 위치에 사람을 직원으로 배정
staff_dict = {}
staff_dict['Program Manager'] = person_dict
# 딕셔너리를 JSON 객체로 변환
staff_json = json.dumps(staff_dict)

# JSON 객체 출력
print(staff_json)
