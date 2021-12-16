import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

fruits = np.load('fruits_300.npy')

# 2차원 배열로
fruits_2d = fruits.reshape(-1, 100*100)

# cluster 는 항목 수 >> 사과 파인애플 바나나
km = KMeans(n_clusters=3, random_state=42)

# 비지도 학습이기 때문에 target은 없음
km.fit(fruits_2d)

print(km.labels_)

print(np.unique(km.labels_, return_counts=True))

# 그림그리기 함수 만들기
def draw_fruits(arr, ratio=1):
    n = len(arr)
    rows = int(np.ceil(n/10))
    cols = n if rows < 2 else 10
    fig, axs = plt.subplots(rows, cols, figsize=(cols * ratio, rows * ratio), squeeze=False)
    for i in range(rows):
        for j in range(cols):
            if i*10 + j < n:
                axs[i, j].imshow(arr[i*10+j], cmap='gray_r')
            axs[i, j].axis('off')
    plt.show()
draw_fruits(km.labels_ == 0)