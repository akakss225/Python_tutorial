# Queue
# 기본적으로 Queue의 경우 2개의 변수가 사용됨
# enQueue : Queue를 늘리는것
# deQueue : Queue를 줄이는것

class Queue:
    def __init__(self):
        self.q = []
    
    def enQueue(self, item):
        self.q.append(item)
    
    def deQueue(self):
        if self.isEmpty() == True:
            return None
        else:
            return self.q.pop(0)
    
    def size(self):
        return len(self.q)
    
    def isEmpty(self):
        return not self.q
    
    #가장 먼저 추가된 데이터
    def getFront(self):
        if self.isEmpty() == True:
            return None
        else:
            return self.q[0]
    
    #가장 나중에 추가된 데이터
    def getRear(self):
        if self.isEmpty() == True:
            return None
        else:
            return self.q[-1]
    

q = Queue()
print(q.isEmpty())
print(q.deQueue())
q.enQueue(10)
q.enQueue(20)
q.enQueue(30)
print(q.q)
print(q.getFront())
print(q.getRear())

print(q.deQueue())
print(q.q)