x = 42
y = 0
try:
    print(x / y)
except ZeroDivisionError as e:
    # 선택적으로 e를 어딘가에 기록하세요.
    print('Sorry, something went wrong')
except:
    print('Something really went wrong')
finally:
    print('This always runs on success or failure')
