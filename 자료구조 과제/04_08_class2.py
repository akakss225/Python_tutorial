# Stack and Queue

# Queue(Queuing Theory) : First in / First out

# 커피가게 rotaiton

def isEmpty(a):
    return len(a) == 0

class Queue:
    def __init__(self):
        self.q = []
    def enQueue(self, item):
        self.q.append(item)
    def deQueue(self):
        if not q.q:
            return None
        else:
            return self.q.pop(0)
    
q = Queue()
print(q.q)
print(q.deQueue())
q.enQueue(10)
q.enQueue(20)
q.enQueue(30)
q.enQueue(40)
print(q.q)
q.deQueue()
print(q.q)