try:
	stream = open('output.txt', 'wt')
	stream.write('Lorem ipsum dolar')
finally:
	stream.close() # 이것은 매우 중요합니다!!

# with open('output.txt', 'wt') as stream:
# 	stream.write('Lorem ipsum dolar')
