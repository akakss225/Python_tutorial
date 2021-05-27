# Dijkstra << 탐욕 알고리즘(greedy Algorithm)
# 네비게이팅 프로그램에 사용됨

# 그래프를 정의한다.(이 그래프는 양방향이다.)

graph = [(0, 1, 7), (0, 4, 3), (0, 5, 10), (1, 2, 4), (1, 4, 2), 
         (1, 5, 6), (1, 3, 10), (2, 3, 2),(3, 5, 9), (3, 6, 4), (4, 6, 5)]
nodes = set()
for node in graph:
    nodes.add(node[0])
    nodes.add(node[1])

# 방문한 노드를 기록하기 위한 집합을 만든다.
visits = set()

# 출발점에서 모든 노드와 거리는 무한대로 설정하고 각 노드의 부모노드는 "모름"으로 초기설정한다.

cost = {}

for node in nodes:
    cost[node] = [float("inf"),None]

# 시작과 끝 노드를 정의한다.
start = 0
end = 3

# 시작노드의 거리는 0으로 설정한다.
curNode = start
cost[curNode][0] = 0    

def _neighbor(curNode):
    # curNode에 연결된 이웃노드를 리스트로 리턴한다.
    neighbor = {}
    for node in graph:
        if node[0] == curNode:
            neighbor[node[1]]= node[2]
        elif node[1] == curNode:
            neighbor[node[0]] = node[2]
    return neighbor

def _getWeight(n1, n2):
    # 그래프에서 노드 n1, n2의 가중값을 리턴한다.
    for node in graph:
        if node[0] == n1 and node[1] == n2:
            return node[2]
        elif node[0] == n2 and node[1] == n1:
            return node[2]
    return None

def dicFilter(cost, nodes):
    import sys
    mini = sys.maxsize
    for key, value in cost.items():
        if key in nodes:
            if value[0] < mini:
                mini = value[0]
                curNode = key
    return curNode

while True:        
    visits.add(curNode)
    nodes.remove(curNode)
    neighbors = _neighbor(curNode)
    # 모든 이웃에 대해 현재 노드를 통해 이웃노드에 접근하는 cost가 더 작을 경우, cost 값을 갱신하고 부모노드를 변경한다.
    for node in neighbors:
        if cost[curNode][0] + _getWeight(curNode,node) < cost[node][0]:
            cost[node][0] = cost[curNode][0] + _getWeight(curNode, node)
            cost[node][1] = curNode
            
    if len(nodes) > 0:
        curNode = dicFilter(cost, nodes)
    else:
        break

path = [end]

while end != start:
    path.append(cost[end][1])
    end = cost[end][1]

print(path[::-1])