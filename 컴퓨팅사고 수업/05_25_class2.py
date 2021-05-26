from keras.datasets import mnist
import matplotlib.pyplot as plt

(trainingImages, trainLabels), (testImages, testLabels) = mnist.load_data()

print('학습 이미지 개수=', trainingImages.shape)
print('테스트 이미지 개수=', testImages.shape)

print('테스트 세번째 숫자=', testLabels[3])
print('\n테스트 세번째 숫자 이미지')

digit = testImages[3]
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()