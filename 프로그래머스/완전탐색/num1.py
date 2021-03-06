# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한 조건
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.




'''
def solution(answers):
    answer = []
    count = [0,0,0]
    num1 = [1,2,3,4,5] # 5개 반복
    num2 = [2,1,2,3,2,4,2,5] # 8개 반복
    num3 = [3,3,1,1,2,2,4,4,5,5] # 10개 반복
    for i in range(len(answers)):
        if answers[i] == num1[i%5]:
            count[0] += 1
        if answers[i] == num2[i%8]:
            count[1] += 1
        if answers[i] == num3[i%10]:
            count[2] += 1
    if count[0] == count[1] == count[2]:
        answer.append(1)
        answer.append(2)
        answer.append(3)
    elif count[0] == count[1]:
        if count[0] > count[2]:
            answer.append(1)
            answer.append(2)
        else:
            answer.append(3)
    elif count[0] == count[2]:
        if count[0] > count[1]:
            answer.append(1)
            answer.append(3)
        else:
            answer.append(2)
    elif count[1] == count[2]:
        if count[1] > count[0]:
            answer.append(2)
            answer.append(3)
        else:
            answer.append(1)
    else:
        if count[0] > count[1]:
            if count[0] > count[2]:
                answer.append(1)
            else:
                answer.append(3)
        else:
            if count[1] > count[2]:
                answer.append(2)
            else:
                answer.append(3)
    return answer

#answers = [1,2,3,4,5]
answers = [1,3,2,4,2]

print(solution(answers))
'''
'''
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
#answers = [1,2,3,4,5]
answers = [1,3,2,4,2]

print(solution(answers))
'''

def solution(answers):
    result = []
    p1 = [1,2,3,4,5] * 8
    p2 = [2,1,2,3,2,4,2,5] * 5
    p3 = [3,3,1,1,2,2,4,4,5,5] * 4
    score = [0, 0, 0]
    answer = list(zip(p1,p2,p3))
    for i in range(len(answers)):
        for j in range(3):
            if answers[i] == answer[i%40][j]:
                score[j] += 1
    for i in range(3):
        if score[i] == max(score):
            result.append(i+1)
    return result
    
answers = [1,3,2,4,2]

print(solution(answers))    
    
    
    






