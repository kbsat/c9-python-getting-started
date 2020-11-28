# get_initial 함수를 만들어 이름을 받고
# 이름의 첫 글자를 대문자로 반환합니다.
# 인자:
#   name: 사람의 이름
# 리턴 값:
#   전달받은 이름의 첫 글자를 대문자로 반환
def get_initial(name):
    initial = name[0:1].upper()
    return initial


# 이름을 묻고 이니셜을 반환
first_name = input('Enter your first name: ')
middle_name = input('Enter your middle name: ')
last_name = input('Enter your last name: ')

# get_initial 함수를 호출하여 이름의 첫 글자를 반환
print('Your initials are: '
      + get_initial(first_name)
      + get_initial(middle_name)
      + get_initial(last_name))
