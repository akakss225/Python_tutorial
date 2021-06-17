# 깊이우선탐색, Stack을 이용해 구현함.

def dfs(graph, v, visited): # 정보가 기록된 graph와, 시작할 노드, 방문처리를 진행할 리스트 세가지를 인자로 사용한다.
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=" ")
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    # 현재 노드와 연결된 다른 노드를 전부 방문했다면, 이전에 스택에 쌓여있던 함수를 진행함.
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i , visited)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9
dfs(graph, 1, visited)
