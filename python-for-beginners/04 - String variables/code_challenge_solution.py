# 사용자에게 first_name을 입력하여 변수에 저장하도록 요청하세요.
first_name = input('What is your first name? ')
# 사용자에게 last_name을 입력하여 변수에 저장하도록 요청하세요.
last_name = input('What is your last name? ')

# full name을 출력하세요.
# 성과 이름 사이에 공백을 삽입하세요.
# 이름과 성의 첫 글자를 대문자여야합니다.
# 나머지 이름은 소문자여야합니다.
print(first_name.capitalize() + ' ' + last_name.capitalize())
