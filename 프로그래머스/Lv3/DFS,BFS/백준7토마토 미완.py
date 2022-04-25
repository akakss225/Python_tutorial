import sys
from collections import deque


read = sys.stdin.readline

M, N, H = map(int, read().split())

tomato = []
ripen = deque()
for i in range(H):
    temp = []
    for j in range(N):
        temp.append(list(map(int, read().split())))
        for k in range(len(temp[j])):
            if temp[j][k] == 1:
                ripen.append([j, k, i, 0])
    tomato.append(temp)


dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
dz = [1, -1, 0, 0]
result = 0

while ripen:
    y, x, z, cnt = ripen.popleft()
    result = cnt
    for i in range(4):
        ny, nx, nz = dy[i] + y, dx[i] + x, dz[i] + z
        
        if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H:
            if tomato[nz][ny][nx] == 0:
                ripen.append([ny, nx, nz ,cnt + 1])
                tomato[nz][ny][nx] = 1

for i in tomato:
    if 0 in i:
        result = -1
        break

print(result)
