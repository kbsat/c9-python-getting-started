# calculator 함수를 만드세요.
# 함수는 세 가지 인자를 받습니다:
# first_number: 연산을 위한 숫자 값
# second_number: 연산을 위한 숫자 값
# operation: 단어 'add' 혹은 'subtract'
# 이 함수는 두 인자의 덧셈 값이나 뺄셈 값을 반환합니다.
# 전달받은 연산자를 기반으로 덧셈과 뺄셈을 알아냅니다.
#

def calculator(first_number, second_number, operation):
    if operation.upper() == 'ADD':
        return(float(first_number) + float(second_number))
    elif operation.upper() == 'SUBTRACT':
        return(float(first_number) - float(second_number))
    else:
        return('Invalid operation please specify ADD or SUBTRACT')


# 여러분의 함수에 6, 4, add 를 넣어 테스트해보세요.
# 10이 반환되어야 합니다.
#
print('Adding 6 + 4 = ' + str(calculator(6, 4, 'add')))
# 여러분의 함수에 6, 4, subtract 를 넣어 테스트해보세요.
# 2가 반환되어야 합니다.
print('Subtracting 6 - 4 = ' + str(calculator(6, 4, 'subtract')))
# 여러분의 함수에 6, 4, divide를 넣어 테스트해보세요.
# 함수에 유효하지 않은 값이 받아들여질 때는 에러 메세지를 반환하도록 합니다.
print('Dividing 6 / 4 = ' + str(calculator(6, 4, 'divide')))
