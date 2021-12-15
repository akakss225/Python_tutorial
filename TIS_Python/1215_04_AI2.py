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






