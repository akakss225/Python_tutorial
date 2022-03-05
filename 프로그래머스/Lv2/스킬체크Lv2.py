def solution(w,h):
    return ((w + h)/gcd(w,h)-1)*gcd(w,h)

def gcd(w, h):
    s = min(w, h)
    b = max(w, h)
    if h == 0:
        return b
    else:
        return gcd(s, b%s)

w = 8
h = 12

print(solution(8, 12))







import string
from collections import deque

def convert(num, base):
    tmp = string.digits + string.ascii_uppercase
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]

def solution2(n, t, m, p):
    answer = ""
    num = 0
    turn = 0
    myturn = p - 1
    while True:
        cur = deque(list(str(convert(num, n))))
        while cur:
            cur_num = cur.popleft()
            if turn == myturn:
                answer += cur_num
                t -= 1
                if turn == m - 1:
                    turn = 0
                else:
                    turn += 1
            else:
                if turn == m - 1:
                    turn = 0
                else:
                    turn += 1
            if t == 0:
                return answer
        num += 1
    
    return answer

n = 2
t = 4
m = 2
p = 1

print(solution2(n, t, m, p))