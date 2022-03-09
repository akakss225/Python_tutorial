from collections import defaultdict 

t = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

graph = defaultdict(list)

for x, y in t:
    graph[x].append(y)

print(graph)