# 다항식의 덧셈 2

class Poly:
    def __init__(self):
        # 파라미터를 담을 list생성
        self.pm = []
    
    def setPm(self, para, deg):
        # 차수항, 차수 순서대로 받아서 리스트 형태로 삽입.
        self.pm.append([para, deg])
    
    def pop(self):
        # 가장 큰 차수먼저 빼는 함수
        return self.pm.pop(0)

    def size(self):
        # 사이즈 확인
        return len(self.pm)
    
    @classmethod
    def add(cls, p, q):
        # 덧셈을 실행할 새로운 객체 생성
        r = Poly()
        # 둘중 하나가 소진될때까지
        while p.size() > 0 and q.size() > 0:
            # 만약 p의 차수가 더 크다면
            if p.pm[0][1] > q.pm[0][1]:
                # p를 뺴서 담아주기
                r.pm.append(p.pop())
            # 반대면
            elif p.pm[0][1] < q.pm[0][1]:
                # q를 빼서 담아주기
                r.pm.append(q.pop())
            # 차수가 같다면
            else:
                # 임시로 p 와 q를 담아주고,
                tempP = p.pop()
                tempQ = q.pop()
                # 차수항을 더한 것, 차수 순서대로 append해준다
                r.pm.append([tempP[0] + tempQ[0], tempQ[1]])
                
        # 둘중 하나가 다 소진되고 나왔을 때
        # 만약 p가 남아있다면
        if p.size() > 0:
            # 남아있는 모든 p 의 값을 넣어준다
            while p.size() > 0:
                r.pm.append(p.pop())
        # q가 남아있다면
        else:
            # 남아있는 모든 q의 값을 넣어준다
            while q.size() > 0:
                r.pm.append(q.pop())
        
        # 새롭게 만들어진 r 을 return
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
