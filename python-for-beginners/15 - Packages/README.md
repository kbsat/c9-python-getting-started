# 패키지와 모듈

## 모듈

[모듈](https://docs.python.org/3/tutorial/modules.html)은 함수와 같은 재사용가능한 코드 블록을 파일로 저장해 놓은 것입니다. 해당 코드블록을 참조하려면 `import` 문을 사용합니다.

``` python
# 네임스페이스로 모듈 가져오기
import helpers
helpers.display('Not a warning')

# 네임스페이스 안의 모든 항목 가져오기
from helpers import *
display('Not a warning')

# 네임스페이스 안의 특정 항목 가져오기
from helpers import display
display('Not a warning')
```

## 패키지

[배포 패키지](https://packaging.python.org/glossary/#term-distribution-package)는 클래스와 함수와 같은 리소스를 담고있고 외부에 저장된 파일입니다. 여러분이 만드는 대부분의 프로그램은 하나 이상의 패키지를 사용합니다. 패키지를 가져오는 방법은 모듈을 가져오는 방법과 동일합니다. [Python Package index](https://pypi.org/)는 [pip](https://pip.pypa.io/en/stable/)를 이용해서 설치할 수 있는 패키지의 모든 목록을 담고있습니다.

## 가상 환경

[가상 환경](https://docs.python.org/3.7/tutorial/venv.html)은 독립된 폴더에 패키지를 설치할 수 있도록 합니다. 버전 관리를 더 효과적으로 만드는 방법입니다.

``` console

```
