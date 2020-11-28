# 코드가 진행되는 동안 발생될 수 있는 에러를 다루는 함수를 만듭니다.
# 함수를 통해 사용자에게 메세지를 표시하며 지원 팀이 오류를 기록하여 디버깅에 도움이됩니다.
#
# 인자:
#   error_code: 각 오류 유형에 할당된 고유한 에러 코드: 예) 45는 데이터 유형 변환 에러입니다.
#   error_severity: 0 - 일어나서는 안될 치명적인 오류
#                   1 - 계속 진행할 수 없는 심각한 오류
#                   2 - 계속 수행될 수 있지만 레코드에 정보가 누락될 위험이 있는 경고 코드
#   log_to_db: 이 오류가 데이터베이스에 기록되어야하는지에 대한 여부
#   error_message: 사용자에게 표시하고 데이터베이스에 쓸 에러 메세지
#   source_module: 오류를 발생시킨 Python 모듈의 이름

def error_logger(error_code, error_severity, log_to_db, error_message, source_module):
    print('oh no error: ' + error_message)
    # 오류를 데이터베이스나 파일에 기록하는 코드를 상상해보세요.


first_number = 10
second_number = 5
if first_number > second_number:
    # 이 함수 호출 할 때 보면 매우 혼랍스럽습니다.
    # 이해하기 위해서는 error_logger의 함수의 정의를 살펴봐야합니다.
    error_logger(45, 1, True, 'Second number greater than first',
                 'adding_method')


if first_number > second_number:
    # 내가 전달한 값이 어떤 함수 매개변수에 매칭되는지 확인 할 수 있기 때문에
    # 함수 호출 할 때 이해하기 더 쉽습니다.
    error_logger(error_code=45,
                 error_severity=1,
                 log_to_db=True,
                 error_message='Second number greater than first',
                 source_module='adding_method')
