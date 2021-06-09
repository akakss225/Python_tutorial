# Graph
# BFS구하기. << BFS는 Queue를 사용

class Queue:
    def __init__(self):
        self.q = []
    
    def enQueue(self, item):
        self.q.append(item)
        
    def size(self):
        return len(self.q)
    
    def isEmpty(self):
        return self.size() == 0
    
    def deQueue(self):
        if self.isEmpty():
            return None
        else:
            return self.q.pop(0)
    
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.q[0]
        
    def print(self):
        print(self.q)
    

class Graph:
    def __init__(self, graph):
        self.graph = graph
    
    def bfs(self, start):
        # 방문한 리스트 생성. 처음에 start를 넣어줌.
        visited = [start]
        q = Queue()
        # 딕셔너리(graph)에서 start key값의 value(item)를 q에 enQueue해준다.
        for item in self.graph[start]:
            # 만약 start가 A일경우, 
            # B / C 순서대로 q 에 들어감.
            q.enQueue(item)
        
        # q가 빌때까지 반복
        while q.isEmpty() == False:
            # 임시로 deQueue한 값을 넣어준다. start가 A일 경우 B가 먼저 들어감.
            item = q.deQueue()
            # 만약 item이 방문목록에 없다면,
            if item not in visited:
                # 이 item의 edge값들을 다시 q에 넣어줌. 이는 방문할 목록이 된다.
                for _item in self.graph[item]:
                    q.enQueue(_item)
                # 다 넣었으면, item을 방문목록에 넣는다.
                visited.append(item)
        return visited
        
g1 = {}
g1['A'] = ['B','C']
g1['B'] = ['A','D','E']
g1['C'] = ['A','E']
g1['D'] = ['B','G']
g1['E'] = ['B','C','G']
g1['F'] = ['G']
g1['G'] = ['D','E','F']
g = Graph(g1)

print(g.bfs('A'))