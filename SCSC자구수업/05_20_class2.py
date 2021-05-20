# BFS는 Queue를 사용한다

class Queue:
    def __init__(self):
        self.q = []

    def enQueue(self, item):
        self.q.append(item)

    def deQueue(self):
        if self.isEmpty() == False:
            return self.q.pop(0)

    def size(self):
        return len(self.q)

    def isEmpty(self):
        if len(self.q) > 0:
            return False
        else:
            return True

    def peek(self):
        if self.isEmpty() == False:
            return self.q[0]

    def delete(self, item):
        if item in self.q:
            self.q.remove(item)
        else:
            print("해당 아이템이 존재하지 않습니다.")

class Graph:
    def __init__(self, graph, start):
        self.graph = graph
        self.start = start
        self.s = Queue()
        self.visit = []
    
    def bfs(self):
        visit = [self.start]
        queue = Queue()
        for item in self.graph[self.start]:
            queue.enQueue(item)

        while queue.isEmpty() == False:
            item = queue.deQueue()
            if not item in visit:  # 현재 아이템이 가본 곳이 아니면 ...
                for _item in self.graph[item]:
                    queue.enQueue(_item)
                visit.append(item)
        return visit

g1 = {}
g1['A'] = ['B','C']
g1['B'] = ['A','D','E']
g1['C'] = ['A','E']
g1['D'] = ['B','G']
g1['E'] = ['B','C','G']
g1['F'] = ['G']
g1['G'] = ['D','E','F']
g = Graph(g1, 'A')
print(g.bfs())