# 글을 작성하기 위해 manage.txt 파일 열기
stream = open('manage.txt', 'wt')

# 파일 스트림으로 문자열 'demo' 작성하기
stream.write('demo!')

# 파일 스트림의 시작 부분으로 돌아가기
stream.seek(0)

# 파일 스트림으로 문자열 'cool' 작성하기
stream.write('cool')

# 파일 버퍼를 위해 파일 스트림의 내용 비우기
stream.flush()

# 파일 스트림 비우고 파일 닫기
stream.close()
