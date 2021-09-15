from Algorithm.다익스트라 import INF


class Dijkstra:
    def __init__(self, graph = None, n = None, visit = None, distance = None):
        INF = int(1e9)
        self.graph = [
            [0, INF, INF, INF, INF, INF, INF, INF, 1, INF, 1, 1], # 숫자패드 0
            [INF, 0, 1, INF, 1, INF, INF, INF, INF, INF, INF, INF], # 숫자패드 1
            [INF, 1, 0, 1, INF, 1, INF, INF, INF, INF, INF ,INF], # 숫자패드 2
            [INF, INF , 1, 0, INF , INF, 1, INF, INF, INF, INF, INF ], # 숫자패드 3
            [INF, 1, INF, INF, 0, 1, INF, 1, INF, INF, INF, INF], # 숫자패드 4
            [INF, INF, 1, INF, 1, 0, 1, INF, INF, INF, INF, INF], # 숫자패드 5
            [INF, INF, INF, 1, INF, 1, 0, INF, INF, 1, INF, INF], # 숫자패드 6
            [INF, INF, INF, INF, 1, INF, INF, 0, 1, INF, 1, INF], # 숫자패드 7
            [INF, INF, INF, INF, INF, 1, INF, 1, 0, 1, INF, INF], # 숫자패드 8
            [INF, INF, INF, INF, INF, INF, 1, INF, 1, 0, INF, 1], # 숫자패드 9
            [1, INF, INF, INF, INF, INF, INF, 1, INF, INF, 0, INF], # 숫자패드 *
            [1, INF, INF, INF, INF, INF, INF, INF, INF, 1, INF, 0] # 숫자패드 #
        ]
        self.n = len(self.graph)
        self.visit = [False] * self.n
        self.distance = [INF] * self.n
        
    def getSmall(self):
        mini = INF
        index = 0
        for i in range(self.n):
            if self.distance[i] < mini and self.visit[i] != True: # start의 경우 0이므로, 이를 베제하기 위함.
                mini = self.distance[i]
                index = i
        return index
    
    def getDijkstra(self):
        for i in range(self.n):
            for j in range(self.n):
                self.distance[i] = self.graph[j][i]
        self.visit[start] = True
        for i in range(n):
            cur = self.getSmall(d)
            self.visit[cur] = True
            for j in range(n):
                if self.visit[j] != True:
                    if d[cur] + self.graph[cur][j] < d[j]:
                        d[j] = d[cur] + self.graph[cur][j]
        return 