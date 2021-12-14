import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 로지스틱 회귀
# z = a * 무게 + b * 길이 + c * 대각선 + d * 높이 + e * 두께 + f
# 시그모이드 함수 = 1 / (1 + e^-z)


fish = pd.read_csv('https://bit.ly/fish_csv')
fish.head()

fish_input = fish[['Weight', 'Length', 'Diagonal', 'Height', 'Width']].to_numpy()
fish_target = fish['Species'].to_numpy()


train_input, test_input, train_target, test_target = train_test_split(fish_input, fish_target, random_state=42)

print(train_input)
print(test_input)

ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

# bream과 smelt 데이터만 골라내기
bream_smelt_indexes = (train_target=='Bream') | (train_target=='Smelt')
print(bream_smelt_indexes)
train_bream_smelt = train_scaled[bream_smelt_indexes]
target_bream_smelt = train_target[bream_smelt_indexes]
print(train_bream_smelt)
print(target_bream_smelt)

# 다항 데이터
lr = LogisticRegression(C=20, max_iter=1000)
lr.fit(train_scaled, train_target)
print(lr.score(train_scaled, train_target))
print(lr.score(test_scaled, test_target))

print(lr.predict(test_scaled[:5]))
proba = lr.predict_proba(test_scaled[:5])
print(np.round(proba, decimals=3))