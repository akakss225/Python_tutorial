# IDEA
# 1. 주어진 input에 대하여 각 튜플의 길이별로 오름차순 정렬을 함. 이를 queue로 만듬.
# 2. 정렬이 된 s를 돌며, len() = 1 인 것은 무조건 맨 앞에 배치키고 popleft해줌.
# 3. queue에서 순차적으로 popleft를 하며, answer에 있으면 넘어가고 없으면 answer.append()해줌

from collections import deque

def solution(s):
    # 정답을 넣을 list
    answer = []
    
    # input data의 맨 앞과 맨 뒤는 {{ / }}이므로, 제거해줌
    s = s[2:-2]
    
    # data가 1개인 경우 바로 return
    if len(s) < 2:
        answer.append(int(s))
        return answer
    
    # 중간에 존재하는 },{로 split해준뒤, 길이에 따른 오름차순 정렬
    s = sorted(s.split("},{"), key=len)
    q = deque()
    
    # q에 각 숫자별로 split된 것을 넣어줌.
    for i in s:
        q.append(i.split(","))
        
    # 정답에 맨 처음에는 무조건 하나의 데이터만 있는것이 들어와야함
    answer.append(int(q.popleft()[0]))
    
    # q에서 popleft하며, q가 남아있지 않을때까지, 반복함
    while q:
        cur = q.popleft()
        
        # q에서 꺼낸 요소를 돌며,
        # answer에 있으면 넘어가고 없으면 순차적으로 넣어주는 반복을 함
        for i in cur:
            if int(i) in answer:
                continue
            else:
                answer.append(int(i))
    
    return answer

s = "{{2,1},{2},{2,1,3},{2,1,3,4}}"

print(solution(s))