# LinkedList를 이용한 다항식의 덧셈.
import numpy as np
'''
class Node:
    def __init__(self, item = None, link = None):
        self.item = item
        self.link = link
        
class LinkedList:
    def __init__(self):
        self.root = None
       
    def append(self, item):
        newNode = Node(item)
        curNode = self.root
        if self.root == None:
            self.root = newNode
        else:
            while curNode.link != None:
                curNode = curNode.link
            curNode.link = newNode
            
    def size(self):
        listSize = 1
        curNode = self.root
        while curNode.link != None:
            curNode = curNode.link
            listSize += 1
        return listSize
    
    def get(self, idx):
        curNode = self.root
        for i in range(idx):
            curNode = curNode.link
        return curNode.item

    def peek(self):
        return self.root.item
    
    def pop(self):
        temp = self.root
        self.root = self.root.link
        return temp.item

class Poly3:
    def __init__(self):
        self.parm = LinkedList()

    def set(self, coef, order):
        self.parm.append([coef, order])

    def peek(self):
        return self.parm.peek()

    def pop(self): 
        return self.parm.pop()

    def size(self):
        return self.parm.size()

    def print(self):
        n = self.parm.size()
        for i in range(n-1):
            _tmp = self.parm.get(i)
            coef = _tmp[0]
            order = _tmp[1]
            print("%d x^%d + " % (coef, order), end = "")
        if self.parm.get(n-1)[1] == 0:
            print("%d" %self.parm.get(n-1)[0])
        else:
            print("%d x^%d" %(self.parm.get(n-1)[0], self.parm.get(n-1)[1]))
            
    @classmethod
    def add(cls, p, q):
        r = Poly3()
        while p.size() > 0 and q.size() > 0:
            if p.peek() > q.peek():
                temp = p.pop()
                r.set(temp[0], temp[1])
            elif p.peek() > q.peek():
                temp = q.pop()
                r.set(temp[0], temp[1])
            else:
                temp1 = p.pop()
                temp2 = q.pop()
                r.set(temp1[0] + temp2[0], temp1[1])
        return r
        


x = Poly3()
x.set(4,4)
x.set(3,2)
x.print()

y = Poly3()
y.set(3,3)
y.set(4,2)
y.set(2,1)
y.set(1,0)
y.print()

z = Poly3.add(x,y)
z.print()



# 두개의 희소행렬의 곱셈
'''
class SparseMatrix:
    def __init__(self,m,n):
        self.sm = [[m ,n ,0]]
        self.m = m
        self.n = n

    def append(self, cell):
        self.sm.append(cell)
        self.sm[0][2] += 1
    
    def shape(self):
        return self.m, self.n
    
    # row와 column값을 주면 그에 대한 값을 반환해 주는 함수(메소드)
    def getValue(self, row, col):
        for i in range(1, len(self.sm)):
            if row == self.sm[i][0] and col == self.sm[i][1]:
                return self.sm[i][2]
        return 0
    
    def transpose(a):
        b = SparseMatrix(a.m, a.n)
        for i in range(len(a.sm)):
            if i == 0 :
                b.sm[0][2] = a.sm[0][2]
            else:
                b.append([a.sm[i][1], a.sm[i][0], a.sm[i][2]])
        return b

    def print(self):
        mat = np.zeros((self.m, self.n))
        for i in range(1, len(self.sm)):
            mat[self.sm[i][0] - 1, self.sm[i][1] - 1] = self.sm[i][2]
        print(mat)
        
    
    @classmethod
    def add(cls, a, b):
        c = SparseMatrix(a.m, a.n)
        if a.sm[0][0] != b.sm[0][0] or a.sm[0][1] != b.sm[0][1]:
            return None
            # 디멘션이 안맞기 때문에 none을 출력. 즉, 같은 크기의 행렬만 계산 가능.
        else:
            # 세트(set) 는 중복을 허용하지 않는 집합이다.
            u = set()
            
            for i in range(1, a.sm[0][2] + 1):
                u.add((a.sm[i][0], a.sm[i][1]))
            for i in range(1, b.sm[0][2]):
                u.add((b.sm[i][0], b.sm[i][1]))
            for term in list(u):
                _tmp = a.getValue(term[0], term[1]) + b.getValue(term[0], term[1])
                if _tmp != 0:
                    # 
                    c.append([term[0], term[1], _tmp])
            return c
   
    @classmethod
    def mult(cls, p, q):
        if p.m != q.n:
            return -1
        c = SparseMatrix(p.m, q.n)
        for i in range(1, p.m+1):
            for j in range(1, q.n+1):
                summ = 0
                for k in range(1, p.n+1):
                    summ += p.getValue(i,k) * q.getValue(k,j)
                if summ != 0:
                    c.append([i, j, summ])
        return c


p = SparseMatrix(3,3)
q = SparseMatrix(3,3)

p.append([1,1,1])
p.append([2,2,2])
p.append([3,3,3])
q.append([1,1,4])
q.append([1,2,7])
q.append([2,3,2])
q.append([3,3,1])

p.print()
q.print()

c = SparseMatrix.mult(p, q)
c.print()  
