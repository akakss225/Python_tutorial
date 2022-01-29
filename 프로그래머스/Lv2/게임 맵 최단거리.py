from collections import deque

def solution(maps):
    # y축
    n = len(maps)
    # x축
    m = len(maps[0])
    # 방문여부
    check = [[False] * m for i in range(n)]
    
    # 우 하 좌 상
    dy = [0, 1 ,0 ,-1]
    dx = [1, 0, -1 ,0]
    q = deque([[0, 0, 0]])
    check[0][0] = True
    while q:
        y, x, cnt = q.popleft()
        cnt += 1
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if maps[ny][nx] == 1 and check[ny][nx] == False:
                    q.append([ny, nx, cnt])
                    check[ny][nx] = True
        
        if x == m-1 and y == n-1:
            return cnt
    
    return -1

# def solution(maps):
#     answer = 0
#     # y축
#     n = len(maps)
#     # x축
#     m = len(maps[0])
#     # 방문여부
#     check = [[False] * m for i in range(n)]
    
#     # 우 하 좌 상
#     dy = [0, 1 ,0 ,-1]
#     dx = [1, 0, -1 ,0]
#     s = [[0, 0]]
#     check[0][0] = True
#     while s:
#         y, x = s.pop()
#         answer += 1
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if 0 <= ny < n and 0 <= nx < m:
#                 if maps[ny][nx] == 1 and check[ny][nx] == False:
#                     s.append([ny, nx])
#                     check[ny][nx] = True
#         if x == m-1 and y == n-1:
#             return answer
    
#     return -1

maps = [
    [1,0,1,1,1],
    [1,0,1,0,1],
    [1,0,1,1,1],
    [1,1,1,0,1],
    [0,0,0,0,1]
    ]

print(solution(maps))