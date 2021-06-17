# BFS : 너비우선 탐색. Queue를 이용해서 구현
# 특히 이는 list에서 첫번째 인덱스의 값을 pop하기 때문에, 필시 deQueue시 O(N)의 시간을 쓰게 된다
# 따라서 시간복잡도를 개선하기 위해 collection 라이브러리를 이용해준다.

from collections import deque

def bfs(graph, start):
    visited = [] # 방문을 한 노드를 담아놓을 그릇
    queue = deque([start]) # 라이브러리를 이용해 손쉽게 deque 생성
    while queue: # queue가 빌 때 까지
        n = queue.popleft() # 꺼내고
        if n not in visited: # 꺼낸게 방문목록에 없다면
            visited.append(n) # 방문목록에 넣어주고
            queue += graph[n] - set(visited) # graph에 현재 꺼낸 값의 value값에서 방문하지 않은걸 queue에 넣어줌.
            # 위의 과정을 반복.
    return visited
    
graph = {1: set([3, 4]),
        2: set([3, 4, 5]),
        3: set([1, 5]),
        4: set([1]),
        5: set([2, 6]),
        6: set([3, 5])}
        
start = 1

print(bfs(graph, start))
