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

# get_initial을 호출하여 이름의 첫 글자를 반환합니다.
# 이름 표기법을 이용하면 순서에 관계없이 매개 변수를 지정할 수 있습니다.
first_name_initial = get_initial(force_uppercase=True,
                                 name=first_name)

print('Your initial is: ' + first_name_initial)
