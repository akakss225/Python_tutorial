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

def dfs(graph, start):
    answer = []
    stack = [start]
    
    while stack:
        cur = stack.pop()
        if cur not in answer:
            answer.append(cur)
            stack.extend(sorted(graph[cur], reverse= True))
    return answer

print(dfs(graph, start))