class Poly1:
    def __init__(self, maxDeg):
        self.maxDeg = maxDeg
        self.coef = [0] * (maxDeg + 1)
        print(list)

    def set(self, Deg, coef):
        self.coef[Deg] = coef
    
    @classmethod
    def add(cls, p, q):
        if p.maxDeg > q.maxDeg:
            new = Poly1(p.maxDeg)
            new.set(p.maxDeg, p.coef[p.maxDeg])
            for i in range(0, p.maxDeg):
                new.set(i, p.coef[i] + q.coef[i])
        elif q.maxDeg < range(0, p.maxDeg - 1):
            new = Poly1(q.maxDeg)
            new.set(q.maxDeg, q.coef[q.maxDeg])
            for i in range(0, q.maxDeg):
                new.set(i,p.coef[i] + q.coef[i])
        return new

p = Poly1(4)
p.set(4,4)
p.set(3,3)
p.set(2,2)
print(p.coef)

q = Poly1(3)
q.set(3,3)
q.set(2,2)
q.set(1,1)
q.set(0,2)
print(q.coef)

print(Poly1.add(p,q).coef)


