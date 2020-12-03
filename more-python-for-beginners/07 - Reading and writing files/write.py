# 쓰기를 위한 파일로 output.txt 열기
stream = open('output.txt', 'wt')

print('\nCan I write to this file? ' + str(stream.writable()) + '\n')

stream.write('H') # 한 문자열 쓰기
stream.writelines(['ello',' ','world']) # 하나 이상의 문자열 쓰기
stream.write('\n') # 새로운 줄 쓰기

names = ['Susan','Christopher']
stream.writelines(names)

# 리스트의 항목 사이에 새 줄을 삽입하는 간단한 방법
stream.write('\n')  # 새로운 줄 쓰기
stream.writelines('\n'.join(names)) 
stream.close() # 스트림을 비우고 닫기
