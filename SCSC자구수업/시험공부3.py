# 다항식의 덧셈 2

class Poly:
    def __init__(self):
        self.pm = []
    
    def setPm(self, para, deg):
        self.pm.append([para, deg])
    
    def pop(self):
        return self.pm.pop(0)

    def size(self):
        return len(self.pm)
    
    @classmethod
    def add(cls, p, q):
        r = Poly()
        while p.size() > 0 and q.size() > 0:
            if p.pm[0][1] > q.pm[0][1]:
                r.pm.append(p.pop())
            elif p.pm[0][1] < q.pm[0][1]:
                r.pm.append(q.pop())
            else:
                tempP = p.pop()
                tempQ = q.pop()
                r.pm.append([tempP[0] + tempQ[0], tempQ[1]])
        
        if p.size() > 0:
            while p.size() > 0:
                r.pm.append(p.pop())
        else:
            while q.size() > 0:
                r.pm.append(q.pop())
            
        return r
    
    
p = Poly()
p.setPm(4,4)
p.setPm(3,2)
p.setPm(3,0)

q = Poly()
q.setPm(3,3)
q.setPm(4,2)
q.setPm(2,1)
q.setPm(1,0)

print(p.pm)
print(q.pm)
r = Poly.add(p,q)
print(r.pm)
