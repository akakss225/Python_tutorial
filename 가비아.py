# # DP >> 피보나치

# # Top down DP
# def fib_dp(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
    
#     fib_arr = [0, 1]
#     num = fib_dp(n-1) + fib_dp(n-2)
#     fib_arr.append(num)
#     return num

# # 개지림... >> Bottom up DP
# def fib_dp2(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     fib_arr = [0, 1]
#     for i in range(2, n+1):
#         num = fib_arr[i-1] + fib_arr[i-2]
#         fib_arr.append(num)
#     return fib_arr[n]

# print(fib_dp2(10000))


from collections import deque

def solution(grid, K):
    answer = 0
    visited = [[False] * len(grid[0]) for i in range(len(grid))]
    dy = [0, 1]
    dx = [1, 0]
    
    for i in range(2):
        temp = []
        for y in range(len(grid)-K+1):
            for x in range(len(grid)-K+1):
                if visited[y][x] == False:
                    q = deque([[y, x]])
                    result = [y,x,0]
                    check = 0
                    while q:
                        cy, cx = q.popleft()
                        result[-1] += grid[cy][cx]
                        for i in range(2):
                            ny, nx = cy+dy[i], cx+dx[i]
                            if nx-x < K and ny-y < K:
                                if visited[ny][nx]:
                                    check = 1
                                    break
                                if [ny, nx] not in q:
                                    q.append([ny,nx])
                    if check == 0:
                        temp.append(result)

        temp.sort(key=lambda x:x[2], reverse=True)
        answer += temp[0][2]
        
        idx = [temp[0][0], temp[0][1]]
        for a in range(idx[0], idx[0]+K):
            for j in range(idx[1], idx[1] + K):
                visited[a][j] = True
        
    return answer

g= [[3, 4, 5], [2, 3, 4], [1, 2, 3]]
g= [[2, 1, 1, 0, 1], [1, 2, 0, 3, 0], [0, 1, 5, 1, 2], [0, 0, 1, 3, 1], [1, 2, 0, 1, 1]]
k= 1
k = 2
print(solution(g, k))


def dp(e, k):
    result = [sum(e[:k])]
    for i in range(k, len(e)):
        result.append(result[-1]-e[i-k]+e[i])
    return max(result)

e =[5, 1, 9, 8, 10, 5]
k = 3
print(dp(e,k))