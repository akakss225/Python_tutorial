def path(grid, d):
    answer = []
    x = len(grid[0])
    y = len(grid)
    g = []
    
    for i in range(y):
        temp = []
        for j in range(x):
            temp.append([[i, j], grid[i][j]])
        g.append(temp)
        
    
    answer.append(d)
    while True:
        direction = answer[-1]
        nextY = direction[0][0]
        nextX = direction[0][1]
        dir = direction[1]
        
        if g[direction[0][0]][direction[0][1]][1] == "S":
            if direction[1] == "UP":
                if direction[0][0] + 1 == y:
                    nextY = 0
                    dir = "UP"
                else:
                    nextY = direction[0][0] + 1
                    dir = "UP"
            elif direction[1] == "DOWN":
                if direction[0][0] - 1 == -1:
                    nextY = y - 1
                    dir = "DOWN"
                else:
                    nextY = direction[0][0] - 1
                    dir = "DOWN"
            elif direction[1] == "LEFT":
                if direction[0][1] + 1 == x:
                    nextX = 0
                    dir = "LEFT"
                else:
                    nextX = direction[0][1] + 1
                    dir = "LEFT"
            elif direction[1] == "RIGHT":
                if direction[0][1] - 1 == -1:
                    nextX = x - 1
                    dir = "RIGHT"
                else:
                    nextX = direction[0][1] - 1
                    dir = "RIGHT"
        elif g[direction[0][0]][direction[0][1]][1] == "L":
            if direction[1] == "UP":
                if direction[0][1] + 1 == x:
                    nextX = 0
                    dir = "RIGHT"
                else:
                    nextX = direction[0][1] + 1
                    dir = "RIGHT"
            elif direction[1] == "DOWN":
                if direction[0][1] - 1 == -1:
                    nextX = x - 1
                    dir = "LEFT"
                else:
                    nextX = direction[0][1] - 1
                    dir = "LEFT"
            elif direction[1] == "LEFT":
                if direction[0][0] - 1 == -1:
                    nextY = y - 1
                    dir = "DOWN"
                else:
                    nextY = direction[0][0] - 1
                    dir = "DOWN"
            elif direction[1] == "RIGHT":
                if direction[0][0] + 1 == y:
                    nextY = 0
                    dir = "UP"
                else:
                    nextY = direction[0][0] + 1
                    dir = "UP"
        else:
            if direction[1] == "UP":
                if direction[0][1] - 1 == -1:
                    nextX = x - 1
                    dir = "RIGHT"
                else:
                    nextX = direction[0][1] - 1
                    dir = "RIGHT"
            elif direction[1] == "DOWN":
                if direction[0][1] + 1 == x:
                    nextX = 0
                    dir = "LEFT"
                else:
                    nextX = direction[0][1] + 1
                    dir = "LEFT"
            elif direction[1] == "LEFT":
                if direction[0][0] + 1 == y:
                    nextY = 0
                    dir = "UP"
                else:
                    nextY = direction[0][0] + 1
                    dir = "UP"
            elif direction[1] == "RIGHT":
                if direction[0][0] - 1 == -1:
                    nextY = y - 1
                    dir = "DOWN"
                else:
                    nextY = direction[0][0] - 1
                    dir = "DOWN"
        nextDirection = [[nextY,nextX], dir]
        
        if nextDirection in answer:
            break
        else:
            answer.append(nextDirection)
    
    return answer

def solution(grid):
    # 상 하 좌 우
    answer = []
    u = sorted(path(grid, [[0, 0], 'UP']))
    d = sorted(path(grid, [[0, 0], 'DOWN']))
    l = sorted(path(grid, [[0, 0], 'LEFT']))
    r = sorted(path(grid, [[0, 0], 'RIGHT']))
    answer.append(u)
    answer.append(d)
    answer.append(l)
    answer.append(r)
    
    for i in range(len(answer)-1):
        for j in range(i+1, len(answer)):
            if answer[i] == answer[j]:
                answer[j] = 0
    result = []
    for i in answer:
        if i != 0:
            result.append(len(i))
    
    return sorted(result)



grid = ["SL","LR"]
grid = ["SL","LL"]
# grid = ["R","R"]
print(solution(grid))