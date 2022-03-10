import sys

read = sys.stdin.readline

N = int(read())

grid = []
for _ in range(N):
    grid.append(list(read().strip()))

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def dfsM(grid):
    answer = 0
    global N
    
    visit = [[False]*N for _ in range(N)]
    
    for y in range(N):
        for x in range(N):
            if grid[y][x] == "R" or grid[y][x] == "G":
                if visit[y][x] == False:
                    s = [[y, x]]
                    while s:
                        cy, cx = s.pop()
                        visit[cy][cx] = True
                        
                        for i in range(4):
                            ny, nx = dy[i] + cy, dx[i] + cx
                            
                            if 0 <= nx < N and 0 <= ny < N:
                                if grid[ny][nx] == "R" or grid[ny][nx] == "G":
                                    if visit[ny][nx] == False:
                                        s.append([ny, nx])
                                        
                    answer += 1
            else:
                if visit[y][x] == False:
                    s = [[y, x]]
                    while s:
                        cy, cx = s.pop()
                        visit[cy][cx] = True
                        
                        for i in range(4):
                            ny, nx = dy[i] + cy, dx[i] + cx
                            
                            if 0 <= nx < N and 0 <= ny < N:
                                if grid[ny][nx] == "B":
                                    if visit[ny][nx] == False:
                                        s.append([ny, nx])
                    answer += 1
    print(answer)

def dfsN(grid):
    answer = 0
    global N
    
    visit = [[False]*N for _ in range(N)]
    
    for y in range(N):
        for x in range(N):
            if grid[y][x] == "R":
                if visit[y][x] == False:
                    s = [[y, x]]
                    while s:
                        cy, cx = s.pop()
                        visit[cy][cx] = True
                        
                        for i in range(4):
                            ny, nx = dy[i] + cy, dx[i] + cx
                            
                            if 0 <= nx < N and 0 <= ny < N:
                                if grid[ny][nx] == "R":
                                    if visit[ny][nx] == False:
                                        s.append([ny, nx])
                    answer += 1
            elif grid[y][x] == "G":
                if visit[y][x] == False:
                    s = [[y, x]]
                    while s:
                        cy, cx = s.pop()
                        visit[cy][cx] = True
                        
                        for i in range(4):
                            ny, nx = dy[i] + cy, dx[i] + cx
                            
                            if 0 <= nx < N and 0 <= ny < N:
                                if grid[ny][nx] == "G":
                                    if visit[ny][nx] == False:
                                        s.append([ny, nx])
                    answer += 1
            else:
                if visit[y][x] == False:
                    s = [[y, x]]
                    while s:
                        cy, cx = s.pop()
                        visit[cy][cx] = True
                        
                        for i in range(4):
                            ny, nx = dy[i] + cy, dx[i] + cx
                            
                            if 0 <= nx < N and 0 <= ny < N:
                                if grid[ny][nx] == "B":
                                    if visit[ny][nx] == False:
                                        s.append([ny, nx])
                    answer += 1
    print(answer, end=" ")

dfsN(grid)
dfsM(grid)