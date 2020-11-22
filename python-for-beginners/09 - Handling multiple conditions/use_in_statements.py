province = input("What province do you live in? ")
tax = 0
# 여러 값이 동일한 출력을 생성하는 경우
# in 연산자로 확인하려는 모든 값을 나열하여 결합할 수 있습니다.
if province in ('Alberta', 'Nunavut', 'Yukon'):
    tax = 0.05
elif province == 'Ontario':
    tax = 0.13
else:
    tax = 0.15
print(tax)
