first_num = input('Enter first number ')
second_num = input('Enter second number ')
# 숫자를 포함하는 문자열 변수가 있습니다.
# 그리고 만일 문자열 변수를 숫자로 취급하고 싶다면
# 문자열 변수를 숫자 데이터 타입으로 변경해줘야합니다.
# int() 함수는 데이터 타입을 문자열에서 정수로 바꿔줍니다. e.g. 5, 8, 416, 506
print(int(first_num) + int(second_num))

# float() 함수는 데이터 타입을 문자열에서 실수형태로 바꿔줍니다. e.g. 3.14159, 89.5, 1.0
print(float(first_num) + float(second_num))
