def solution(param0):
    temp1 = []
    list1 = []
    for i in range(len(param0)):
        for j in range(-1, -len(param0[i])-1,-1):
            if param0[i][j] == '/':
                list1.append(param0[i][:j:-1])
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
            dic[i] = 1
    answer = []
    for i in dic:
        if dic[i] > 1:
            answer.append(i)
            answer.append('%s'%dic[i])
    
    return answer
    
param0 = ['/a/a_v2.x', '/b/a.x', '/c/t.z', '/d/a/t.x', '/e/z/t_v1.z', '/k/k/k/a_v9.x']
param0 = ['/t.z', '/z/z_v2.z', '/a.z', '/d/b.z', '/d/a/t.z']

print(solution(param0))