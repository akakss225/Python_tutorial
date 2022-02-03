#  크리마 시험문제

# 1
from collections import deque
import datetime
import re

from appscript import con

def preprocessDate(dates):
    for i in range(len(dates)):
        a = dates[i].split(" ")
        date = re.findall(r'\d+', a[0])[0] + " " + a[1] + " " + a[2]
        result = datetime.datetime.strptime(date, "%d %b %Y").strftime("%Y-%m-%d")
        dates[i] = result
    return dates
    
dates = ["20th Oct 2052", "6th Jun 1933", "26th May 1960", "20th Sep 1958"]

# 2

def findRange(num):
    num_str1 = str(num)
    num_str2 = str(num)
    max_num = 0
    min_num = 0
    # find max
    if num_str1[0] == "9":
        for i in range(1, len(num_str1)):
            if num_str1[i] != "9":
                max_num = num_str1[i]
                break
    else:
        max_num = num_str1[0]
    
    if max_num == 0:
        max_num = "9"
    # find min
    if num_str2[0] == "1":
        for i in range(1, len(num_str2)):
            if num_str2[i] != "0" and num_str2[i] != "1":
                min_num = num_str2[i]
                break
    else:
        min_num = num_str2[0]
    
    if min_num == 0:
        min_num = "1"
    
    max = num_str1.replace(max_num, "9")
    if num_str2.index(min_num) == 0:
        min = num_str2.replace(min_num, "1")
    else:
        min = num_str2.replace(min_num, "0")
    
    return int(max) - int(min)

num = 999999999
num = 909
print(findRange(num))

# 3

def countMatches(grid1, grid2):
    # 상 하 좌 우
    y = [0, 1, 0 , -1]
    x = [1, 0, -1, 0]
    
    g1 = []
    check_g1 = [[False] * len(grid1[0]) for i in range(len(grid1))]
    g2 = []
    check_g2 = [[False] * len(grid2[0]) for i in range(len(grid2))]
    
    
    for i in range(len(grid1)):
        for j in range(len(grid1[0])):
            cur_x = j
            cur_y = i
            if cur_y == 0 and cur_x == 0:
                check_g1[cur_y][cur_x] = True
                if grid1[cur_y][cur_x] == "1":
                    g1.append([cur_x, cur_y])
            for k in range(4):
                next_y = y[k] + cur_y
                next_x = x[k] + cur_x
                if 0 <= next_x < len(grid1[0]) and 0 <= next_y < len(grid1):
                    if check_g1[next_y][next_x] == False and grid1[next_y][next_x] == "1":
                        g1.append([next_x, next_y])
                        check_g1[next_y][next_x] = True
                        
    for i in range(len(grid2)):
        for j in range(len(grid2[0])):
            cur_x = j
            cur_y = i
            if cur_y == 0 and cur_x == 0:
                check_g2[cur_y][cur_x] = True
                if grid2[cur_y][cur_x] == "1":
                    g2.append([cur_x, cur_y])
            for k in range(4):
                next_y = y[k] + cur_y
                next_x = x[k] + cur_x
                if 0 <= next_x < len(grid2[0]) and 0 <= next_y < len(grid2):
                    if check_g2[next_y][next_x] == False and grid2[next_y][next_x] == "1":
                        g2.append([next_x, next_y])
                        check_g2[next_y][next_x] = True
    
    return g2

def bfs(y, x, check, grid):
    result = []
    dy = [0, 1, 0 , -1]
    dx = [1, 0, -1, 0]
    
    q = deque([[y, x]])
    check[y][x] = True
    while q:
        cur_y, cur_x = q.popleft()
        result.append([cur_x, cur_y])
        for k in range(4):
            next_y = dy[k] + cur_y
            next_x = dx[k] + cur_x
            if 0 <= next_x < len(grid[0]) and 0 <= next_y < len(grid):
                if grid[next_y][next_x] == "1" and check[next_y][next_x] == False:
                    check[next_y][next_x] = True
                    q.append([next_y, next_x])
    return result

def countMatches(grid1, grid2):
    answer = 0
    g1 = []
    check_g1 = [[False] * len(grid1[0]) for i in range(len(grid1))]
    g2 = []
    check_g2 = [[False] * len(grid2[0]) for i in range(len(grid2))]
    
    for i in range(len(grid1)):
        for j in range(len(grid1[0])):
            if grid1[i][j] == "1" and check_g1[i][j] == False:
                g1.append(bfs(i, j, check_g1, grid1))
    for i in range(len(grid2)):
        for j in range(len(grid2[0])):
            if grid2[i][j] == "1" and check_g2[i][j] == False:
                g2.append(bfs(i, j, check_g2, grid2))
    
    for i in g1:
        if i in g2:
            answer += 1    
    
    return answer

grid1 = ["001", 
         "011", 
         "100"]

grid2 = ["001", 
         "011", 
         "101"]

print(countMatches(grid1, grid2))

# 4
# 가장 큰 숫자는 일단 활성화
# 그리고 나머지 남은 길이에서 그다음 큰 숫자를 활성화
# 반복
def findMax(l, check):
    
    max_list = []
    max_num = max(l)
    for i in range(len(l)):
        if l[i] == max_num:
            max_list.append([l[i], i])
    
    compare = []
    for i in max_list:
        if i[0] + i[1] > len(l) - 1:
            end = len(l) - 1
        else:
            if check[i[0] + i[1]] == False:
                end = i[0] + i[1]
            else:
                j = 1
                while check[i[0] + i[1] - j] == True and i[0] + i[1] - j > i[1]:
                    j += 1
                end = i[0] + i[1] - j
        if i[1] - i[0] < 0:
            start = 0
        else:
            if check[i[1] - i[0]] == False:
                start = i[1] - i[0]
            else:
                j = 1
                while check[i[1] - i[0] + j] == True and i[1] - i[0] + j < i[1]:
                    j += 1
                start = i[1] - i[0] + j
        compare.append(end-start)
    
    max_idx = max_list[compare.index(max(compare))][1]
    # 청산하기
    if max_idx + max_num > len(l) - 1:
        end = len(l) - 1
    else:
        end = max_idx + max_num
    if max_idx - max_num < 0:
        start = 0
    else:
        start = max_idx - max_num
    for i in range(start, end + 1):
        l[i] = -1
        check[i] = True

