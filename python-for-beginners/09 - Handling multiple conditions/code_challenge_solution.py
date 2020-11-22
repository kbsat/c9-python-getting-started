# 이름에 따라 사람들을 다른 방으로 배정하세요.
# 당신이 작업을 마쳤다면
# Anna는 AB 방에 있어야합니다.
# Bob은 AB 방에 있어야합니다.
# Charlie는 C 방에 있어야합니다.
# Khalid Haque는 OTHER 방에 있어야합니다.
# Xin Zhao는 Z 방에 있어야합니다.
# 사용자에게 이름을 물어보세요.
name = input('What is your name? ')

# 만약 그들의 first name이 A 나 B로 시작한다면
# 그들에게 AB 방으로 이동하라고 말하세요.
first_letter = name[0:1]
if first_letter.upper() in ('A', 'B'):
    room = 'AB'
# 만약 그들의 first name이 C로 시작한다면
# 그들에게 CD 방으로 이동하라고 말하세요.
elif first_letter.upper() == 'C':
    room = 'C'
else:
    # 만약 그들의 first name이 다른 문자로 시작한다면 그들의 last name을 물어보세요.
    # 만약 그들의 last name이 Z로 시작한다면 Z 방으로 이동하라고 말하세요.
    last_name = input('what is your last name? ')
    last_name_first_letter = last_name[0:1]
    # 만약 그들의 last name이 다른 문자로 시작한다면 그들에게 OTHER 방으로 가라고 말하세요.
    if last_name_first_letter == 'Z':
        room = 'Z'
    else:
        room = 'OTHER'
print('Please go to room ' + room)
