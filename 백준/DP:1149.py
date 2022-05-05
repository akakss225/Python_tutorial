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

first = min(grid[0])
idx = grid[0].index(first)
colors = [[first, idx]]

for i in range(1, N):
    grid[i][colors[i-1][1]] = 9999
    minimum = min(grid[i])
    mini_idx = grid[i].index(minimum)
    
    colors.append([colors[i-1][0] + minimum, mini_idx])

print(colors)
    
# for i in range(1, N):
#     temp = []
#     if colors[i-1][0][1] == 0:
#         if colors[i-1][0][0] + grid[i][1] <= colors[i-1][0][0] + grid[i][2]:
#             temp.append([colors[i-1][0][0] + grid[i][1], 1])
#         else:
#             temp.append([colors[i-1][0][0] + grid[i][2], 2])
#     elif colors[i-1][0][1] == 1:
#         if colors[i-1][0][0] + grid[i][0] <= colors[i-1][0][0] + grid[i][2]:
#             temp.append([colors[i-1][0][0] + grid[i][0], 0])
#         else:
#             temp.append([colors[i-1][0][0] + grid[i][2], 2])
#     else:
#         if colors[i-1][0][0] + grid[i][0] <= colors[i-1][0][0] + grid[i][1]:
#             temp.append([colors[i-1][0][0] + grid[i][0], 0])
#         else:
#             temp.append([colors[i-1][0][0] + grid[i][1], 1])
            
#     if colors[i-1][1][1] == 0:
#         if colors[i-1][1][0] + grid[i][1] <= colors[i-1][1][0] + grid[i][2]:
#             temp.append([colors[i-1][1][0] + grid[i][1], 1])
#         else:
#             temp.append([colors[i-1][1][0] + grid[i][2], 2])
#     elif colors[i-1][1][1] == 1:
#         if colors[i-1][1][0] + grid[i][0] <= colors[i-1][1][0] + grid[i][2]:
#             temp.append([colors[i-1][1][0] + grid[i][0], 0])
#         else:
#             temp.append([colors[i-1][1][0] + grid[i][2], 2])
#     else:
#         if colors[i-1][1][0] + grid[i][0] <= colors[i-1][1][0] + grid[i][1]:
#             temp.append([colors[i-1][1][0] + grid[i][0], 0])
#         else:
#             temp.append([colors[i-1][1][0] + grid[i][1], 1])
    
#     if colors[i-1][2][1] == 0:
#         if colors[i-1][2][0] + grid[i][1] <= colors[i-1][2][0] + grid[i][2]:
#             temp.append([colors[i-1][2][0] + grid[i][1], 1])
#         else:
#             temp.append([colors[i-1][2][0] + grid[i][2], 2])
#     elif colors[i-1][2][1] == 1:
#         if colors[i-1][2][0] + grid[i][0] <= colors[i-1][2][0] + grid[i][2]:
#             temp.append([colors[i-1][2][0] + grid[i][0], 0])
#         else:
#             temp.append([colors[i-1][2][0] + grid[i][2], 2])
#     else:
#         if colors[i-1][2][0] + grid[i][0] <= colors[i-1][2][0] + grid[i][1]:
#             temp.append([colors[i-1][2][0] + grid[i][0], 0])
#         else:
#             temp.append([colors[i-1][2][0] + grid[i][1], 1])
#     colors.append(temp)





