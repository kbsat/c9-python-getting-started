from pathlib import Path
cwd = Path.cwd()

# 부모 디렉토리 가져오기
parent = cwd.parent

# 디렉토리인지 확인하기
print('\nIs this a directory? ' + str(parent.is_dir()))

# 파일인지 확인하기
print('\nIs this a file? ' + str(parent.is_file()))

# 자식 디렉토리 나열
print('\n-----directory contents-----')
for child in parent.iterdir():
    if child.is_dir():
        print(child)
