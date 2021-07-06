n = 6

INF = int(1e9)

graph = [
    [0, 2, 5, 1, INF, INF],
    [2, 0, 3, 2, INF, INF],
    [5, 3, 0, 3, 1, 5],
    [1, 2, 3, 0, 1, INF],
    [INF, INF, 1, 1, 0, 2],
    [INF, INF, 5, INF, 2, 0]
]

visit = [False]*n # 방문 여부 확인
distance = [INF] * n # 최단거리 저장

# 가장 최소 거리를 가지는 정점을 반환합니다.
def getSmall(distance):
    mini = INF
    index = 0
    for i in range(n):
        if distance[i] < mini and visit[i] != True: # start의 경우 0이므로, 이를 베제하기 위함.
            mini = distance[i]
            index = i
    return index

def dijkstra(graph, n, start, visit): # 다익스트라 실제 구현 함수
    d = [INF] * n
    for i in range(n):
        d[i] = graph[start][i]
    visit[start] = True
    for i in range(n):
        cur = getSmall(d)
        visit[cur] = True
        for j in range(n):
            if visit[j] != True:
                if d[cur] + graph[cur][j] < d[j]:
                    d[j] = d[cur] + graph[cur][j]
    return d

print(dijkstra(graph, n, 0, visit))
