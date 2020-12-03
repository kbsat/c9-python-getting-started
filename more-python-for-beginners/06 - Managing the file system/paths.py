# Python 3.6 버전 이상에서 사용가능
# 라이브러리 가져오기
from pathlib import Path

# 무엇이 현재 실행중인 디렉토리인가요?
cwd = Path.cwd()
print('\nCurrent working directory:\n' + str(cwd))

# 경로와 파일 이름을 합쳐서 전체 경로 이름 생성
new_file = Path.joinpath(cwd, 'new_file.txt')
print('\nFull path:\n' + str(new_file))

# 파일이 존재하는지 확인
print('\nDoes that file exist? ' + str(new_file.exists()) + '\n')