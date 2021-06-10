# 다항식의 덧셈

class Poly:
    def __init__(self, maxdeg):
        self.maxdeg = maxdeg
        self.a = [0] * (maxdeg+1)
    
    def setA(self, deg, a):
        self.a[deg] = a
    
    
    @classmethod
    def add(cls, p, q):
        # q가 차수가 더 높다면
        if p.maxdeg < q.maxdeg:
            # 차수가 큰 parameter와 같은 차수의 새로운 변수를 생성
            r = Poly(q.maxdeg)
            # 차수가 작은 parameter의 길이의 + 1 한 횟수만큼 반복 << 상수항을 포함하기 떄문.
            for i in range(p.maxdeg + 1):
                # 반복하며 r의 인덱스 순서대로 합 값을 setting해준다.
                r.setA(i, q.a[i] + p.a[i])
            # 이후 나머지 계산이 되지않은 q의 고차항을 setting해준다.
            for i in range(p.maxdeg + 1, q.maxdeg + 1):
                r.setA(i, q.a[i])
        # p가 차수가 더 높다면
        elif p.maxdeg > q.maxdeg:
            # 위의 과정을 반대로 반복.
            r = Poly(p.maxdeg)
            for i in range(q.maxdeg + 1):
                r.setA(i, q.a[i] + p.a[i])
            for i in range(q.maxdeg + 1, p.maxdeg + 1):
                r.setA(i, p.a[i])
        # 차수가 같다면
        else:
            # 그냥 다 더해주면 됨.
            r = Poly(p.maxdeg)
            for i in range(p.maxdeg + 1):
                r.setA(i, p.a[i] + q.a[i])
        return r

p = Poly(4)
p.setA(4,4)
p.setA(2,3)
p.setA(0,3)
print(p.a)

q = Poly(2)
q.setA(2,4)
q.setA(1,2)
q.setA(0,1)
print(q.a)

r = Poly.add(p, q)
print(r.a)
