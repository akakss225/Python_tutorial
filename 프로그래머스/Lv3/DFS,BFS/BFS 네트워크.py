# IDEA
# 1. 일단 모든 노드를 다 돌아봐야함. >> n개의 노드가 있다는 것은 최대 n개의 네트워크가 존재한다는 의미
# 2. 즉, 노드간 연결이 없어도 각각의 네트워크는 따로존재 >> 이를 카운트 하기위해 모든 노드를 다 봐야함
# 3. BFS로 인접한 노드를 확인 하고 넘어가야함.
# 4. 인접 노드가 더이상 없다고 판단 되는 순간 answer += 1

from collections import deque

def solution(n, computers):
    answer = 0
    visit = [0] * n
    q = deque()
    
    while 0 in visit:
        q.append(visit.index(0))
        while q:
            cur = q.popleft()
            visit[cur] = 1
            for i in range(n):
                if computers[cur][i] == 1 and visit[i] == 0:
                    q.append(i)
        answer += 1
    
    return answer


n = 3
c = [
    [1, 1, 0], 
    [1, 1, 0], 
    [0, 0, 1]
    ]

print(solution(n, c))