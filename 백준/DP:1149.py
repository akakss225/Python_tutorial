# RGB distance

import sys

input = sys.stdin.readline

N = int(input())

grid = []

for i in range(N):
    temp = input().split()
    result = []
    for i in temp:
        result.append(int(i))
    grid.append(result)

colors = [[[grid[0][0], 0], [grid[0][1], 1], [grid[0][2], 2]]]

for i in range(1, N):
    temp = []
    first_mini = min(colors[i-1])
    second_mini = sorted(colors[i-1])[1]
    
    for j in range(3):
        if first_mini[1] == j:
            temp.append([second_mini[0] + grid[i][j], j])
        else:
            temp.append([first_mini[0] + grid[i][j], j])
    
    colors.append(temp)

print(min(colors[N-1])[0])
