# 네임스페이스로 모듈 가져오기
import helpers
helpers.display('Not a warning')

# 네임스페이스 안의 모든 항목 가져오기
from helpers import *
display('Not a warning')

# 네임스페이스 안의 특정 항목 가져오기
from helpers import display
display('Not a warning')