# pandas DataFrame 내용 검사

pandas [DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html)은 2차원 테이블 형식 데이터를 저장하기 위한 구조입니다.

## 일반적인 함수

- [head](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.head.html)는 DataFrame에서 첫 *n* 번째 행을 반환합니다.
- [tail](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.tail.html)는 DataFrame에서 마지막 *n* 번째 행을 반환합니다.
- [shape](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.shape.html)는 DataFrame의 차원을 반환합니다. (e.g. 행과 열의 개수)
- [info](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.info.html)는 열의 이름, 열의 데이터타입, non-null 값을 포함한 행의 개수 등의 DataFrame 내용의 요약을 제공합니다.