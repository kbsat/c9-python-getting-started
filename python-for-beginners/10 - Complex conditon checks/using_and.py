# 평균이 85점 이상이고 최저 성적이 70점 미만이 아닌 학생들을 우등생으로 뽑습니다.
gpa = float(input('What was your Grade Point Average? '))
lowest_grade = input('What was your lowest grade? ')
lowest_grade = float(lowest_grade)

if gpa >= .85 and lowest_grade >= .70:
    print('You made the honour roll')
