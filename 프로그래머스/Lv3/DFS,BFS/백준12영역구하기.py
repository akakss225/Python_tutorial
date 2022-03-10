import sys

read = sys.stdin.readline

Y, X, K = map(int, read().split())

grid = [[1]*X for _ in range(Y)]

position = set()

for _ in range(K):
    temp = list(map(int, read().split()))
    position1 = (temp[1], temp[0])
    position2 = (temp[3]-1, temp[2]-1)
    position.add(position1)
    position.add(position2)
    
    for y in range(position1[0], position2[0]+1):
        for x in range(position1[1], position2[1]+1):
            position.add((y, x))

for y, x in position:
    grid[y][x] = 0

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


result = 0
answer = []
for y in range(Y):
    for x in range(X):
        if grid[y][x] == 1:
            s = [[y,x]]
            cnt = 0
            while s:
                cy, cx = s.pop()
                grid[cy][cx] = -1
                cnt += 1
                for i in range(4):
                    ny = dy[i] + cy
                    nx = dx[i] + cx
                    
                    if 0 <= nx < X and 0 <= ny < Y:
                        if grid[ny][nx] == 1:
                            grid[ny][nx] = -1
                            s.append([ny, nx])
            answer.append(cnt)
            result += 1

answer.sort()

print(result)
for i in answer:
    print(i,end=" ")
