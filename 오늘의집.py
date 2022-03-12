from collections import deque

# 1
def solution(pro,  pur):
    d = dict()
    priority = dict()
    for i in pro:
        temp = i.split()
        d[temp[0]] = temp[1:]
        d[temp[0]].append(0)
        for j in temp[1:]:
            if j not in priority:
                priority[j] = 0
    
    for i in pur:
        for j in d[i][:-1]:
            priority[j] += 1
        del d[i]
    
    priority = sorted(priority.items(), key=lambda x:x[0])
    priority = sorted(priority, key=lambda x:x[1], reverse=True)
    priority = dict(priority)
    
    com = len(priority) + 1
    add = 0
    for i in priority:
        priority[i] += (com - add)
        add += 1
    
    for i in priority:
        for j in d:
            if i in d[j]:
                d[j][-1] += priority[i]
    
    check = 0
    length = 0
    for i in d:
        if d[i][-1] > check:
            if len(d[i]) >= length:
                check = d[i][-1]
                answer = i
                length = len(d[i])
            else:
                continue
    return answer

products = ["sofa red long", "blanket blue long", "towel red", "mattress long", "curtain blue long cheap"]
purchased = ["towel", "mattress", "curtain"]

print(solution(products, purchased))



# 2
a = [[1,2],[2,2],[3,2]]

for i in range(len(a)-1, -1, -1):
    print(a[i])