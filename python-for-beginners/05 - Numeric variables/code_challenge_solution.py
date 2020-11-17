# 사용자에게 숫자를 입력받으세요.
first_number = input('Enter a number: ')

# 사용자에게 두번째 숫자를 입력받으세요.
second_number = input('Enter another number: ')

# 두 수를 더한 뒤 합계를 계산하세요.
answer = float(first_number) + float(second_number)

# 'first number + second number = answer'의 형식으로 출력하세요.
# 예를 들어 4와 6을 입력했다면 아래와 같이 출력됩니다.
# 4 + 6 = 10
print(first_number + ' + ' + second_number + ' = ' + str(answer))

# 소수점 이하의 자릿수를 원하지 않는다면 답을 반올림 할 수 있습니다.
print(first_number + ' + ' + second_number + ' = ' + str(round(answer)))
