# 반복문

## For 반복문

[For 반복문](https://docs.python.org/3/reference/compound_stmts.html#the-for-statement)은 배열 또는 컬렉션의 각 요소를 순서대로 가져와서 정의한 변수에 할당합니다.

``` python
names = ['Christopher', 'Susan']
for name in names:
    print(name)
```

## While 반복문

[While 반복문](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)은 조건이 참일 경우 반복해서 작업을 실행합니다.

``` python
names = ['Christopher', 'Susan']
index = 0
while index < len(names):
    name = names[index]
    print(name)
    index = index + 1
```
