import numpy as np
from random import *

class Queue:
    def __init__(self):
        self.q = []

    def enQueue(self, item):
        self.q.append(item)

    def deQueue(self):
        if self.isEmpty() == False:
            return self.q.pop(0)

    def getLast(self):
        if self.isEmpty() == False:
            return self.q[-1]
        else:
            return None

    def size(self):
        return len(self.q)

    def isEmpty(self):
        return not self.q
    
    def peek(self):
        if self.isEmpty() == False:
            return self.q[0]

    def delete(self, item):
        if item in self.q:
            self.q.remove(item)
        else:
            print("item is not found")

class Cust:
    def __init__(self, arriveTime):
        # 손님 도착시간
        self.arriveTime= arriveTime
        # 손님 주문시간
        self.orderTime = 0
        # 손님 나가는 시간
        self.outTime = 0

class Shop: # 결국 프로그램을 돌릴떄는 가게 기준으로 해야함.
    def __init__(self):
        # 마치 은행처럼 Queue의 주체는 카페가 됨.
        self.q = Queue()

    def size(self):
        return self.q.size()

    def entCust(self, c):
        self.q.enQueue(c) # 손님이 들어온것은 Queue에서 enQueue와 같은 의미

    def outCust(self, curTime):
        # 손님이 0명이 아닐때, 동시에 손님이 나간 시간이 현재 시간보다 작을 때 deQueue해준다.
        while self.size() > 0 and self.q.peek().outTime < curTime: 
            self.q.deQueue() # 손님이 나가는것은 Queue에서 deQueue와 같은 의미

    def getLast(self): # 마지막 손님 입장.
        return self.q.getLast()

curTime = 0
s = Shop()
# 현재 시간 0(8시)부터 시작해서 14시간동안(오후 10시까지) 판매시작.
while curTime < 14 * 60:
    temp = np.random.exponential(1, 1)
    # 난수로 현재시간을 실시간으로 구해준다.
    curTime += temp
    # s.outCust시간은 현재 시간에서 커피가 만들어지는 랜덤한 시간을 더하기 위하여 미리 지정해놓는다.
    s.outCust(curTime)
    c = Cust(curTime)
    if s.size() == 0:
        # 이전 Queue가 없다면, 들어오자마자 주문할 수 있다고 가정한다.
        c.orderTime = c.arriveTime
    else:
        # 그렇지 않다면, 이전 손님이 나가는 시간이 주문시간이 된다.
        c.orderTime = s.getLast().outTime
    # 손님이 나간시간은 주문시간에서 평균이 1 이고 표준편차가 0.2인 random한 수를 더해주어 구한다.
    c.outTime = c.orderTime + np.random.normal(1,0.2,1)
    # 구한 손님 인스턴스를 상점에 적용한다.
    s.entCust(c)
    print(c.arriveTime, c.orderTime, c.outTime, s.size())