country = 'CANADA'
# 입력한 문자열을 소문자로 변환하고 이를 모두 소문자인 문자열과 비교합니다.
# 이는 대소문자를 구분하지 않습니다.
# CANADA나 Canada를 입력한다해도 여전히 일치합니다.
if country.lower() == 'canada':
    print('Hello eh')
else:
    print('Hello')
