

def solution(maps):
    answer = 0
    n = len(maps) - 1
    m = len(maps[0]) - 1
    x = 0
    y = 0
    visited = []
    while x != n and y != m:
        maps[y][x] = 0
        visited.append([x, y])
        answer += 1
        
        
    
    return -1

maps = [
    [1,0,1,1,1],
    [1,0,1,0,1],
    [1,0,1,1,1],
    [1,1,1,0,1],
    [0,0,0,0,1]
    ]

print(solution(maps))