# 이 코드의 오류를 수정하고 아래 설명에 따라 테스트하세요.
# 2.00을 입력하면 "Tax rate is : 0.07" 을 출력하세요.
# 1.00을 입력하면 "Tax rate is : 0.07" 을 출력하세요.
# 0.50을 입력하면 "Tax rate is : 0" 을 출력하세요.
price = input('how much did you pay? ')

if price > 1.00:
    tax = .07
    print('Tax rate is: ' + str(tax))
else:
    tax = 0
print('Tax rate is: ' + str(tax))
