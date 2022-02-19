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
    
    # 사람이 앉아있는 자리 찾기
    # [방 번호, 열, 자리]
    for i in range(room):
        for j in range(n):
            for k in range(m):
                if places[i][j][k] == "P":
                    q.append([i, j, k])
                
    while q:
        # 방번호 / 열 / 자리
        curR, curY, curX = q.popleft()
        # 현재 사람 주변의 자리를 넣어줄 스택 생성
        s = []
        for i in range(4):
            # 상하좌우 확인을 할 예정
            nextY = dy[i] + curY
            nextX = dx[i] + curX
            
            # 인덱스가 넘지 않는 선에서
            if 0 <= nextX < 5 and 0 <= nextY < 5:
                # 만약 그 주변자리가 O인 경우 우선 s에 넣는다 >> 파티션이 아닌 경우 한번 더 봐야함
                if places[curR][nextY][nextX] == "O":
                    s.append([curR, nextY, nextX])
                # 만약 현재 자리 주변이 P인 경우 >> 이미 조건에 부합하지 않기 때문에, answer[curR] = 0
                elif places[curR][nextY][nextX] == "P":
                    answer[curR] = 0
                    # 뒤의 과정이 필요없기 때문에 스택 클리어
                    s.clear()
                    # 추가적으로 현재 방은 이미 0이기 때문에, q에서 현재 방인 경우를 다 제거해준다.
                    while q:
                        if q[0][0] == curR:
                            q.popleft()
                        else:
                            break
                    break
                # X인 경우는 넣을 필요 없음.
        
        # s 가 있는 경우는 현재 자리 주변에 O인 경우임
        while s:
            # P주변 O자리의 좌표를 꺼냄
            curRR, curYY, curXX = s.pop()
            check = 1
            for j in range(4):
                # 주변O 의 상하좌우를 확인할 예정
                nextYY = dy[j] + curYY
                nextXX = dx[j] + curXX
                
                if 0 <= nextXX < 5 and 0 <= nextYY < 5:
                    # 만약 상하좌우에 P가 있으면서, 이 P는 원래 P자리가 아닌 경우에, 현재 방 또한 조건 불만족.
                    if places[curRR][nextYY][nextXX] == "P" and curX != nextXX and curY != nextYY:
                        answer[curR] = 0
                        s.clear()
                        check = 0
                        break
            # 만약 check == 1이면, 계속해서 스택 진행
            # check == 0이면, 조건 불만족을 의미. 즉, 방이 이미 0이기 때문에 현재 방 q를 다 빼준다.
            if check == 0:
                while q:
                    if q[0][0] == curR:
                        q.popleft()
                    else:
                        break
            # 자연스럽게 s가 다 pop이 되면, while문 종료.
    
    return answer

def solution(places):
    answer = []
    
    room = len(places)
    n = len(places[0])
    m = len(places[0][0])
    d = dict()
    
    # 사람이 앉아있는 자리 찾기
    # [방 번호, 열, 자리]
    for i in range(room):
        for j in range(n):
            for k in range(m):
                if places[i][j][k] == "P":
                    if i in d:
                        d[i].append([j, k])
                    else:
                        d[i] = [[j, k]]
    for i in d:
        check = 1
        
        for j in range(len(d[i])):
            for k in range(j+1, len(d[i])):
                if abs(d[i][j][0] - d[i][k][0]) + abs(d[i][j][1] - d[i][k][1]) == 1:
                    answer.append(0)
                    check = 0
                    break
                elif abs(d[i][j][0] - d[i][k][0]) + abs(d[i][j][1] - d[i][k][1]) == 2:
                    if d[i][j][0] == d[i][k][0] and places[i][abs(j-k)][0] == "O":
                        check = 0
                        answer.append(0)
                        break
                    elif d[i][j][1] == d[i][k][1] and places[i][abs(j-k)][d[i][j][1]] == "O":
                        check = 0
                        answer.append(0)
                        break
                    elif places[i][abs(j-k)][d[i][j][1]] == "O" or places[i][abs(j-k)][d[i][j][0]] == "O":
                        check = 0
                        answer.append(0)
                        break
            if check == 0:
                break
        if check == 1:
            answer.append(1)
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