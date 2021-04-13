import numpy as np

# 기본적으로 axis 값에 따라 차원이 바뀜
# axis = 0 : 행(가로)
# axis = 1 : 열(세로)
# axis = 2 : tensor

'''
numpy를 이용해 손쉽게 배열을 생성할 수 있으며
내장함수등을 이용할 수 있다.

list_data = [1,2,3]
array = np.array(list_data)

print(array)
print(array.size)
print(array.dtype)
print(array[2])
'''

'''
배열 메소드들

array1 = np.arange(4) # 0 ~ 3까지 자동으로 배열을 만들어주는 메소드
print(array1)

array2 = np.zeros((4,4), dtype=float) # zeros의 경우, 행렬의 생성 과 데이터타입 설정이 가능하며, 모든 element를 0으로 넣어주는 메소드
print(array2)

array3 = np.ones((4,4), dtype= str) # zeros와 동일하지만 모든 값을 1 로 통일한다.
print(array3)

array4 = np.random.randint(0, 10,(3,3)) # random.randint의 경우 (이상, 미만, 크기)에서 random한 숫자로 배열(행렬)을 만든다
print(array4)

# 또한 통계적으로 특정한 분포를 따르는 배열을 만들 수 있다
array5 = np.random.normal(0, 1, (3,3)) #평균이 0이고 표준편차가 1 인 표준 정규분포를 띄는 배열
print(array5)
'''

'''
배열 합치기 가능

가로
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
array3 = np.concatenate([array1, array2]) # 배열에 감싸서 만들어야함

print(array3.shape) # 크기
print(array3)


세로
arr1 = np.arange(4).reshape(1,4)
arr2 = np.arange(8).reshape(2,4)

print(arr1)
print(arr2)

arr3 = np.concatenate([arr1,arr2], axis=0)
print(arr3)

'''

# 배열 나누기 가능

arr = np.arange(8).reshape(2,4)
print(arr)
left, right = np.split(arr, [2], axis=1) # (배열, 자르는 기준index, 자르는 방향) 이중 index가 2이면 2번인덱스 왼쪽으로 나눔
print(left.shape)
print(right.shape)
print(left)
print(right)



'''
배열 재배치 가능

arr1 = np.array([1,2,3,4])
arr2 = arr1.reshape((2,2))

print(arr2)
'''

