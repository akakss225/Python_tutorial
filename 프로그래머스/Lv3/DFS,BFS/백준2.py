# 대체로 미로찾기, 최단거리 문제는 BFS를 사용하는게 좋음
# cnt를 적극 활용할것을 추천

from collections import deque

def bfs(n, m, graph):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    
    visit = [[False] * m for i in range(n)]
    q = deque([[0, 0, 1]])
    visited = []
    
    while q:
        y, x, cnt = q.popleft()
        visited.append([y, x, cnt])
        visit[y][x] = True
        if x == m-1 and y == n-1:
            break
        
        for i in range(4):
            nextY = dy[i] + y
            nextX = dx[i] + x
            if 0 <= nextX < m and 0 <= nextY < n:
                if visit[nextY][nextX] == False and graph[nextY][nextX] == 1:
                    q.append([nextY, nextX, cnt + 1])
    return visited[-1][2]

n = 4
m = 6
graph = [
    [1,0,1,1,1,1],
    [1,0,1,0,1,0],
    [1,0,1,0,1,1],
    [1,1,1,0,1,1]
]
graph = [
    [1,1,0,1,1,0],
    [1,1,0,1,1,0],
    [1,1,1,1,1,1],
    [1,1,1,1,0,1]
]

print(bfs(n, m, graph))