# 다항식의 덧셈

class Poly:
    def __init__(self, maxdeg):
        self.maxdeg = maxdeg
        self.a = [0] * (maxdeg+1)
    
    def setA(self, deg, a):
        self.a[deg] = a
    
    
    @classmethod
    def add(cls, p, q):
        if p.maxdeg < q.maxdeg:
            r = Poly(q.maxdeg)
            for i in range(p.maxdeg + 1):
                r.setA(i, q.a[i] + p.a[i])
            for i in range(p.maxdeg + 1, q.maxdeg + 1):
                r.setA(i, q.a[i])
        elif p.maxdeg > q.maxdeg:
            r = Poly(p.maxdeg)
            for i in range(q.maxdeg + 1):
                r.setA(i, q.a[i] + p.a[i])
            for i in range(q.maxdeg + 1, p.maxdeg + 1):
                r.setA(i, p.a[i])
        else:
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
