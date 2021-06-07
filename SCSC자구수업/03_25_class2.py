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
        # 모든 값이 0 인 3x3 marix생성
        mat = np.zeros((self.m, self.n))
        # 0번째 인덱스는 초기 설정 cell이기 때문에, 출력하지 않는다.
        for i in range(1, len(self.sm)):
            # 3x3 matrix의 각 항에 해당되는 sm[i][2]값을 넣어준다.
            mat[self.sm[i][0] - 1, self.sm[i][1] - 1] = self.sm[i][2]
        print(mat)
    
    @classmethod
    def add(cls, a, b):
        # 행렬의 덧셈의 경우 같은 size의 행렬만 덧셈이 가능하기에, 아무 matrix의 행렬 size를 가져온다.
        c = SparseMatrix(a.m, a.n)
        if a.sm[0][0] != b.sm[0][0] or a.sm[0][1] != b.sm[0][1]:
            return None
            # 디멘션이 안맞기 때문에 none을 출력. 즉, 같은 크기의 행렬만 계산 가능.
        else:
            # 세트(set) 는 중복을 허용하지 않는 집합이다.
            u = set()
            # a.sm의 첫번째 인덱스는 초기값 이기 때문에 1번부터 시작, 또한, 값이 들어있는 항의 갯수는 a.sm[0][2]개 이기 때문에 a.sm[0][2]번까지 반복.
            for i in range(1, a.sm[0][2]+1):
                # set(집합)은 중복을 허용하지 않기 때문에, 같은 값은 같은 곳에 저장됨.
                u.add((a.sm[i][0], a.sm[i][1]))
            for i in range(1, b.sm[0][2]+1):
                u.add((b.sm[i][0], b.sm[i][1]))
            # 집합을 돌면서, 값이 0 이 아닌 것을 새로운 matrix에 append해준다.
            for term in list(u):
                _tmp = a.getValue(term[0], term[1]) + b.getValue(term[0], term[1])
                if _tmp != 0:
                    
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
