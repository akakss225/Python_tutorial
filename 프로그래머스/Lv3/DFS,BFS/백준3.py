import sys

# read = sys.stdin.readline
# n = int(read())
# g = []
# for i in range(n):
#     temp = list(map(int, read().strip()))
#     g.append(temp)


def bfs(n, graph):
    answer = []
    global dy, dx
    visit = [[False] * n for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 and visit[i][j] == False:
                cnt = 0
                s = [[i, j]]
                visit[i][j] = True
                while s:
                    cy, cx = s.pop()
                    cnt += 1
                    visit[cy][cx] = True
                    for k in range(4):
                        ny = cy + dy[k]
                        nx = cx + dx[k]
                        
                        if 0 <= nx < n and 0 <= ny < n:
                            if graph[ny][nx] == 1 and visit[ny][nx] == False:
                                if [ny, nx] not in s:
                                    s.append([ny, nx])
                answer.append(cnt)
    answer.sort()
    print(len(answer))
    for i in answer:
        print(i)
    

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
n = 7
g = [
    [0,1,1,0,1,0,0],
    [0,1,1,0,1,0,1],
    [1,1,1,0,1,0,1],
    [0,0,0,0,1,1,1],
    [0,1,0,0,0,0,0],
    [0,1,1,1,1,1,0],
    [0,1,1,1,0,0,0]
]
n = 7
g = [
    [0,1,1,0,1,1,1],
    [0,1,1,0,1,0,1],
    [1,1,1,0,1,0,1],
    [1,0,0,0,1,1,1],
    [0,1,0,0,0,0,0],
    [0,1,1,1,1,1,0],
    [0,1,1,1,0,0,0]
]

bfs(n, g)