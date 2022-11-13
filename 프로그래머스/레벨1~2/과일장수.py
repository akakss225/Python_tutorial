## 사과 한상자에 m개씩, 사과 등급이 가장 낮은 점수가 p라고 가정하면, 한상자 가격은 p * m
## k 는 해당 사과박스의 가장 높은 등급임.
## 1. score 에 적힌 사과를 최대한 소진하며 최고의 가격을 리턴해야함
## 2. 만약 7개의 사과가있고 1박스에 4개짜리면, 3개는 남게됨
## 3. score / m >= 1 일떄까지 계속 반복
## 4. 만약 score / m < 2 일경우, 최소등급 사과는 배제한다. *** 키포인트
## 5. score / m >= 2 일 경우, 가장 최소등급끼리 최대한 몰아넣는다. >> 최고등급은 최고등급끼리 최대한 묶는다.
from collections import deque as deq

def solution(k, m, score):
    answer = 0
    score = deq(sorted(score, reverse=True))
    while len(score) / m >= 1:
        if len(score) / m >= 2:
            box = []
            for i in range(m):
                item = score.pop()
                box.append(item)
            answer += min(box) * m
        else:
            box = []
            for i in range(m):
                item = score.popleft()
                box.append(item)
            answer += min(box) * m
    return answer

k = 4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]

print(solution(k, m, score))
