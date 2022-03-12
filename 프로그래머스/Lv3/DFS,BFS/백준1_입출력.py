import sys
from collections import defaultdict
from collections import deque

read = sys.stdin.readline

N, M, V = map(int, read().split())

g = []
for i in range(M):
    x, y = map(int, read().split())
    g.append([x, y])

def dfs(v, g):
    g.sort(reverse=True)
    d = defaultdict(list)
    for x, y in g:
        d[x].append(y)
        d[y].append(x)
    
    s = [v]
    visit = []
    while s:
        cur = s.pop()
        
        if cur not in visit:
            visit.append(cur)
            print(cur, end=" ")
            if cur in d:
                s.extend(d[cur])

def bfs(v, g):
    g.sort()
    d = defaultdict(list)
    for x, y in g:
        d[x].append(y)
        d[y].append(x)
    
    q = deque([v])
    visit = []
    
    while q:
        cur = q.popleft()
        
        if cur not in visit:
            visit.append(cur)
            print(cur, end=" ")
            if cur in d:
                q.extend(d[cur])

dfs(V, g)
print()
bfs(V, g)