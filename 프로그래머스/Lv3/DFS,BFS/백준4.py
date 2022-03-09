import sys
from collections import defaultdict

read = sys.stdin.readline
n = int(read())
m = int(read())
d = defaultdict(list)

s = [1]
visit = []
for i in range(m):
    x, y = map(int, read().split())
    d[x].append(y)
    d[y].append(x)


def dfs(d):
    global s
    global visit
    while s:
        cur = s.pop()
        if cur not in visit:
            visit.append(cur)
            s.extend(d[cur])
            d[cur].clear()
            
    visit.pop(0)
    print(len(visit))

dfs(d)
