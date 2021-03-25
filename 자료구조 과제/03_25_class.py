# 다항식의 덧셈2

class Poly2:
    def __init__(self):
        self.parm =[]

    def append(self, parm):
        self.parm.append(parm)

    def pop(self):
        return self.parm.pop(0)

    def size(self):
        return len(self.parm)

    @classmethod
    def add(cls, q, p):
        r = Poly2()
        while p.size() > 0 and q.size() > 0:
            if p.parm[0][1] > q.parm[0][1]:
                r.append(p.pop())
            elif p.parm[0][1] < q.parm[0][1]:
                r.append(q.pop())
            else:
                _tmp1 = p.pop()
                _tmp2 = q.pop()
                r.append([_tmp1[0] + _tmp2[0], _tmp1[1]])
        
        if p.size() > 0:
            while p.size() > 0:
                r.append(p.pop())
        else:
            while q.size() > 0:
                r.append(q.pop())
        return r

p = Poly2()
p.append([4,4])
p.append([3,2])
p.append([3,0])

q = Poly2()
q.append([3,3])
q.append([4,2])
q.append([2,1])
q.append([1,0])

r = Poly2.add(p,q)
print(r.parm)
