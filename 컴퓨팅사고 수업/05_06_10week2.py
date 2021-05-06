import numpy as np

# 모든 값이 0 인 2x3행렬
print(np.zeros((2,3)))

# 모든 값이 1 인 2x3행렬
print(np.ones((2,3)))

# 모든 값이 특정 값인 행렬
print(np.full((3,3), 7))

# 대각선의 값이 1 이고 나머진 0인 3x3행렬
print(np.eye(3))

# 그 밖의 행렬 만들기
a = np.array(np.arange(30)).reshape((5,6))
print(a)

# 행렬 splicing
b = np.array([[1,2,3],[4,5,6]])
c = b[0:2,0:2]
print(c)

# 행렬 곱
x = np.array([[4,5],[8,9]])
y = np.array([[2,3],[5,7]])

print(np.dot(x,y))