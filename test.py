def dfs(start, place, visit):
    global N
    global dy, dx
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

N = 5
dy = [1, 0, -1, 0]
dx = [0, -1, 0, 1]
visit = [[False] * N for i in range(N)]
place = [
[6 ,8 ,2 ,6 ,2],
[3 ,2 ,3 ,4 ,6],
[6 ,7 ,3 ,3 ,2],
[7 ,2 ,5 ,3 ,6],
[8 ,9 ,5 ,2 ,7]
]

print(dfs(5, place, visit))