# DFS / BFS
# 두개를 이용해 출력해보기
from collections import deque
import sys




def dfs(s, graph):
    d = dict()
    for i in graph:
        if i[0] in d:
            d[i[0]].append(i[1])
            d[i[0]].sort(reverse=True)
        else:
            d[i[0]] = [i[1]]
        if i[1] in d:
            d[i[1]].append(i[0])
            d[i[1]].sort(reverse=True)
        else:
            d[i[1]] = [i[0]]
    
    stack = [s]
    visit = []
    
    while stack:
        cur = stack.pop()
        if cur not in visit:
            visit.append(cur)
            for i in d:
                if i == cur and d[i]:
                    stack.extend(d[i])
                    d[i].clear()
                    break
    return visit

def bfs(s, graph):
    d = dict()
    for i in graph:
        if i[0] in d:
            d[i[0]].append(i[1])
            d[i[0]].sort()
        else:
            d[i[0]] = [i[1]]
        if i[1] in d:
            d[i[1]].append(i[0])
            d[i[1]].sort()
        else:
            d[i[1]] = [i[0]]
            
    q = deque([s])
    visit = []
    
    while q:
        cur = q.popleft()
        
        if cur not in visit:
            visit.append(cur)
            for i in d:
                if i == cur and d[i]:
                    q.extend(d[i])
                    d[i].clear()
                    break
    return visit
    


start = 1
graph = [[1,2],[1,3],[1,4],[2,4],[3,4]]

start = 3
graph = [[5,4],[5,2],[1,2],[3,4],[3,1]]

# start = 1000
# graph = [[999, 1000]]


print(dfs(start, graph))
print(bfs(start, graph))