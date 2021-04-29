# Stack and Queue

# Stack : Last in/ First out


# Stack의 경우 리스트의 역배열을 만들고자 할 때 사용되는 대표적인 자료구조이다.

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
print(s.isEmpty())
print(s.size())
print(s.peek())
print(s.s)
s.pop()
print(s.s)

a = [1,2,3,4,5]
print(a)
print(a[::-1]) # 이러한 메소드가 Stack을 통해 만들어진다.

# Stack의 개념을 이용한 reverse함수 만들기.
def reverse(a):
        s = Stack()
        b = ''
        for i in range(len(a)):
            s.push(a[i])
        for i in range(len(a)):
            b += s.pop()
        return b

a = 'abcdefg'
print(reverse(a))

# 수식에서 '('와  ')' 의 수가 맞는지 확인하는 메소드 또한 Stack의 개념을 사용한다.

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

f = '(1+2) + (3*4) ='
print(eqBranktCheck(f))

# eval()메소드 Stack으로 구현하기 수식 후위표기 알고리즘(Postfix algorithm)

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

a = '12.1'
print(isOder(a))
print(isNum(a))



