# get_initial 함수를 만들어 이름을 받고
# 이름의 첫 글자를 대문자로 반환합니다.
# 인자:
#   name: 사람의 이름
# 리턴 값:
#   전달받은 이름의 첫 글자를 대문자로 반환
def get_initial(name):
    initial = name[0:1].upper()
    return initial


# 이름을 묻고 이니셜을 반환하는 프로그램
first_name = input('Enter your first name: ')
# get_initial 함수를 호출하여 first name의 첫 글자를 반환
first_name_initial = get_initial(first_name)

middle_name = input('Enter your middle name: ')
# get_initial 함수를 호출하여 middle name의 첫 글자를 반환
middle_name_initial = get_initial(middle_name)

last_name = input('Enter your last name: ')
# get_initial 함수를 호출하여 last name의 첫 글자를 반환
last_name_initial = get_initial(last_name)

print('Your initials are: ' + first_name_initial
      + middle_name_initial + last_name_initial)
