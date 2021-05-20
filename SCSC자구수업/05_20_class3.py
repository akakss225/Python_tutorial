'''
최소비용신장트리
간선에 가중치가 존재하는 가중치 그래프에서 가중치의 합이 최소화되도록 구성한 트리를 말한다.
최소비용신장트리는 두개의 정점사이에 한개 경로만 존재한다. 그러므로 싸이클도 존재할 수 없다.
복잡한 그래프에서 최소비용신장트리를 구성하는 것은 네트워크가 작동할 수 있는 최소 조건을 구하는 의미가 있다.
최소비용신장트리를 구하는 방법으로는 Kruskal 알고리즘, Prim 알고리즘, Sollin 알고리즘 등이 있다.


Kruskal 알고리즘

간선들의 가중값을 정렬한 후, 가장 작은 가중값을 가지는 간선부터 추가해 간다.
추가중에 간선의 수가 n-1이 되면 알고리즘이 종료된다. n은 노드 수다.
위의 그림에서 최소 간선 (4,6) 부터 차례대로 빈 트리에 삽입한다.
삽입과정에서 (1,4), (2,4), (3,6)은 싸이클이 형성되므로 스킵한다.
삽입하다가 삽입된 간선이 6개(노드수-1)가 되면 알고리즘이 종료된다.
싸이클을 탐지하는 방법으로 Union-Find 알고리즘을 사용할 수 있다.


Union Find Algorithm

Union Find 알고리즘은 노드 연결을 나타내는 리스트를 정의하고 추가 되는 엣지(n1, n2)에 대해 Union 해 간다.
예를 들어, 현재 [[0,1,2],[3,4]] 이 존재할 때, 아래와 같이 처리한다.
[[0,1,2],[3,4]] + [5,6] = [[0,1,2],[3,4],[5,6]] # 연결할 수 없으므로 따로 생성
[[0,1,2],[3,4]] + [1,5] = [[0,1,2,5],[3,4]] # 존재하는 곳에 연결함
[[0,1,2],[3,4]] + [1,3] = [[0,1,2,3,4]] # n1, n2 모두 존재하므로 두개가 존재하는 서브 리스트를 합친다.
[[0,1,2],[3,4]] + [0,2] = 싸이클 # 0과 2가 모두 0번째로 같은 위치에 존재하므로 추가할 필요가 없고 이때 싸이클이 존재한다.
'''

def isCycle(u, n):
    idx1 = idx2 = -1
    n1 = n[0]
    n2 = n[1]
    for i in range(len(u)):
        if n1 in u[i]:
            idx1 = i
        if n2 in u[i]:
            idx2 = i

    if idx1 == -1 and idx2 == -1: # [n1,n2] 이 기존 리스트에 없다면 
        u.append([n1,n2])
        print(u)
        return False
    elif idx1 == -1:              # [n1,n2] 이 기존 리스트 중 한 곳에만 있다면
        u[idx2].append(n1)
        print(u)
        return False
    elif idx2 == -1:              # [n1,n2] 이 기존 리스트 중 한 곳에만 있다면
        u[idx1].append(n2)
        print(u)
        return False
    elif idx1 != idx2:            # [n1,n2] 이 기존 리스트에 서로 다른 곳에 존재한다면 
        d1 = u[idx1]
        d2 = u[idx2]
        union = d1 + d2
        u.remove(d1)
        u.remove(d2)
        u.append(union)
        print(u)
        return False

    elif idx1 == idx2 and len(u[idx1]) > 2:# [n1,n2] 이 기존 리스트에 같은 곳에 존재한다면
        print(u)   
        return True

class SpanningTree:
    def __init__(self, graph):
        self.graph = graph
        self.nodes = set()
        self.union = [] # union-find 알고리즘에서 기존 엣지 리스트
        
        # 그래프의 노드를 구함
        for edge in graph:
            self.nodes.add(edge[0])
            self.nodes.add(edge[1])
        self.nNode = len(self.nodes)

    def isCycle(self, n1, n2):
        idx1 = idx2 = -1
        for i in range(len(self.union)):
            if n1 in self.union[i]:
                idx1 = i
            if n2 in self.union[i]:
                idx2 = i

        if idx1 == -1 and idx2 == -1:
            self.union.append([n1, n2])
            return False
        elif idx1 == -1:
            self.union[idx2].append(n1)
            return False
        elif idx2 == -1:
            self.union[idx1].append(n2)
            return False
        elif idx1 != idx2:
            d1 = self.union[idx1]
            d2 = self.union[idx2]
            union = d1 + d2
            self.union.remove(d1)
            self.union.remove(d2)
            self.union.append(union)
            return False
        elif idx1 == idx2 and len(self.union[idx1]) > 2:
            print(self.union[idx1])
            return True
        else:
            return False

    def kruskal(self):
        self.graph.sort(key = lambda t: t[2]) # 그래프를 2번째 원소기준으로 소트한다.
        tree = []  # 최소비용신장트리를 담을 리스트를 만든다.
        nedges = 0 # nedges == self.nNode - 1이면 알고리즘이 끝난다.
        i = 0
        while nedges < self.nNode - 1:
            if self.isCycle(self.graph[i][0],self.graph[i][1]) == False:
                tree.append(self.graph[i])
                nedges += 1
            else:
                print("싸이클 발견",self.graph[i] )
            i += 1

        return tree


