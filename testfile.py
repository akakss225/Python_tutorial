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

# def solution(n, edge):
#     vertex = dict()
#     for i in range(len(edge)):
#         if edge[i][0] in vertex:
#             vertex[edge[i][0]].append(edge[i][1])
#         else:
#             vertex[edge[i][0]] = [edge[i][1]]
#         if edge[i][1] in vertex:
#             vertex[edge[i][1]].append(edge[i][0])
#         else:
#             vertex[edge[i][1]] = [edge[i][0]]
#     route = []
#     stack = [1]
#     visite = []
#     level = 0
#     while stack:
#         cur = stack.pop()
#         if cur not in visite:
#             visite.append(cur)
#             stack.extend(vertex[cur])
#             level += 1
#         elif cur in visite and cur in stack:
#             route.append(level)
        
#     return route


# vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
# n = 6
# print(solution(n, vertex))

# phone = ["12","123","1235","567","88"]


def solution(param0):
    temp1 = []
    list1 = []
    for i in range(len(param0)):
        for j in range(1, len(param0[i])):
            if param0[i][-j] == '/':
                list1.append(param0[i][:-j:-1])
                break
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            temp1.append([list1[i][len(list1[i])-1],list1[i][0]])
            break
    temp = []
    for i in temp1:
        temp.append('.'.join(i))
    dic = {}
    for i in temp:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 0
    answer = []
    for i in dic:
        if dic[i] > 0:
            answer.append(i)
            answer.append('%s'%dic[i])
    
    return answer
    
param0 = ['/a/a_v2.x', '/b/a.x', '/c/t.z', '/d/a/t.x', '/e/z/t_v1.z', '/k/k/k/a_v9.x']
param0 = ['/t.z', '/z/z_v2.z', '/a.z', '/d/b.z', '/d/a/t.z']

print(solution(param0))

