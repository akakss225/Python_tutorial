# eval()메소드 Stack으로 구현하기 수식 후위표기 알고리즘(Postfix algorithm)
class Stack:
    def __init__(self):
        self.s = []

    def push(self, item):
        self.s.append(item)

    def isEmpty(self):
        return len(self.s) == 0 # True, False

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
    
def eqBranktCheck(f):
    s = Stack()
    for i in range(len(f)):
        if f[i] == '(':
            s.push(f[i])
        elif f[i] == ')':
            if s.pop() == None:
                return False
    if s.isEmpty() == True:
        return True
    else:
        return False

def isOder(a):
    if a == '+' or a == '-' or a == '/' or a == '*':
        return True
    else:
        return False

def isNum(a):
    try:
        float(a)
        return True
    except ValueError:
        return False

    
eq = '( 12.3 + 6 ) * 3 / 6'
eqList = eq.split(" ")
s = Stack()
postEq = []

print(eqList)

for item in eqList:
    if item == '(':
        s.push(item)
    elif item == ')':
        while True:
            _tmp = s.pop()
            if _tmp == '(':
                break
            else:
                postEq.append(_tmp)
    elif item == "+" or item == "-":
        while isOder(s.peek()) == True:
            postEq.append(s.pop())
        s.push(item)
    elif item == "*" or item == "/":    
        while s.peek() == "*" or s.peek() == "/":
            postEq.append(s.pop())
        s.push(item)
    elif isNum(item) == True:
        postEq.append(item)
    print(s.s)
    print(postEq)
    
while s.isEmpty() == False:
    postEq.append(s.pop())

print(postEq)