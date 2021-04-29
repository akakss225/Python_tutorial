# 바 그래프

import matplotlib.pyplot as plt

x1 = [1,3,4,5,6,7,9]
y1 = [4,7,2,4,7,8,3]

x2 = [2,4,6,8,10]
y2 = [5,6,2,6,2]

plt.bar(x1, y1, label="Blue Bar", color='b') # label은 범례이름 지정
plt.bar(x2, y2, label="Green Bar", color='g') # color는 색 지정
plt.plot()

plt.xlabel("bar number") # x축 이름
plt.ylabel("bar height") # y축 이름
plt.title('Bar Chart Example') # Chart이름
plt.legend() # 범례함수
plt.show() # 그래프를 띄우는 함수
