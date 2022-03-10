import sys

read = sys.stdin.readline

# 상하좌우/대각선
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

result = []
while True:
    W, H = map(int, read().split())
    
    if W == 0 and H == 0:
        break
    
    land_map = []
    for _ in range(H):
        land_map.append(list(map(int, read().split())))
    
    visit = [[False] * W for i in range(H)]
    
    answer = 0
    
    for y in range(H):
        for x in range(W):
            if land_map[y][x] == 1 and visit[y][x] == False:
                s = [[y, x]]
                while s:
                    cy, cx = s.pop()
                    visit[cy][cx] = True
                    for i in range(8):
                        ny, nx = cy+dy[i], cx+dx[i]
                        
                        if 0<=nx<W and 0<=ny<H:
                            if land_map[ny][nx] == 1 and visit[ny][nx] == False:
                                s.append([ny, nx])
                answer += 1
    result.append(answer)

for i in result:
    print(i)
