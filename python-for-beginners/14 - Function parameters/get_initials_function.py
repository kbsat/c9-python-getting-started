# 이름의 첫 이니셜을 반환하는 함수를 생성하세요.
# 인자:
#   name: 사람의 이름
# 반환 값:
#   전달 된 이름의 첫 이니셜
def get_initial(name):
    initial = name[0:1].upper()
    return initial


# 이름을 묻고 이니셜을 반환
first_name = input('Enter your first name: ')

# get_initial 함수를 호출하여 이름의 첫 이니셜을 반환합니다.
first_name_initial = get_initial(first_name)

print('Your initial is: ' + first_name_initial)
