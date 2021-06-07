# 행렬의 덧셈뺄셈
import numpy as np
from numpy.matrixlib.defmatrix import matrix

class SparseMatrix:
    def __init__(self, m, n): # 행렬 size받기
        self.sm = [[m, n, 0]]
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
    
    def print(self):
        matrix = np.zeros((self.m, self.n))
        for i in range(1, len(self.sm)):
            matrix[self.sm[i][0]-1, self.sm[i][1]-1] = self.sm[i][2]
        print(matrix)
    
    @classmethod
    def add(cls, q, p):
        c = SparseMatrix(q.m, q.n)
        u = set()
        if q.sm[0][0] != p.sm[0][0] or q.sm[0][1] != p.sm[0][1]:
            return None
        else:
            for i in range(1, q.sm[0][2]+1): # 중복값 허용 x 
                u.add((q.sm[i][0], q.sm[i][1]))
            for i in range(1, p.sm[0][2]+1): # 따라서 값이 존재하는 좌표(?)만 담음 
                u.add((p.sm[i][0], p.sm[i][1]))
            for i in list(u): # 값이 존재하는 모든 좌표를 리스트 형태로 호출
                temp = p.getValue(i[0], i[1]) + q.getValue(i[0], i[1]) # 값이 있는 좌표의 합 을 구해 리뉴얼시킴.
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