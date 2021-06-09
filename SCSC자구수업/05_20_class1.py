# 8ch
# Graph

# DFS(Depth First Search) : 깊이 우선 탐색 / 출발선에서 출발해 끝까지 갔다가 되돌아오면서 다른 방향을 모색하는 방법
# BFS(Breadth First Search) : 너비 우선 탐색 / 

class Stack:
    def __init__(self):
        self.s = []

    def push(self, item):
        self.s.append(item)

    def pop(self):
        if self.isEmpty() == False:
            return self.s.pop(-1)
        else:
            return None

    def peek(self):
        if self.isEmpty() == False:
            return self.s[-1]
        else:
            return None

    def isEmpty(self):
        if len(self.s) > 0:
            return False
        else:
            return True

    def size(self):
        return len(self.s)

    def print(self):
        print(self.s)
        

class Graph:
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start
        self.s = Stack()
        self.visit = []

    def dfs(self):
        self.s.push(self.start)
        while self.s.isEmpty() == False:
            curNode = self.s.pop()
            if curNode not in self.visit:
                self.visit.append(curNode)
                for node in sorted(list(set(self.graph[curNode]) - set(self.visit))):
                    self.s.push(node)
                    print(curNode,end=" ")
                    self.s.print()
        return self.visit

g1 = {}
g1['A'] = ['B','C']
g1['B'] = ['A','D','E']
g1['C'] = ['A','E']
g1['D'] = ['B','G']
g1['E'] = ['B','C','G']
g1['F'] = ['G']
g1['G'] = ['D','E','F']

g = Graph(g1,'A')
print(g.dfs())

print(g1)