from collections import deque

graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D'],
        'D': ['C', 'E', 'G'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }

start = 'A'

def bfs(graph, start):
    visite = []
    queue = deque([start])
    
    while queue:
        cur = queue.popleft()
        if cur not in visite:
            visite.append(cur)
            queue.extend(graph[cur])
    return visite

print(bfs(graph, start))
