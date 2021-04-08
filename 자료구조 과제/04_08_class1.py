# Stack and Queue

# Stack : Last in/ First out

class Stack:
    def __init__(self):
        self.s = []
    
    def push(self, item):
        self.s.append(item)
    
    def isEmpty(self):
        return len(self.s) == 0
    
    def pop(self):
        if self.isEmpty() == False:
            return self.s.pop(-1)
        else:
            return None
    
    def size(self):
        return len(self.s)
    
    def peek(self):
        if self.isEmpty() == False:
            return self.s[-1]
        else:
            return None
        
s = Stack()

s.push('사과')
s.push('딸기')
s.push('포도')
s.push('체리')

print(s.s)

