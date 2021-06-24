'''
1. 논리적 추론 == 거짓말 A, 빵먹 B

2. 페턴찾기 == 답 71

3. 반복구조 답 == 15

4. 조건식 == count < 101

5. 논리식 == 3번 (year % 4 != 0 && year % 100 == 0) || year % 400 != 0
'''

# 6 번 구현
'''
arr = [3,2,4,4,2,5,2,5,5]
answer = [0] * len(arr)
result = []

for i in arr:
    answer[i-1] += 1
for i in answer:
    if i > 1:
        result.append(i)
if result:
    print(result)
else:
    print(-1) 
'''
'''
graph = [
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

vertax = []

for i in enumerate(graph, start= 1):
    vertax.append(i)
    
print(vertax)
'''

# p1 = [1,2,3,4,5] * 8
# p2 = [2,1,2,3,2,4,2,5] * 5
# p3 = [3,3,1,1,2,2,4,4,5,5] * 4

# print(list(zip(p1,p2,p3)))

def solution(n, edge):
    vertex = dict()
    for i in range(len(edge)):
        if edge[i][0] in vertex:
            vertex[edge[i][0]].append(edge[i][1])
        else:
            vertex[edge[i][0]] = [edge[i][1]]
        if edge[i][1] in vertex:
            vertex[edge[i][1]].append(edge[i][0])
        else:
            vertex[edge[i][1]] = [edge[i][0]]
    route = []
    stack = [1]
    visite = []
    level = 0
    while stack:
        cur = stack.pop()
        if cur not in visite:
            visite.append(cur)
            stack.extend(vertex[cur])
            level += 1
        elif cur in visite and cur in stack:
            route.append(level)
        
    return route


vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
n = 6
print(solution(n, vertex))