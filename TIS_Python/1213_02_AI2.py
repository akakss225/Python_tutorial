from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from matplotlib import rc

# 1. 데이터 준비 - 훈련데이터, 훈련타겟 / 평가데이터, 평가타겟 >> scale작업
# 2. 훈련 - 어떤 알고리즘을 사용할 것인가?
# 3. 평가 - 0 ~ 1 : 1에 가까울수록 훈련이 잘 됨을 의미
# 4. 예측 or 판정 - predict. 예측에 사용할 데이터 >> 필요하면 scale 작업


# 지도 학습 : 정답을 알려줌 ( target 존재 )
# 비지도 학습 : 정답을 안알려줌 ( target 없음 )

fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8,
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7,
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

fish_data = np.column_stack((fish_length, fish_weight))

fish_target = np.concatenate((np.ones(35), np.zeros(14)))

# 사이킷 런을 이용해 데이터 나누기. 훈련을 시켜주는 메소드 train_test_split()
# 반드시 기억해야할 메소드
# train_test_split()
# fit()
# score()
# predict()
train_input, test_input, train_target, test_target = train_test_split(fish_data, fish_target, random_state=42)

# 데이터 가져오기
kn = KNeighborsClassifier()
# 훈련시키기
kn.fit(train_input, train_target)
# 평가하기
kn.score(test_input, test_target)
# 판정
print(kn.predict(test_input))

# 평균
mean = np.mean(train_input, axis=0)
# 표준편차
std = np.std(train_input, axis=0)

# (훈련 데이터 - 평균) / 표준편차 = 정제된 훈련된 데이터임. >> x축 y축 스케일을 맞추는 작업
train_scaled = (train_input - mean) / std

# train_scaled로 다시 훈련 시키기
kn.fit(train_scaled, train_target )

# 평가 데이터도 스케일을 맞춰줌
test_scaled = (test_input - mean) / std
# 판정
kn.score(test_scaled, test_target)

new = ([25, 150] - mean) / std
print(kn.predict([new]))