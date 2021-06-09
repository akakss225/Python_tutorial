# Graph 
# DFS 구현하기

class Stack:
    def __init__(self):
        self.s = []
    
    def push(self, item):
        self.s.append(item)
    
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.s.pop()
        
    def size(self):
        return len(self.s)
    
    def peek(self):
        if self.isEmpty():
            return None
        else:
            return self.s[-1]
    
    def isEmpty(self):
        return len(self.s) == 0
    
    def print(self):
        print(self.s)
    
    

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.s = Stack()

    def dfs(self, start):
        # 방문이 된 순서대로 담을 그릇
        visited = []
        # 빈 Stack에 시작점을 넣어줌.
        self.s.push(start)
        # Stack이 빌때까지 반복시작
        while self.s.isEmpty() == False:
            # 처음에는 시작점을 뽑아서 curNode에 담아준다. 이후엔 이미 방문한 마지막, 즉 현재위치의 부모를 담아줌
            curNode = self.s.pop()
            # 만약 스택에서 꺼낸 curNode가 방문된 그릇에 없다면
            if curNode not in visited:
                # 그대로 넣어줌. 이는 중복을 걸러내기 위함이다.(back edge)
                visited.append(curNode)
                # revers를 써준 이유는, 개발자가 스스로 방문 순서를 정해놨다고 보면 됨. 이땐 오름차순, 알파벳 순서대로 진행한다. 스택이기 때문에.
                # set을 사용하는 이유는, 중복을 제거하기위함.
                # 즉 set(self.graph[curNode]) - set(visited)는 딕셔너리 key값인 curNode의 value값중 방문한걸 제외한 나머지 node임.
                # curNode 가 만약 A일경우, set(self.graph[curNode]) = [B, C]이고, set(visited) = [A] >>> 중복 제거하기.
                for node in sorted(list(set(self.graph[curNode]) - set(visited)), reverse=True): 
                    # 다시 방문하고자 하는 node를 Stack에 넣어줌.
                    self.s.push(node)
                # 현재 방문중인 curNode를 먼저 출력해주고, 그 옆에 방문 가능한 ndoe들(edge로 연결된)을 출력해줌
                print(curNode,end=" ")
                self.s.print()
            # 만약 스택에서 꺼낸 curNode가 방문된 그릇에 있다면, visited에 넣어주지않고 다시 while문 시작.
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
print(g.dfs('A'))

print(g1)