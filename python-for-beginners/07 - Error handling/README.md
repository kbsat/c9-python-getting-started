# 에러 처리하기

Python에서 에러를 처리하는 것은 [try/except/finally](https://docs.python.org/3.7/reference/compound_stmts.html#except)을 이용하여 관리됩니다.

Python에는 많은 [내장된 예외들](https://docs.python.org/3.7/library/exceptions.html)이 있습니다. `except` 구문을 만들 때 [계층 구조](https://docs.python.org/3.7/library/exceptions.html#exception-hierarchy)에 따라 가장 구체적인 것부터 가장 일반적인 것까지 생성해야합니다.
