import sys
from collections import deque

read = sys.stdin.readline
N, M = map(int, read().split())
place = []
for i in range(N):
    place.append(list(map(int, read().strip())))



dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

q = deque([[0, 0, 1]])
while q:
    y, x, cnt = q.popleft()
    place[y][x] = -1
    
    if x+1 == M and y+1 == N:
        print(cnt)
        break
    
    for i in range(4):
        ny = dy[i] + y
        nx = dx[i] + x
        if 0 <= nx < M and 0 <= ny < N:
            if place[ny][nx] == 1:
                q.append([ny, nx, cnt + 1])
