from collections import deque as dq

while(dq):
    tmp = dq[0][1]
    dqList = [x[1] for x in dq]
    print(dqList)
    if(tmp == max(dqList)):
        cnt += 1
        if(dq[0][0] == m):
            dq.popleft()
            break
        else:
            dq.popleft()
    elif (tmp != max(dqList)):
        dq.popleft()
        dq.append(tmp)

print(cnt)