class _SpanningTree:
    def __init__(self, graph):
        self.graph = graph
        self.nodes = set() # 그래프의 노드 집합
        self.union = [] # 싸이클 여부를 판단하는 리스트

        for edge in graph: # 모든 그래프의 엣지에 대해 노드를 추출해 nodes 집합에 저장한다.
            self.nodes.add(edge[0])
            self.nodes.add(edge[1])
        self.nNode = len(self.nodes) # 그래프에 존재하는 노드의 수

    # union 리스트에 Union-Find 알고리즘의 결과를 저장하면서 싸이클 발생 여부를 리턴한다.
    # 새로 입력된 엣지 (n1, n2)가 union 리스트에 어느 곳에 있는지를 판단하여 idx1, idx2를 생성한다.

    # idx1, idx2가 모두 -1이면 입력된 엣지가 union 집합에 있는 엣지들과 연결되어 있지 않으므로 새로운 엣지로 추가하고 싸이클 여부는 False다.
    # idx1, idx2 둘 중 하나가 -1이면 하나는 연결되어 있고 하나는 새 노드이므로 연결되어 있는 노드집합에 추가하고 싸이클 여부는 False다.
    # idx1, idx2 둘 다 0 이상이고, 서로 다른 값을 가지면, 두 노드 집합을 연결하고 싸이클 여부는 False다.
    # idx1, idx2 둘 다 0 이상이고, 서로 같은 값을 가지면, 싸이클 여부는 True 이므로 엣지를 추가하지 않는다.
    def isCycle(self, n1, n2):
        idx1 = idx2 = -1
        for i in range(len(self.union)):
            if n1 in self.union[i]:
                idx1 = i
            if n2 in self.union[i]:
                idx2 = i

        if idx1 == -1 and idx2 == -1:
            self.union.append([n1, n2])
            return False
        elif idx1 == -1:
            self.union[idx2].append(n1)
            return False
        elif idx2 == -1:
            self.union[idx1].append(n2)
            return False
        elif idx1 != idx2:
            d1 = self.union[idx1]
            d2 = self.union[idx2]
            union = d1 + d2
            self.union.remove(d1)
            self.union.remove(d2)
            self.union.append(union)
            return False
        elif idx1 == idx2 and len(self.union[idx1]) > 2:
            return True
        else:
            return False

    def kruskal(self):
        self.graph.sort(key = lambda t: t[2]) # edge 크기로 그래프를 소트한다.
        tree = []
        nedges = 0
        i = 0
        while nedges < self.nNode - 1:
            if self.isCycle(self.graph[i][0],self.graph[i][1]) == False:
                tree.append(self.graph[i])
                nedges += 1
            else:
                print("cycle found",self.graph[i] )
            i += 1
        return tree

    # 최소비용신장트리 과정에서 남아 있는 엣지(remains) 들 중에 nodes에 연결된 최소비용 엣지를 구해 리턴한다.
    def _minEdge(self, remains, nodes):
        import sys
        mini = sys.maxsize
        for node in nodes:
            for edge in remains:
                if edge[0] == node or edge[1] == node: # 노드와 연결된 엣지이고
                    if edge[2] < mini: # 최소비용 엣지이면 ... 
                        minEdge = edge
                        mini = minEdge[2]
        return minEdge

    # 최소비용신장트리 mst에 존재하는 노드의 집합을 구해 리턴한다.
    def _getNodes(self, mst):
        nodes = []
        for edge in mst:
            nodes.append(edge[0])
            nodes.append(edge[1])
        return nodes

    # Prim 알고리즘으로 최소비용신장트리를 구한다.
    def prim(self):
        mst = [] # 최소비용신장트리를 저장할 리스트
        self.union = [] # 싸이클 여부를 판단할 리스트
        self.graph.sort(key=lambda t: t[2]) # 그래프를 소트해서 최소비용 엣지하나를 구함
        if self.isCycle(self.graph[0][0], self.graph[0][1]) == False:
            mst.append(self.graph[0]) # 첫번째 엣지를 mst에 추가

        remains = list(set(self.graph) - set(mst)) # 그래프에서 mst를 제외한 집합으로 remains에서 엣지를 선택해 mst에 추가할 것임
        nodes = self._getNodes(mst) # 현재, mst에 존재하는 노드집합을 구함
        minEdge = self._minEdge(remains, nodes) # 현재, mst에 존재하는 노드와 연결된 엣지들 중에 최소비용 엣지를 구함

        while len(mst) < self.nNode - 1:
            if self.isCycle(minEdge[0], minEdge[1]) == False: # 최소비용 엣지가 싸이클을 형성하지 않으면 mst에 추가
                mst.append(minEdge)
            remains.remove(minEdge) # 싸이클을 형성 여부와 상관없이 remains에서 제거
            #print(mst)
            nodes = self._getNodes(mst) # 업데이트된 mst와 remains를 이용하여 최소비용엣지를 구하고 루프를 반복함
            minEdge = self._minEdge(remains, nodes)

        return mst

g = [(0,1,9),(0,2,10),(1,3,10),(1,4,5),(1,6,3),(2,3,9),(2,4,7),(2,5,2),(3,5,4),(3,6,8),(4,6,1),(5,6,6)]
t = SpanningTree(g)
print(t.kruskal())

g = [(0,1,9),(0,2,10),(1,3,10),(1,4,5),(1,6,3),(2,3,9),
     (2,4,7),(2,5,2),(3,5,4),(3,6,8),(4,6,1),(5,6,6)]
t = _SpanningTree(g)
print(t.kruskal())
print(t.prim())