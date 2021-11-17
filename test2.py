def solution(grid, clockwise):
    answer = []
    dic = {}
    count = 1
    for j in grid:
        for i in range(1,len(j)+1):
            dic[j[i-1]] = count
            count += 1
            
        
    return dic

grid = ["1","234","56789"]
clockwise = True

# 5 762 98431
print(solution(grid, clockwise))