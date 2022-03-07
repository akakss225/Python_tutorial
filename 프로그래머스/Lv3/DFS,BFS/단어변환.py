# IDEA
# 1. 가장 우선적을 target word 가 주어진 words안에 있어야함
# 2. begin을 기준으로 DFS시작.
# 3. visit list를 만들고, 현재 위치의 단어를 append.
# 4. 만약 현재 단어가 target word와 2개 같다면, 그대로 visit list의 길이를 출력
# 5. 다르다면, 스택 list에 변환될 수 있는 단어(현재 단어와 2개 같은)를 넣어줌
# 6. 반복

def solution(b, t, w):
    if t not in w:
        return 0
    
    s = [b]
    visit = []
    while True:
        cur = s.pop()
        visit.append(cur)
        result = 0
        for i in range(len(cur)):
            if cur[i] != t[i]:
                result += 1
        if result == 1:
            return visit
        for i in w:
            check = 0
            for j in range(len(i)):
                if cur[j] != i[j]:
                    check += 1
            if check == 1:
                if i not in visit and i not in s:
                    s.append(i)



b = "hit"
t = "cog"
w = ["hot", "dot", "dog", "lot", "log", "cog"]
# w = ["cog", "log", "lot", "dog", "dot", "hot"]
b = "aoa"
t = "aof"
w = ["aob", "aoc", "aod", "aof", "aoe"]

begin = "hit"
target = "hhh"
words = ["hhh","hht"]

print(solution(b,t,w))
print(solution(begin,target,words))

