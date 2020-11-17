# 문자열 변수에 사용할 수 있는 여러 문자열 함수들이 있습니다.
sentence = 'The dog is named Sammy'

# upper 함수는 문자열 전체를 대문자로 반환합니다.
print(sentence.upper())

# lower 함수는 문자열 전체를 소문자로 반환합니다.
print(sentence.lower())

# captalize 함수는 문자열을 첫번째 단어는 대문자로 나타내고
# 나머지 단어들은 소문자로 반환합니다.
print(sentence.capitalize())

# count 함수는 특정한 문자열이 포함된 횟수를 반환합니다.
# 아래는 문자열에서 'a' 문자가 나타나는 횟수를 반환합니다.
print(sentence.count('a'))
