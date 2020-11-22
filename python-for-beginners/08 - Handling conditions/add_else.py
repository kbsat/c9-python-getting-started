price = input('how much did you pay? ')
price = float(price)

if price >= 1.00:
    # $1.00 이상이면 7%의 세금을 부과합니다.
    # 들여쓰기 된 코드는 가격이 1 이상일 경우에만 실행됩니다.
    tax = .07
    print('Tax rate is: ' + str(tax))
else:
    # 그 외 모든 것은 세금을 부과하지 않습니다.
    # 들여쓰기 된 코드는 가격이 1보다 작을 경우에만 실행됩니다.
    tax = 0
    print('Tax rate is: ' + str(tax))
