import numpy as np

# 제곱근 출력하기
print(np.sqrt(2))

# 파이와 삼각함수
print(np.pi)
print(np.sin(0))
print(np.cos(np.pi))

# 랜덤함수 rand
print(np.random.rand(5)) # 0~1 사이의 random한 n개의 수 출력, 이때 배열의 형태로 출력된다.

# 랜덤함수 choice
print(np.random.choice(6, 10)) # 6미만의 random한 수 10개가 중복을 허용하고 나옴
print(np.random.choice(10, 6, replace=False)) # 중복을 허용하지 않고 나옴

