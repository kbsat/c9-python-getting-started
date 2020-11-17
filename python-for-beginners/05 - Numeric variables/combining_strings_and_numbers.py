days_in_feb = 28

# print 함수에는 숫자 변수와 문자열 변수 모두 들어올 수 있습니다.
print(days_in_feb)

# + 연산자는 두 개의 수를 더하기도 하고 두 개의 문자열을 연결하기도 합니다.
# 만약 하나의 문자열과 하나의 수를 주어진다면 무엇을 해야할지 모릅니다.
# 따라서 다음 코드는 에러를 일으키게 됩니다.
print(days_in_feb + ' days in February')

# 값을 표시하려면 숫자를 문자열로 변환해야합니다.
# 다음 코드는 작동하게됩니다.
print(str(days_in_feb) + ' days in February')
