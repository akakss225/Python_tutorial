# 문제 설명
# n개의 노드가 있는 그래프가 있습니다. 각 노드는 1부터 n까지 번호가 적혀있습니다. 1번 노드에서 가장 멀리 떨어진 노드의 갯수를 구하려고 합니다. 가장 멀리 떨어진 노드란 최단경로로 이동했을 때 간선의 개수가 가장 많은 노드들을 의미합니다.

# 노드의 개수 n, 간선에 대한 정보가 담긴 2차원 배열 vertex가 매개변수로 주어질 때, 1번 노드로부터 가장 멀리 떨어진 노드가 몇 개인지를 return 하도록 solution 함수를 작성해주세요.

# 제한사항
# 노드의 개수 n은 2 이상 20,000 이하입니다.
# 간선은 양방향이며 총 1개 이상 50,000개 이하의 간선이 있습니다.
# vertex 배열 각 행 [a, b]는 a번 노드와 b번 노드 사이에 간선이 있다는 의미입니다.
# 입출력 예
#    n	                           vertex	                                    return
#    6	    [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]               3


from collections import deque


def solution(n, edge):
    d = dict() # 각 노드를 연결하는 link를 딕셔너리로 만들어줌.
    for x, y in edge:
        if x in d:
            d[x].append(y)
        else:
            d[x] = [y]
        if y in d:
            d[y].append(x)
        else:
            d[y] = [x]
    
    
    queue = deque([[1,0]]) # BFS를 위한 queue를 수행시간을 줄이기 위해 deque로 만들어주고, 인자를 각각 [노드,깊이]로 묶어서 넣어준다. 
    check = [-1] * (n + 1) # 방문표기를 위한 check list를 만들어준다.
    while queue:
        index, depth = queue.popleft() # 노드와 깊이를 인자로 가져온다.
        check[index] = depth # 노드의 깊이를 치환해준다.
        for i in d[index]: # 현재 노드와 연결된 링크를 확인하면서
            if check[i] == -1: # 만약 현재노드와 연결된 노드를 방문하지 않았다면,
                check[i] = 0 # 방문표시를 해주고
                queue.append([i, depth + 1]) # 방문한 노드와 그 깊이를 치환해준다.(BFS이기 때문에 다음순서에서 무조건 depth는 + 1)
        depth += 1 # 깊이를 이동했기 때문에 깊이 기본값을 + 1 해준다.

    return check.count(max(check))


vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
n = 6
print(solution(n, vertex))