def findMax(l, check):
    max_list = []
    for i in range(len(l)):
        if l[i] == -1:
            max_list.append(-1)
            continue
        if l[i] == 0:
            max_list.append(1)
            continue
        
        start = 0 
        end = 0
        b = f = 0
        countb = countf = 0
        while b <= l[i] and i - b >= 0:
            if check[i - b] == False:
                b += 1
                countb += 1
            else:
                b += 1
        while f <= l[i] and i + f <= len(l) - 1:
            if check[i + f] == False:
                f += 1
                countf += 1
            else:
                f += 1
        
        
        max_list.append(countb + countf - 1)
        
    max_idx = max_list.index(max(max_list))
    max_num = l[max_idx]
    
    if max_idx - max_num < 0:
        start = 0
    else:
        start = max_idx - max_num
    if max_idx + max_num > len(l) - 1:
        end = len(l) - 1
    else:
        end = max_idx + max_num
    
    for i in range(start, end + 1):
        l[i] = -1
        check[i] = True
    
def fountainActivation(locations):
    answer = 0
    n = len(locations)
    check = [False] * n
    
    while False in check:
        findMax(locations, check)
        answer += 1
    return answer
    


locations = [
    1,1,1,2,3,1,3,2,4,5,1,2,13,2,14,11,
    2,3,1,2,4,5,6,1,2,3,4,6,1,2,3,1,0,0,
    0,1,2,3,0,0,1,14,14,1,2,4,3,4,5,7,1,
    2,3,4,35,36,37,38,3,12,3,4,1,23,4,6,1,
    2,3,41,2,3,4,1,23,4,6,1,2,5,5,1,23,5,6,
    7,1,3,5,1,23,5,6,1,23,4,52
    ]
locations = [
    4,1,2,1,3,0,0,0,0,0,1,2,
    6,2,3,4,1,5,6,7,1,2,3,4,6,1,4,1,2,3,4,15
    ]
locations = [
    4,1,2,1,3,0,0,0,0,0,1,2,
    2,3,4,1,5,6,5,4,1,2,3,4,10
    ]
# locations = [1, 1, 1]
print(fountainActivation(locations))



# 5
# x + y = a
# x XOR y = b

def bitwiseEquations(a, b):
    answer = []
    # list a 의 길이만큼 반복문 실행 >> len(a) == len(b)
    for i in range(len(a)):
        # 반복문 진행마다 결과값을 담을 result변수 초기화
        result = 0
        
        # x값이 a[i] 의 반일때 까지만 실행 >> 넘어가면 결국 같아지기 떄문
        for j in range(1, a[i] // 2 + 1):
            # x + y = a[i] 가 되게 설정 >> x가 0인 경우는 skip
            x = j
            y = a[i] - j
            # x ^ y (x XOR y) == b[i] 인 경우 result에 담아주고 반복문 탈출 >> x 가 최소인 경우만을 찾음
            # break를 안거치고, for 문을 끝까지 돌면, result = 0 인 상태로 빠져나감
            if x ^ y == b[i]:
                result = (2 * x) + (3 * y)
                break
        # list에 순서대로 append
        answer.append(result)
    return answer

a = [4, 3, 57]
b = [2, 4, 49]
a = [15, 139, 22]
b = [15, 75, 22]
a = [22, 15]
b = [22, 15]
print(bitwiseEquations(a, b))



# 6

# dfs를 이용해 가장 edge가 많은 node로부터의 모든 경로를 찾아준다
def dfs(node, graph):
    
    result = []
    for i in graph[node]:
        s = [i]
        route = [node]
        
        while True:
            cur = s.pop()
            
            if cur not in route:
                route.append(cur)
                s.extend(graph[cur])
            else:
                result.append(route)
                break
    return result

def hospital(city_nodes, city_from, city_to):
    # 각 노드당 연결된 양방향 그래프를 만들어준다
    d = {}
    for i in range(len(city_from)):
        if city_from[i] in d:
            d[city_from[i]].add(city_to[i])
        else:
            d[city_from[i]] = set([city_to[i]])
        if city_to[i] in d:
            d[city_to[i]].add(city_from[i])
        else:
            d[city_to[i]] = set([city_from[i]])

    # 가장 많은 edge를 가지고있는 노드를 찾아준다
    max_list = 0
    for i in d:
        if max_list < len(d[i]):
            max_list = len(d[i])
            max_idx = i
    
    # 가장 많은 edge를 가지고있는 노드로부터 시작해 모든 경로를 구해준다
    check = dfs(max_idx, d)
    install = [0] * city_nodes
    
    # 각 경로로부터 마지막 노드의 위쪽 노드부터 hospital을 건설해준다
    # 만약 인접 노드에 hospital이 있다면, 건너 뛴다.
    # 이후 인접노드에 겹쳐지는 hospital을 제거해준다.
    for i in check:
        for j in range(-1, -len(i)-1, -1):
            if j % 2 == 0:
                install[i[j] - 1] = 1
    
    
    return install.count(1)


print(hospital(6, [6, 1, 2, 4, 2, 2], [5, 2, 3, 2, 5, 6]))


