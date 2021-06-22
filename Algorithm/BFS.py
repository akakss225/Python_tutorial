from collections import deque

graph = {1: set([3, 4]),
        2: set([3, 4, 5]),
        3: set([1, 5]),
        4: set([1]),
        5: set([2, 6]),
        6: set([3, 5])}

start = 1

def new_func(graph, start):
    def bfs(graph, start):
        visite = []
        queue = deque([start])
    
        while queue:
            cur = queue.popleft()
            if cur not in visite:
                visite.append(cur)
                queue += graph[cur] - set(visite)
        return visite

    print(bfs(graph, start))

new_func(graph, start)
