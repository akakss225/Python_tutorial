import sys

read = sys.stdin.readline

R, C = map(int, read().split())

grid = []
for i in range(R):
    grid.append(list(read().strip()))

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def bfs():
    result = 1
    q = set([(0, 0, grid[0][0])])
    while q:
        y, x, visit = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < C and 0 <= ny < R:
                if grid[ny][nx] not in visit:
                    q.add((ny, nx, visit + grid[ny][nx]))
                    result = max(result, len(visit + grid[ny][nx]))
    return result

print(bfs())