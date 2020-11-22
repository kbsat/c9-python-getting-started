country = input('Enter the name of your home country: ')
if country == 'canada':
    # 문자열 비교는 대소문자를 구분합니다.
    # 만약 당신이 CANADA와 Canada를 입력했다면 둘은 다른 것으로 취급합니다.
    print('So you must like hockey!')
else:
    print('You are not from Canada')
