INF = int(1e9)

graph = [
    [0, 5, INF, 8],
    [7, 0, 9, INF],
    [2, INF, 0, 4],
    [INF, INF, 3, 0]
]
n = 4
def floydwarshall(n, graph):
    # 결과 그래프를 초기화
    d = graph
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][k]+d[k][j], d[i][j])
    
    for i in d:
        print(i)

floydwarshall(n, graph)
