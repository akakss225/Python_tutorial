# eval()메소드 Stack으로 구현하기 수식 후위표기 알고리즘(Postfix algorithm)
class Stack:
    def __init__(self):
        self.s = []
    
    def push(self, item):
        self.s.append(item)
        
    def isEmpty(self):
        return len(self.s) == 0
    
    def pop(self):
        if self.isEmpty() == True:
            return None
        else:
            return self.s.pop(-1)
    
    def size(self):
        return len(self.s)
    
    def peek(self):
        if self.isEmpty == True:
            return None
        else:
            return self.s[-1]
    
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

    
num = '( 12.3 + 6 ) * 3 / 6'
numList = num.split(" ")
s = Stack() # 빈 스텍
postNum = [] # 빈 리스트를 준비

print(numList)

for item in numList:
    # 만약 item 이 ( 이면, Stack s 에  ( 를 넣는다.
    if item == '(':
        s.push(item)
    # 또한, item 이 ) 이면,
    elif item == ')':
        while True:
            # Stack s에서 계속해서 pop한 값이 ( 일때까지 찾는다.
            temp = s.pop()
            # 만일 temp에 ( 가 들어오면, while문을 나간다.
            if temp == '(':
                break
            else:
                # 반복문을 통해 temp에 들어오는 값이 ( 가 아니면, 빈 list에 값을 담아놓는다.
                postNum.append(temp)
    # item이 + - 연산자 이면,
    elif item == '+' or item == '-':
        # 우선 isOder를 통해 스택의 last가 연산자임을 확인하고,
        while isOder(s.peek()) == True:
            # True가 나온다면, s에서 pop한 값을 list에 담는다.
            postNum.append(s.pop())
        # 스택에 쌓인 값이 숫자 혹은 + - 연산자가 아니라면, item을 s에 담아준다.
        s.push(item)
    # item이 * / 연산자 이면,
    elif item == '*' or item == '/':
        # 우선 s에 쌓여있는 값 중 last가 곱셈 나눗셈 연산자인지 확인하고
        while s.peek() == '*' or s.peek() == '/':
            # 맞다면, 그 값을 리스트에 담아주고
            postNum.append(s.pop())
        # 아니라면 item을 s에 담아준다.
        s.push(item)
    # item이 숫자라면,
    elif isNum(item) == True:
        # 그대로 list에 담아준다
        postNum.append(item)
    # list 혹은 Stack에 값을 담을 때 마다 출력해준다.
    print(postNum)

# 최종적으로 Stack이 빌때까지 Stack에 남은 값들을 list에 담아준다.
#이는 곧 최종적으로 list 의 마지막 부분에는 무조건 연산자가 오게된다.
while s.isEmpty() == False:
    postNum.append(s.pop())

print(s.s)



