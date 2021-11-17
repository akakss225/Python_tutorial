# 1
def solution(arr):
    answer = []
    nums = [0, 0, 0]
    for i in arr:
        if i == 1:
            nums[0] += 1
        elif i == 2:
            nums[1] += 1
        else:
            nums[2] += 1
    
    for i in range(len(nums)):
        num = max(nums) - nums[i]
        answer.append(num)
    
    return answer
# 2
def solution(arr):
    answer = ''
    timeTable = []
    result = 0
    for i in arr:
        timeTable.append(i.split(":"))
        
    for i in range(0, len(arr)//2):
        start = 2 * i
        end = 2 * i + 1
        h = (int(timeTable[end][0]) - int(timeTable[start][0])) * 60
        m = int(timeTable[end][1]) - int(timeTable[start][1])
        timeSet = h + m
        
        if timeSet > 105:
            result += 105
        elif timeSet < 5:
            continue
        else:
            result += timeSet
    h = result // 60
    m = result % 60
        
    if h < 10:
        answer += "0" + str(h) + ":"
    else:
        answer += str(h) + ":"
        
    if m < 10:
        answer += "0" + str(m)
    else:
        answer += str(m)
            
    return answer

# 3
def solution(ings, menu, sell):
    answer = 0
    ingsDic = {}
    menuDic = {}
    made = {}
    
    for i in ings:
        ingsDic[i.split()[0]] = int(i.split()[1])
    for i in menu:
        menuDic[i.split()[0]] = int(i.split()[2])
    
    for i in menu:
        for j in i.split()[1]:
            if i.split()[0] in made:
                made[i.split()[0]] += ingsDic[j]
            else:
                made[i.split()[0]] = ingsDic[j]
    for i in menuDic:
        made[i] = menuDic[i] - made[i]
    
    for i in sell:
        answer += (made[i.split()[0]] * int(i.split()[1]))
    
    return answer

# 4
from collections import deque
def solution(s):
    result = []
    answer = deque(s)
    while True:
        if answer[-1] == answer[0]:
            answer.appendleft(answer.pop())
        else:
            break
    
    count = 1
    while answer:
        temp = answer.popleft()
        if len(answer) == 0:
            result.append(count)
            break
        if temp == answer[0]:
            count += 1
        else:
            result.append(count)
            count = 1
    
    return sorted(result)

# 5
def check(arr):
    for i in arr:
        if 0 in i:
            return True
        else:
            continue
    return False

def solution(rows, columns):
    board = []
    for i in range(rows):
        board.append([0]*columns)
    row = 0
    col = 0
    count = 1
    while check(board):
        if row == rows:
            row = 0
        if col == columns:
            col = 0
        board[row][col] = count
        
        if count % 2 == 1:
            col += 1
        else:
            row += 1
        count += 1
        if columns == rows and count == columns * 2 + 1: 
            return board
        
    return board

# 6
import re
def solution(time, plans):
    answer = ''
    go_work = 13
    out_work = 18
    
    plansDic = {}
    for i in plans:
        if "PM" in i[1]:
            plansDic[i[0]] = [12+float(re.sub(r'[^0-9]',"",i[1]))]
        else:
            plansDic[i[0]] = [float(re.sub(r'[^0-9]',"",i[1]))]
        if "PM" in i[2]:
            plansDic[i[0]].append(12+float(re.sub(r'[^0-9]',"",i[2])))
        else:
            plansDic[i[0]].append(float(re.sub(r'[^0-9]',"",i[2])))
    
    # 각 여행지별 소요시간 및 휴가시간 고려
    for i in range(len(plans)):
        if i > 0:
            pre = i - 1
        else:
            pre = 0
        if out_work - plansDic[plans[i][0]][0] > 0:
            time -= (out_work - plansDic[plans[i][0]][0])
        if plansDic[plans[i][0]][1] - go_work > 0:
            time -= (plansDic[plans[i][0]][1] - go_work)
        plansDic[plans[i][0]].append(time)
        
        if time < 0 and i == 0:
            return "호치민"
        elif time < 0 and i > 0:
            return plans[pre][0]
        
    
    return plans[-1][0]

# 7