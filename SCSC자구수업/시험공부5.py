# 행렬 덧셈 + 역행렬

import numpy as np

class SparseMatrix:
    def __init__(self,m ,n):
        self.sm = [[m, n, 0]]
        self.m = m
        self.n = n
    
    def getValue(self, row, col):
        for i in range(1, len(self.sm)):
            if row == self.sm[i][0] and col == self.sm[i][1]:
                return self.sm[i][2]
        return 0
    
    def append(self, cell):
        self.sm.append(cell)
        self.sm[0][2] += 1
        
    def shape(self):
        return self.m, self.n
        
    def transpose(self):
        c = SparseMatrix(self.m, self.n)
        for i in range(len(self.sm)):
            if i == 0:
                c.sm[0][2] = self.sm[0][2]
            else:
                c.sm.append([self.sm[i][1], self.sm[i][0], self.sm[i][2]]) # 그냥 바꿔치기만 하면댐
        return c

    def print(self):
        c = np.zeros((self.m, self.n))
        for i in range(1, len(self.sm)):
            c[self.sm[i][0]-1, self.sm[i][1]-1] = self.sm[i][2]
        print(c)
    
    @classmethod
    def add(cls, a, b):
        c = SparseMatrix(a.m, a.n)
        u = set()
        if a.sm[0][0] != b.sm[0][0] or a.sm[0][1] != b.sm[0][1]:
            return None
        else:
            for i in range(1, a.sm[0][2]+1):
                u.add((a.sm[i][0], a.sm[i][1]))
            for i in range(1, b.sm[0][2]+1):
                u.add((b.sm[i][0], b.sm[i][1]))
            for i in list(u):
                temp = a.getValue(i[0], i[1]) + b.getValue(i[0], i[1])
                if temp != 0:
                    c.append([i[0], i[1], temp])
            return c
            

A = SparseMatrix(3,3)
A.append([1,1,1])
A.append([2,2,2])
A.append([3,3,3])

B = SparseMatrix(3,3)
B.append([1,1,1])
B.append([1,2,1])
B.append([2,2,1])
B.append([2,3,1])
B.append([3,3,1])

A.print()
B.print()


C = SparseMatrix.add(A,B)
C.print()

D = C.transpose()

D.print()