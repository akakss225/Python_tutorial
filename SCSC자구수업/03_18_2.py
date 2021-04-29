# 다항식의 사칙연산 

class Poly1:
    def __init__(self, maxDeg):
        self.maxDeg = maxDeg
        self.coef = [0] * (maxDeg + 1)
    
    def setCoef(self, deg, coef):
        self.coef[deg] = coef

    @classmethod    
    def add(cls, p, q):
        if p.maxDeg > q.maxDeg:
            r = Poly1(p.maxDeg)
            for i in range(q.maxDeg + 1):
                r.setCoef(i ,p.coef[i] + q.coef[i])
            for i in range(q.maxDeg +1, p.maxDeg +1):
                r.setCoef(i, p.coef[i])
        elif p.maxDeg < q.maxDeg:
            r = Poly1(q.maxDeg)
            for i in range(p.maxDeg + 1):
                r.setCoef(i ,q.coef[i] + q.coef[i])
            for i in range(p.maxDeg +1, q.maxDeg +1):
                r.setCoef(i, q.coef[i])
        return r
        

p = Poly1(4)
p.setCoef(4,4)
p.setCoef(2,3)
p.setCoef(0,3)
print(p.coef)

q = Poly1(2)
q.setCoef(2,4)
q.setCoef(1,2)
q.setCoef(0,1)
print(q.coef)

r = Poly1.add(p, q)
print(r.coef)
