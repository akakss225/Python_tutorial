# 행렬의 덧셈뺄셈
import numpy as np
from numpy.matrixlib.defmatrix import matrix

class SparseMatrix:
    def __init__(self, m, n): # 행렬 size받기
        # 행렬내부 값이 존재하는 좌표와 값을 담아두는 list의 첫 값은, matrix의 크기와 값이 담겨져있는 좌표의 수를 return해준다.
        self.sm = [[m, n, 0]]
        self.m = m
        self.n = n
    
    def append(self, cell):
        # list에 값을 append해주고
        self.sm.append(cell)
        # 값이 추가되었으니 첫번쨰 인덱스의 세번째 인덱스값에 + 1 을 해준다.
        self.sm[0][2] += 1
        
    def shape(self):
        return self.m, self.n
    
    # row와 column값을 주면 그에 대한 값을 반환해 주는 함수(메소드)
    def getValue(self, row, col):
        # 첫번쨰 인덱스는 행렬의 사이즈를 나타내는 것이기에 제외하고 반복문을 시행해준다.
        for i in range(1, len(self.sm)):
            # for loop을 돌면서 row값과 col값이 일치하는 리스트의 값을 리턴해준다.
            if row == self.sm[i][0] and col == self.sm[i][1]:
                return self.sm[i][2]
        # for loop이 끝나고 나오면 return 0을 해줌. << 왜냐하면 없기때문.
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
        # 행렬의 크기가 다르다면 덧셈을 실행할 수 없기 때문에 return None
        if q.sm[0][0] != p.sm[0][0] or q.sm[0][1] != p.sm[0][1]:
            return None
        # 행렬의 크기가 같다면 실행
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