# Stack
# Last in First out

class Stack:
    def __init__(self):
        self.s = []
    
    def size(self):
        return len(self.s)
    
    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False
    
    def push(self, item):
        self.s.append(item)
    
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.s.pop(-1)
    
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.s[-1]

s = Stack()


print(s.isEmpty())
print(s.peek())

s.push('사과')

print(s.isEmpty())
print(s.peek())

print(s.pop())
print(s.peek())