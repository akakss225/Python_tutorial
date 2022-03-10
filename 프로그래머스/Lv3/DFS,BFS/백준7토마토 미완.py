import sys
from collections import deque

read = sys.stdin.readline

M, N = map(int, read().split())

tomato = []
ripen = deque()
for i in range(N):
    temp = list(map(int, read().split()))
    tomato.append(temp)
    if 1 in temp:
        ripen.append([i, temp.index(1), 0])


dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
result = 0

while ripen:
    y, x, cnt = ripen.popleft()
    result = cnt
    for i in range(4):
        ny, nx = dy[i] + y, dx[i] + x
        
        if 0 <= nx < M and 0 <= ny < N:
            if tomato[ny][nx] == 0:
                ripen.append([ny, nx, cnt + 1])
                tomato[ny][nx] = 1

for i in tomato:
    if 0 in i:
        result = -1
        break
print(result)
