import numpy as np

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

# 상수는 대문자로 표기해주는게 관례
# 추가적으로 수학에서 대체로 변수가 대문자로 표현되면, 행렬을 의미한다.

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
