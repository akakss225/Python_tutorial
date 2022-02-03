from collections import deque

def solution(places):
    answer = [1] * len(places)
    # 상 하 좌 우
    dy = [0, 1, 0 , -1]
    dx = [1, 0, -1, 0]
    room = len(places)
    n = len(places[0])
    m = len(places[0][0])
    q = deque()
    for i in range(room):
        for j in range(n):
            for k in range(m):
                if places[i][j][k] == "P":
                    q.append([i, j, k])
                
    while q:
        curR, curY, curX = q.popleft()
        s = []
        for i in range(4):
            nextY = dy[i] + curY
            nextX = dx[i] + curX
            
            if 0 <= nextX < 5 and 0 <= nextY < 5:
                if places[curR][nextY][nextX] == "O":
                    s.append([curR, nextY, nextX])
                elif places[curR][nextY][nextX] == "P":
                    answer[curR] = 0
                    s.clear()
                    while q:
                        if q[0][0] == curR:
                            q.popleft()
                        else:
                            break
                    continue
        while s:
            curRR, curYY, curXX = s.pop()
            check = 1
            for j in range(4):
                nextYY = dy[j] + curYY
                nextXX = dx[j] + curXX
                
                if 0 <= nextXX < 5 and 0 <= nextYY < 5:
                    if places[curRR][nextYY][nextXX] == "P" and curX != nextXX and curY != nextYY:
                        answer[curR] = 0
                        s.clear()
                        check = 0
                        break
            if check == 0:
                while q:
                    if q[0][0] == curR:
                        q.popleft()
                    else:
                        break
    return answer


places = [
        ["POOOP", 
        "OXXOX", 
        "OPXPX", 
        "OOXOX", 
        "POXXP"], 
        
        ["POOPX", 
        "OXPXP", 
        "PXXXO", 
        "OXXXO", 
        "OOOPP"], 
        
        ["PXOPX", 
        "OXOXP", 
        "OXPOX", 
        "OXXOP", 
        "PXPOX"], 
        
        ["OOOXX", 
        "XOOOX", 
        "OOOXX", 
        "OXOOX", 
        "OOOOO"], 
        
        ["PXPXP", 
        "XPXPX", 
        "PXPXP", 
        "XPXPX", 
        "PXPXP"]
    ]

# places = [["OOPOO", 
#            "OPOOO", 
#            "OOOOO", 
#            "OOOOO", 
#            "OOOOO"],
#           ["PXPXP", 
#            "XPXPX", 
#            "PXPXP", 
#            "XPXPX", 
#            "PXPXP"]]

print(solution(places))