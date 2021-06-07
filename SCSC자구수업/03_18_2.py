# 다항식의 사칙연산 


class Poly1:
    def __init__(self, maxDeg):
        self.maxDeg = maxDeg
        self.coef = [0] * (maxDeg + 1) # 4차 방정식. 따라서 상수항 포함 총 5개의 항이 필요.
    
    def setCoef(self, deg, coef):
        self.coef[deg] = coef # deg(차수) 인덱스에 항(coef)을 넣어줌.

    @classmethod
    def add(cls, p, q):
        if p.maxDeg > q.maxDeg: # 차수가 더 높은걸 확인. p가 더 크다면
            r = Poly1(p.maxDeg) # 높은 차수의 임의의 객체 생성
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
