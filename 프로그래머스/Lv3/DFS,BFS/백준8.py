import sys

read = sys.stdin.readline

N = int(read())
place = []
big = 0
for _ in range(N):
    temp = list(map(int, read().split()))
    if max(temp) > big:
        big = max(temp)
    place.append(temp)



dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]

def dfs(start, place):
    global N
    global dy, dx
    visit = [[False] * N for _ in range(N)]
    
    result = 0
    for a in range(N):
        for b in range(N):
            if place[a][b] > start and visit[a][b] == False:
                s = [[a, b]]
                while s:
                    y, x = s.pop()
                    visit[y][x] = True
                    
                    for i in range(4):
                        ny, nx = dy[i] + y, dx[i] + x
                        if 0 <= nx < N and 0 <= ny < N:
                            if visit[ny][nx] == False and place[ny][nx] > start:
                                s.append([ny, nx])
                result += 1
    return result

answer = []
for i in range(big+1):
    answer.append(dfs(i, place))
print(max(answer))