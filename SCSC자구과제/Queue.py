# Queue
# enQueue : Queue에 추가하는 메소드
# deQueue : Queue에서 삭제시키는 메소드

# 기본적으로 Queue의 경우 FIFO이기 때문에, deQueue를 쓸 떄 pop(0) 를 사용한다.

class Queue:
    def __init__(self):
        self.q = []
    
    def isEmpty(self):
        return not self.q
    
    def peek(self):
        return self.q[0]
    
    def enQueue(self, item):
        return self.q.append(item)
    
    def deQueue(self): 
        if self.isEmpty() == True:
            return None
        else:
            return self.q.pop(0)

q = Queue()
q.enQueue(10)
q.enQueue(20)
q.enQueue(30)
print(q.isEmpty())
print(q.q)
print(q.peek())
q.deQueue()
print(q.q)
