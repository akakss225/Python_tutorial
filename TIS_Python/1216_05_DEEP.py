# 딥러닝
# tensorflow >> keras사용

from tensorflow import keras
import matplotlib.pyplot as plt

# 머신러닝과 문법의 순서가 다르다

# 1. 데이터 준비하기
# 2. 모델만들기 >> Dense : 밀집층 만들기 & Model
# 3. 컴파일 >> GPU성능에 따라 달라짐
# 4. 훈련시키기
# 5. evaluate == (score) 평가하기


# 데이터 읽어오기
(train_input, train_target), (test_input, test_target) = keras.datasets.fashion_mnist.load_data()

# 크기 확인
print(train_input.shape, train_target.shape)
print(test_input.shape, test_target.shape)

# 10개만 출력해보기
fig, axs = plt.subplots(1, 10, figsize=(10, 10))
for i in range(10):
  axs[i].imshow(train_input[i], cmap='gray_r')
  axs[i].axis('off')
plt.show()

# 분류번호 출력하기 실질적인 정답
print([train_target[i] for i in range(10)])


