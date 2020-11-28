# 함수 매개변수

함수를 사용하면 반복되는 코드를 가져와 필요할 때 호출 할 수 있는 모듈로 이동할 수 있습니다. 함수는 `def` 키워드로 정의되며 코드에서 함수가 호출되기 전에 선언되어야합니다. 함수는 하나 이상의 매개 변수를 허용하고 값을 반환할 수 있습니다.

- [함수](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

```python
def function_name(parameter):
    # 실행할 코드
    return value
```

매개변수에 [default 값](https://docs.python.org/3/tutorial/controlflow.html#default-argument-values)을 할당하여 함수가 호출될 때 선택적으로 만들 수 있습니다.

```python
def function_name(parameter=default):
    # 실행할 코드
    return value
```

함수를 호출 할 때 위치 또는 [이름 표기법](https://docs.python.org/3/tutorial/controlflow.html#keyword-arguments)을 사용하여 매개 변수의 값을 지정할 수 있습니다.

```python
def function_name(parameter1, parameter2):
    # 실행할 코드
    return value

# 위치 표기법은 매개 변수가 선언된 것과 동일한 순서로 인자를 전달합니다.
result = function_name(value1,value2)

# 이름 표기법
result = function_name(parameter1=value1, parameter2=value2)
```
