# IDEA
# 1. 사람 수 n 만큼 2개씩 짝지어 count + 1 만큼씩 리턴해서 새로운 리스트에 넣음
# 2. 지정된 숫자 a와 b는 인덱싱으로 체크를 해줌.
# 3. a와 b 가 붙는 순간 답을 리턴
from collections import deque

from aem import con


def solution(n,a,b):
    answer = 1
    result = deque()
    for i in range(1, n+1):
        result.append(i)
    
    temp = []
    while True:
        if len(result) > 1:
            cur = result.popleft()
            next = result.popleft()
            if cur == a and next == b:
                return answer
            if cur == a or cur == b:
                temp.append(cur)
                continue
            elif next == a or next == b:
                temp.append(next)
                continue
            
            temp.append(cur)
        else:
            result.extend(temp)
            temp.clear()
            answer += 1

from math import ceil

def solution(n, a, b):
    answer = 0
    result = deque()
    for i in range(1, n+1):
        result.append(i)
    while True:
        cur = result.popleft()
        next = result.popleft()
        if cur == 1:
            answer += 1
            
        if cur == a and next == b:
            return answer
        
        if cur == a:
            result.append(ceil(cur/2))
            a = ceil(cur/2)
            continue
        elif cur == b:
            result.append(ceil(cur/2))
            b = ceil(cur/2)
            continue
        elif next == a:
            result.append(ceil(next/2))
            a = ceil(next/2)
            continue
        elif next == b:
            result.append(ceil(next/2))
            b = ceil(next/2)
            continue
        result.append(ceil(cur/2))
        
def solution(n, a, b):
    answer = 1
    c = min(a, b)
    d = max(a, b)
    while True:
        if c % 2 == 1 and d == c + 1:
            return answer
        c = ceil(c/2)
        d = ceil(d/2)
        answer += 1
        
        
    


print(solution(8,4,7))