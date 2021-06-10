# Dijkstra << 탐욕 알고리즘(greedy Algorithm)
# 네비게이팅 프로그램에 사용됨

# 그래프를 정의한다.(이 그래프는 양방향이다.)

graph = [(0, 1, 7), (0, 4, 3), (0, 5, 10), (1, 2, 4), (1, 4, 2), 
         (1, 5, 6), (1, 3, 10), (2, 3, 2),(3, 5, 9), (3, 6, 4), (4, 6, 5)]

# 중복을 허용하지 않는 자료형 set를 사용
nodes = set()
for node in graph:
    # 각 노드 집합을 구하기
    nodes.add(node[0])
    nodes.add(node[1])
# nodes = [0,1,4,5,2,3,6] << 이는 graph에 존재하는 모든 node값이다.


# 방문한 노드를 기록하기 위한 집합을 만든다.
visits = set()

# 출발점에서 모든 노드와 거리는 무한대로 설정하고 각 노드의 부모노드는 "모름"으로 초기설정한다.
cost = {}
for node in nodes: # nodes = [0,1,4,5,2,3,6]
    # 딕셔너리로 cost를 지정해줌. 노드의 이름을 key값으로 사용하여, 순서대로 Key : cost , 부모 순서대로 넣어준다. 
    # 이때 아직 방문하지 않은 곳의 경우 충분히 큰 값을 넣어준다.
    cost[node] = [float("inf"),None]
# cost = {0 : [9999, None], 1 : [9999, None], 4 : [9999, None], 
#         5 : [9999, None], 2 : [9999, None], 3 : [9999, None],
#         6 : [9999, None]}



# 시작과 끝 노드를 정의한다.
start = 0
end = 3

# 시작노드의 거리는 0으로 설정한다.
curNode = start
cost[curNode][0] = 0    

def _neighbor(curNode):
    # curNode에 연결된 이웃노드를 리스트로 리턴한다.
    neighbor = {}
    # graph = [(0, 1, 7), (0, 4, 3), (0, 5, 10), (1, 2, 4), (1, 4, 2), 
    #      (1, 5, 6), (1, 3, 10), (2, 3, 2),(3, 5, 9), (3, 6, 4), (4, 6, 5)]
    for node in graph:
        # node[0] = 0 이면,
        if node[0] == curNode:
            # neighbor = {1 : 7}
            neighbor[node[1]]= node[2]
        # curNode 가 1이면,
        elif node[1] == curNode:
            # neighbor = {0 : 7}
            neighbor[node[0]] = node[2]
    return neighbor

def _getWeight(n1, n2):
    # 그래프에서 노드 n1, n2의 가중값을 리턴한다.
    # graph = [(0, 1, 7), (0, 4, 3), (0, 5, 10), (1, 2, 4), (1, 4, 2), 
    #         (1, 5, 6), (1, 3, 10), (2, 3, 2),(3, 5, 9), (3, 6, 4), (4, 6, 5)]
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


# 실제 다익스트라 알고리즘이 구현되는 코드
while True:
    # visits는 집합 자료형. 처음엔 비어있음
    visits.add(curNode)
    # 현재 목록에 존재하는 모든 node가 있는 집합. nodes = [0,1,4,5,2,3,6]
    nodes.remove(curNode)
    # 현재 선택된 노드(이 경우엔 start)의 인접 노드와 그 가중치를 구함.
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
