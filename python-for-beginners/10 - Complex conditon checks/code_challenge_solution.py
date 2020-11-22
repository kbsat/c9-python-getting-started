# 하키 팀에 가입하면 유니폼 뒷면에 이름을 표시합니다.
# 하지만 유니폼은 모든 글자를 담을 수 있을만큼 크지 않을 수 있습니다.
# 사용자에게 first name을 물으세요.
first_name = input('Please enter your first name: ')
# 사용자에게 last name을 물으세요.
last_name = input('Please enter your last name: ')

# 만약 first name이 10글자 미만이고 last name이 10글자 미만이면
#       first name과 last name을 유니폼에 출력합니다.
# 만약 first name 10글자 이상이고 last name이 10글자 미만이면
#       first name의 첫 이니셜과 last name 전체를 출력합니다.
# 만약 first name 10글자 미만이고 last name이 10글자 이상이면
#       first name 전체와 last name의 첫 이니셜을 출력합니다.
# 만약 first name이 10글자 이상이고 last name 또한 10글자 이상일 때
#       last name만 출력합니다.

# first name의 길이 체크
if len(first_name) >= 10:
    long_first_name = True
else:
    long_first_name = False

# last name의 길이 체크
if len(last_name) >= 10:
    long_last_name = True
else:
    long_last_name = False

# 이름의 길이에 따라서 가능한 유니폼 이름을 조합합니다.
if long_first_name and long_last_name:
    print(last_name)
elif long_first_name:
    print(first_name[0:1] + '. ' + last_name)
elif long_last_name:
    print(first_name + ' ' + last_name[0:1] + '.')
else:
    print(first_name + ' ' + last_name)
