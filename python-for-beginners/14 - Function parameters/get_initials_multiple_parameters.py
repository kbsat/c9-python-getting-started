# 이름의 첫 이니셜을 반환하는 함수를 생성하세요.
# 인자:
#   name: 사람의 이름
#   force_uppercase: 이니셜을 항상 대문자로 표시할 지 여부를 나타냅니다.
# 반환 값:
#   전달 된 이름의 첫 이니셜
def get_initial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial


# 이름을 묻고 이니셜을 반환
first_name = input('Enter your first name: ')

# get_initial 함수를 호출하여 이름의 첫 이니셜을 반환합니다.
# 항상 대문자로 이니셜을 반환합니다.
first_name_initial = get_initial(first_name, True)

print('Your initial is: ' + first_name_initial)
