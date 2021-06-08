# Queue
# Last in Last out

class Queue:
    def __init__(self):
        self.q = []
    
    def size(self):
        return len(self.q)
    
    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False
        
    def enQueue(self, item):
        self.q.append(item)
    
    def deQueue(self):
        if self.isEmpty():
            return None
        else:
            return self.q.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.q[0]
        
q = Queue()
print(q.q)
print(q.isEmpty())
print(q.peek())
print(q.deQueue())

q.enQueue(1)
q.enQueue(3)
q.enQueue(5)
q.enQueue(7)
q.enQueue(9)

print(q.q)
print(q.isEmpty())
print(q.deQueue())
print(q.peek())