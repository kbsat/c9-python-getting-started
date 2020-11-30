# 데코레이터

[데코레이터](https://www.python.org/dev/peps/pep-0318/)는 Python의 코드 블록에 의미나 기능을 추가하는 점에서 속성과 유사합니다. 데코레이터는 주로 [Flask](http://flask.pocoo.org/)나 [Django](https://www.djangoproject.com/)와 같은 프레임워크에서 사용됩니다. Python 개발자는 대부분 데코레이터를 만드는 것보다  사용을 주로 합니다.

``` python
# Example decorator
@log(True)
def sample_function():
    print('this is a sample function')
```
