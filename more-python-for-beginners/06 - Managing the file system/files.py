from pathlib import Path
cwd = Path.cwd()

demo_file = Path(Path.joinpath(cwd, 'demo.txt'))

# 파일 이름 가져오기
print('\nfile name: ' + demo_file.name)

# 확장자 가져오기
print('\nfile suffix: ' + demo_file.suffix)

# 폴더 가져오기
print('\nfile folder: ' + demo_file.parent.name)

# 사이즈 가져오기
print('\nfile size: ' + str(demo_file.stat().st_size) + '\n')