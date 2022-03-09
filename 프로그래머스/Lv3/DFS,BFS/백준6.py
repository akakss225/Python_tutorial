import sys
from collections import defaultdict

read = sys.stdin.readline
N, M = map(int, read().split())
d = defaultdict(list)

for _ in range(M):
    x, y = map(int, read().split())
    d[x-1].append(y-1)
    d[y-1].append(x-1)

def dfs(d):
    visit = [False] * N
    cnt = 0
    for i in d:
        if visit[i] == False:
            s = [i]
            while s:
                cur = s.pop()
                if visit[cur] == False:
                    visit[cur] = True
                    s.extend(d[cur])
                    
            cnt += 1
    if False in visit:
        cnt += visit.count(False)
    print(cnt)

dfs(d)
