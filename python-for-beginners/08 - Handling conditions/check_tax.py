# 세금 계산하기
# 1.00$가 넘는 모든 물건들은 7%의 세금이 부과됩니다.
price = input('how much did you pay? ')

# 문자열을 숫자형으로 변경하세요.
price = float(price)

# 가격이 1.00$를 넘는지 검사하세요.
if price >= 1.00:
    # 1.00$가 넘는 모든 물건들은 7%의 세금이 부과됩니다.
    tax = .07
    print('Tax rate is: ' + str(tax))
