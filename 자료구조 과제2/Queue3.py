import numpy as np
import copy

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
            print("해당 아이템이 존재하지 않습니다.")

class Cust:
    def __init__(self, aTime):
        self.arriveTime= aTime
        self.orderTime = 0
        self.outTime = 0

class Shop:
    def __init__(self):
        self.q = Queue()

    def size(self):
        return self.q.size()

    def entCust(self, c):
        self.q.enQueue(c)

    def outCust(self, curTime):
        while self.size() > 0 and self.q.peek().outTime < curTime:
            self.q.deQueue()

    def getLast(self):
        return self.q.getLast()

curTime = 0
s = Shop()
while curTime < 14 * 60:
    _tmp = np.random.exponential(1, 1)
    curTime += _tmp
    s.outCust(curTime)
    c = Cust(curTime)

    if s.size() == 0:
        c.orderTime = c.arriveTime
    else:
        c.orderTime = s.getLast().outTime
    c.outTime = c.orderTime + np.random.normal(1,0.2,1)
    s.entCust(c)
    print(c.arriveTime, c.orderTime, c.outTime, s.size())