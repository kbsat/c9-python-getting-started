# 계산을 통한 모델의 정확도 평가

값들을 직접 다루는 것은 모델을 테스트하기 위한 좋은 방법이 아닙니다. 다행히도 [scikit-learn](https://scikit-learn.org/)에서는 자동으로 테스트하고 분석하는 도구를 제공합니다.

## 일반적인 함수

- [metrics](https://scikit-learn.org/stable/modules/classes.html?highlight=metrics#module-sklearn.metrics)는 모델의 정확도 측정을 포함한 데이터 사이언스에 사용할 수 있는 함수 및 메트릭이 포함합니다.
- [mean_squared_error](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_squared_error.html#sklearn.metrics.mean_squared_error)는 선형 회귀 모델의 정확도를 측정하는데 사용되는 측정 값인 평균 제곱 오차를 반환합니다.
- [r2_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score)는 선형 회귀 모델의 정확도를 측정하는데 사용되는 값인 R^2 결정계수를 반환합니다.

## NumPy

[NumPy](https://numpy.org/)는 Python의 컴퓨터 사이언스용 패키지입니다.

### 일반적인 함수

- [sqrt](https://numpy.org/doc/1.18/reference/generated/numpy.sqrt.html?highlight=sqrt#numpy.sqrt)는 값의 제곱근을 반환합니다.

## Microsoft 학습 자료

[Microsoft Learn](https://learn.microsoft.com/?WT.mc_id=python-c9-niner)에서 관련 튜토리얼을 찾아보세요.

- [Python과 Azure Notebooks을 이용한 기계 학습 입문](https://docs.microsoft.com/learn/paths/intro-to-ml-with-python/?WT.mc_id=python-c9-niner)
