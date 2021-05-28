class Dijkstra:
    def __init__(self,nodes):
        self.g = {}
        self.dist = {}
        self.nodes = ()
        for node in nodes:
            self.g[node] = {}
            self.dist[node] = [float("inf"), "none"]

    def setEdge(self,a,b,w,bidirection=True):
        self.g[a][b] = w
        if bidirection == True: self.g[b][a] = w

    def getPath(self,start,end):
        dictfilt = lambda x, y: dict([(i, x[i]) for i in x if i in set(y)])
        visits = set()
        curNode = start
        self.dist[curNode][0] = 0
        while True:
            visits.add(curNode)
            self.nodes.remove(curNode)
            neighbors = self.g[curNode]

            for node in neighbors:
                if min(self.dist[node][0], self.dist[curNode][0] + self.g[curNode][node]) < self.dist[node][0]:
                    self.dist[node][0] = min(self.dist[node][0], self.dist[curNode][0] + self.g[curNode][node])
                    self.dist[node][1] = curNode

            if len(self.nodes) > 0:
                curNode = min(dictfilt(self.dist, self.nodes), key=dictfilt(self.dist, self.nodes).get)
            else:
                break

        path = [end]
        dist = []

        while end != start:
            path.append(self.dist[end][1])
            dist.append(self.dist[end][0])
            end = self.dist[end][1]

        return path[::-1], dist[::-1]

