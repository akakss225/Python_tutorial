# 12 / 10 (fri) class 5 . numpy >> 수학관련

import matplotlib.pyplot as plt
import numpy as np
import csv
from matplotlib import rc

# t = np.arange(0., 5., 0.2)
#
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()

# 0~1난수 생성
a = np.random.rand(5)
print(a)

# 0 ~ 5 수를 10개 출력하기
print(np.random.choice(6, 10))

# 0 ~ 9 수를 6개 출력 + 중복을 제거
print(np.random.choice(10, 6, replace=False))

# 인구 구조 알아보기 with numpy

f = open("age.csv", "r")
data = csv.reader(f)
next(data)
data = list(data)
name = input('인구 구조가 알고 싶은 지역의 이름(읍면동 단위)을 입력해주세요 : ')
mn = 1           # 최솟값을 저장할 변수 생성 및 초기화
result_name = '' # 최솟값을 갖는 지역의 이름을 저장할 변수 생성 및 초기화
result = 0       # 최솟값을 갖는 지역의 연령대별 인구 비율을 저장할 배열 생성 및 초기화
for row in data :
    if name in row[0] :
        home = np.array(row[3:], dtype=int)/int(row[2])
for row in data :
    away = np.array(row[3:], dtype=int)/int(row[2])
    s = np.sum((home-away)**2)
    if s < mn and name not in row[0] : # 자기자신은 뺴기
        mn = s
        result_name = row[0]
        result = away

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False
plt.title(name + "지역과 가장 비슷한 인구 구조를 가진 지역") # 그래프 제목 설정
plt.plot(home, label=name)             # home 값을 그리는 그래프 레이블 설정
plt.plot(result, label=result_name)    # result 값을 그리는 그래프 레이블 설정
plt.legend()                           # 범례 표기
plt.show()