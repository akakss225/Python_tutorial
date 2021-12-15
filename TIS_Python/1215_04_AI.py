import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_validate
import numpy as np
from sklearn.model_selection import StratifiedKFold

# 트리 알고리즘


wine = pd.read_csv('https://bit.ly/wine-date')
wine.head()

data = wine[['alcohol', 'sugar', 'pH']].to_numpy()
target = wine['class'].to_numpy()

# 훈련 8 : 테스트 2
train_input, test_input, train_target, test_target = train_test_split(data, target, test_size=0.2, random_state=42)
# 위의 훈련 8에서 다시 훈련 8 : 검증 2
sub_input, val_input, sub_target, val_target = train_test_split(train_input, train_target, test_size=0.2, random_state=42)

# 과대적합
dt = DecisionTreeClassifier(random_state=42)
dt.fit(sub_input, sub_target)
print(dt.score(sub_input, sub_target))
print(dt.score(val_input, val_target))


scores = cross_validate(dt, train_input, train_target)
print(scores)

print(np.mean(scores['test_score']))

# 튜닝 : 교차 검증
splitter = StratifiedKFold(n_splits = 10, shuffle = True, random_state = 42)
scores = cross_validate(dt, train_input, train_target, cv = splitter)
print(scores)
print(np.mean(scores['test_score']))

# 그리드 서치
from sklearn.model_selection import GridSearchCV
params = {'min_impurity_decrease' : [0.0001, 0.0002, 0.0003, 0.0004, 0.0005]}

gs = GridSearchCV(DecisionTreeClassifier(random_state=42), params, n_jobs=-1)
gs.fit(train_input, train_target)
dt = gs.best_estimator_
print(dt)
print(gs.best_params_)

# 파라미터를 늘려서 다시 실행 >> 정확도 up
params = {'min_impurity_decrease' : np.arange(0.0001, 0.001, 0.0001),
          'max_depth' : range(5, 20, 1),
          'min_samples_split' : range(2, 100, 10)}
gs = GridSearchCV(DecisionTreeClassifier(random_state=42), params, n_jobs=-1)
gs.fit(train_input, train_target)
print(gs.best_estimator_)

# 위의 경우 파라미터가 추가 될 떄마다, 그 파라미터의 길이만큼 추가 곱을 해주어 실행한다.
# 이는 실행 횟수가 기하급수적으로 증가함을 의미한다.
# 이를 좀 더 효율적으로 하기 위해 랜덤 서치를 한다

# 랜덤서치 >> 난수를 발생시켜, 무작위로 서치한다.
