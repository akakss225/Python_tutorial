# IDEA
# 1. 주어진 항공권을 다 사용해야함
# 2. [a, b] 이면, a -> b 항공권을 의미함
# 3. 시작은 반드시 ICN
# 4. 알파벳 오름차순을 기준으로 작성

# DFS구현해서 해야함!

from audioop import reverse
from collections import deque

def solution(tickets):
    tickets.sort(key=lambda x:x[1])
    d = dict()
    
    for i in tickets:
        if i[0] in d:
            d[i[0]].append(i[1])
        else:
            d[i[0]] = [i[1]]
    
    s = [d["ICN"].pop()]
    answer = ["ICN"]
    while s:
        cur = s.pop()
        answer.append(cur)
        if cur in d and d[cur]:
            s.append(d[cur].pop())
    return answer

def solution(tickets):
    tickets.sort(key=lambda x:x[1])
    d = dict()
    
    for i in tickets:
        if i[0] in d:
            d[i[0]].append(i[1])
        else:
            d[i[0]] = deque([i[1]])
    
    q = deque([d["ICN"].popleft()])
    answer = ["ICN"]
    while q:
        cur = q.popleft()
        answer.append(cur)
        if cur in d and d[cur]:
            q.append(d[cur].popleft())
    return answer


def solution(tickets):
    answer = []
    tickets.sort(key=lambda x:x[0]=="ICN")
    answer.extend(tickets.pop())
    while tickets:
        for i in range(len(tickets)):
            if answer[-1] == tickets[i][0]:
                cur = tickets.pop(i)
                answer.append(cur[1])
                break
    return answer



visit = []

def dfs(start, tickets):
    global visit
    
    if start in tickets and tickets[start]:
        visit.append(start)
        next_location = tickets[start].pop()
        dfs(next_location, tickets)
    else:
        visit.append(start)
        return
    
    
def solution(tickets):
    global visit
    d = dict()
    for i in tickets:
        if i[0] in d:
            d[i[0]].append(i[1])
        else:
            d[i[0]] = [i[1]]
    visit.append("ICN")
    start = d["ICN"].pop()
    dfs(start, d)
    
    return visit


def dfs(n, d, visit):
    
    if n in d:
        if d[n]:
            n = d[n].pop()
            visit.append(n)
            dfs(n, d, visit)
        else:
            return
    else:
        return

def solution(t):
    d = dict()
    for i in t:
        if i[0] in d:
            d[i[0]].append(i[1])
        else:
            d[i[0]] = [i[1]]
    
    visit = ["ICN"]
    dfs("ICN", d, visit)
    
    return visit


def solution(t):
    t.sort(reverse=True)
    d = dict()
    for i in t:
        if i[0] in d:
            d[i[0]].append(i[1])
        else:
            d[i[0]] = [i[1]]
    s = ["ICN"]
    visit = []
    while s:
        cur = s[-1]
        if cur not in d or len(d[cur]) == 0:
            visit.append(s.pop())
        else:
            s.append(d[cur].pop())
    visit.reverse()
    return visit


t = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
t = [["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]
t = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(t))