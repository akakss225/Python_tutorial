import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler


# 특성 공학과 규제 == 튜닝

# 변환기 >> PolynomialFeatures(degree=int, include_bias=boolean)
# degree는 튜닝할때 사용. 특성의 갯수에 따라 달라진다. 좀 더 높은 score를 위해
# 사용법
poly = PolynomialFeatures()
poly.fit([[2,3]])
# 1 , 2 , 3 , 2**2 , 2*3 , 3**2
print(poly.transform([[2,3]]))


# 농어데이터 >> 길이 / 높이 / 두께
df = pd.read_csv('https://bit.ly/perch_csv')
# 넘파이 배열로 변환
perch_full = df.to_numpy()
print(perch_full)

# 규제 >> 이전에 scaling작업 해줄때의 작업을 해주는 라이브러리


# 릿지 회귀



# 라쏘 회귀