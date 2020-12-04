# 누락된 값의 행 및 중복 처리하기

기계 학습을 위한 데이터를 준비 할 때 중복 행을 제거해야하며 누락 된 값이있는 행을 삭제해야 할 수 있습니다.

## 일반적인 함수

- [dropna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html) 는 누락된 값의 행을 지웁니다.
- [duplicated](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.duplicated.html) 는 기존 행에 중복되는 행인지 확인한 후 True나 False의 값을 반환합니다.
- [drop_duplicates](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html)는 중복 행을 지운 DataFrame을 반환합니다.

## Microsoft 학습 자료

[Microsoft Learn](https://learn.microsoft.com/?WT.mc_id=python-c9-niner)에서 관련 튜토리얼을 찾아보세요.

- [Python과 Azure Notebooks을 이용한 기계 학습 입문](https://docs.microsoft.com/learn/paths/intro-to-ml-with-python/?WT.mc_id=python-c9-niner)
