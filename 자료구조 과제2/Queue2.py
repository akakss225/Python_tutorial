import numpy as np
import matplotlib.pyplot as plt
import random

class Queue:
    def __init__(self):
        # instance객체가 만들어지면, Queue를 위한 list를 만들어준다.
        self.q = []
    
    def isEmpty(self):
        # Queue list에 대하여 비어있으면 True, element가 존재하면 False를 호출하는 메소드
        return not self.q
    
    def peek(self):
        # Queue에서 First Out되는 element를 호출하는 메소드
        return self.q[0]
    
    def enQueue(self, item):
        # Queue에 element를 추가해주는 메소드
        return self.q.append(item)
    
    def deQueue(self): 
        # Queue에 element를 삭제해주는 메소드
        if self.isEmpty() == True:
            return None
        else:
            return self.q.pop(0)


lamda = 1
'''
지수분포표 만드는 코드

x = np.linspace(0, 10, 100)
pdf = (1/lamda) * np.exp(-x/lamda)
plt.plot(x, pdf)
plt.show()
'''

'''
난수 만드는 코드

np.random.seed(seed=1)
x = np.random.exponential(1,10)
print(x)
entTime = np.cumsum(x) # cummurative sum : 누적합 
print(entTime) # 따라서 x담긴 10개의 난수 element들의 누적합이 entTime의 element로 들어감
               # 즉, x[0] = entTime[0], x[0] + x[1] = entTime[1], entTime[1] + x[2] = entTime[2] ...
'''

#지수분포표 적분
'''
x = np.linspace(0, 10, 100)
cdf = 1 - np.exp(-x / lamda)
plt.plot(x,cdf)
plt.show()
'''

'''
난수로 표현된 값을 넣어 지수분포표로 표현해도
기존의 지수분포표와 매우 유사한 값이 나옴

u = np.random.random(100)
n = - lamda * np.log(u)
plt.hist(n, bins = 'auto')
plt.show()
'''
