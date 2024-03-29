import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# 리눅스 명령어
# !wget https://bit.ly/fruits_300_data -O fruits_300.npy

fruits = np.load('fruits_300.npy')
print(fruits.shape)

# 첫번째 사진의 첫번째 행 모든 열 출력
print(fruits[0, 0:])

# 첫번째 사진 출력
plt.imshow(fruits[0], cmap='gray')
plt.show()

# 반전시켜, 원본이미지로 출력
plt.imshow(fruits[0], cmap='gray_r')
plt.show()

# 샘플 차원 변경하기 to 1D
apple = fruits[0:100].reshape(-1, 100 * 100)
pineapple = fruits[100:200].reshape(-1, 100 * 100)
banana = fruits[200:300].reshape(-1, 100 * 100)

# apple 의 평균값 / axis = 축 1 == x축 0 == y축
print(apple.mean(axis=1))

# 히스토그램 그리기
# alpha값은 겹쳤을때를 대비한 값. >> 투명도
plt.hist(np.mean(apple, axis=1), alpha=0.8)
plt.hist(np.mean(pineapple, axis=1), alpha=0.8)
plt.hist(np.mean(banana, axis=1), alpha=0.8)
plt.legend(['apple', 'pineapple', 'banana'])
plt.show()

# axis = 0
# 막대그래프 이용
fig, axs = plt.subplots(1, 3, figsize=(20, 5))
fig.axs = plt.subplots(1, 3, figsize = (20, 5))
axs[0].bar(range(10000), np.mean(apple, axis=0))
axs[1].bar(range(10000), np.mean(pineapple, axis=0))
axs[2].bar(range(10000), np.mean(banana, axis=0))
plt.show()

# 평균이미지 그리기
# 그림을 그려야하기 때문에 다시 2차원 배열로 변환
apple_mean = np.mean(apple, axis = 0).reshape(100, 100)
pineapple_mean = np.mean(pineapple, axis = 0).reshape(100, 100)
banana_mean = np.mean(banana, axis = 0).reshape(100, 100)
fig, axs = plt.subplots(1, 3, figsize = (20, 5))
axs[0].imshow(apple_mean, cmap = 'gray_r')
axs[1].imshow(pineapple_mean, cmap = 'gray_r')
axs[2].imshow(banana_mean, cmap = 'gray_r')
plt.show()


# 평균과 가장 가까운 사진 고르기
abs_diff = np.abs(fruits - apple_mean)
abs_mean = np.mean(abs_diff, axis = (1, 2))
print(abs_mean.shape)

apple_index = np.argsort(abs_mean)[:100]
fig, axs = plt.subplots(10, 10, figsize = (10, 10))
for i in range(10):
  for j in range(10):
    axs[i, j].imshow(fruits[apple_index[i * 10 + j]], cmap = 'gray_r')
    axs[i, j].axis('off')
plt.show()

