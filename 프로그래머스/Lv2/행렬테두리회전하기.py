# IDEA
# 1. List를 배열로 표시하기 위한 좌표를 설정
# 2. cordinate 라는 list를 만들고, 반시계 방향으로 돌면서 좌표를 넣어줌.
# 3. cordinate 에 추가된 요소를 순차적으로 돌며, 다음 좌표와 switching >> 자동적으로 시계방향으로 돌아짐
# 4. 포함된 좌표들의 최솟값을 answer에 append해줌.

def solution(rows, columns, queries):
    # 정답을 넣을 answer list
    answer = []
    
    # 1 to rows*columns 배열을 만들어줌
    procession = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(i*columns+j + 1)
        procession.append(row)

    # 제공해준 queries를 돌 반복문 생성
    for i in queries:
        # 알맞는 인덱스를 위해 -1 값을 해준 좌표를 반환
        x1 = i[0]-1
        y1 = i[1]-1
        x2 = i[2]-1
        y2 = i[3]-1
        
        # 지정된 범위의 행렬 테두리 value를 넣을 temp list 생성
        temp = []
        
        # 지정된 범위의 행렬 테두리 좌표를 넣을 cordinate list 생성
        # 이 list 를 통해, 시계방향으로 돌릴것임.
        cordinate = []
        
        # 시계방향으로 돌리기 쉽게, cordinate list에 좌표를 반시계방향으로 append 해줌.
        for j in range(x1, x2+1):
            cordinate.append([j, y1])
            temp.append(procession[j][y1])
        for j in range(y1+1, y2+1):
            cordinate.append([x2, j])
            temp.append(procession[x2][j])
        for j in range(x2-1, x1-1, -1):
            cordinate.append([j, y2])
            temp.append(procession[j][y2])
        for j in range(y2-1, y1, -1):
            cordinate.append([x1, j])
            temp.append(procession[x1][j])
            
        # 범위에 포함되는 좌표를 시계방향으로 돌려주는 반복문 실행
        # 처음에 반시계 방향으로 append 해주었기에, 
        # cordinate list를 순서대로 돌며 다음 좌표와 switch만 해주어도 시계방향으로 바뀜.
        for j in range(len(cordinate)-1):
            procession[cordinate[j][0]][cordinate[j][1]], procession[cordinate[j+1][0]][cordinate[j+1][1]] = procession[cordinate[j+1][0]][cordinate[j+1][1]], procession[cordinate[j][0]][cordinate[j][1]]
        
        # 최종적으로 지정된 범위에 포함되는 숫자중, 가장 작은 수를 answer 에 append 해줌.
        answer.append(min(temp))
    return answer

queries = [
    [2,2,5,4],
    [3,3,6,6],
    [5,1,6,3]
    ]
rows = 6
columns = 6

print(solution(rows, columns, queries))