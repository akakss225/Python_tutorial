import sys
from collections import defaultdict
from tkinter import Y

read = sys.stdin.readline
T = int(read())

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

for _ in range(T):
    M, N, K = map(int, read().split())
    
    visit = [[False] * M for i in range(N)]
    place = [[0] * M for i in range(N)]
    position = []
    
    result = 0
    
    for i in range(K):
        x, y = map(int, read().split())
        position.append([y, x])
        place[y][x] = 1
    
    for y, x in position:
        
        if visit[y][x] == False:
            s = [[y, x]]
            while s:
                cy, cx = s.pop()
                visit[cy][cx] = True
                
                for i in range(4):
                    ny = dy[i] + cy
                    nx = dx[i] + cx
                    
                    if 0 <= nx < M and 0 <= ny < N:
                        if place[ny][nx] == 1 and visit[ny][nx] == False:
                            s.append([ny, nx])
            result += 1
    print(result)