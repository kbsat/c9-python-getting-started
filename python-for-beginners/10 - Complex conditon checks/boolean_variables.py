# 우등생의 조건을 만족하는지 검사합니다.
gpa = float(input('What was your Grade Point Average? '))
lowest_grade = float(input('What was your lowest grade? '))

# Boolean 변수는 True/False의 값을 가질 수 있습니다.
if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False

# 학생이 우등생인지 확인을 해야할 때
# 코드에서 미리 설정해둔 부울 변수를 확인하면 됩니다.
if honour_roll:
    print('You made honour roll')
