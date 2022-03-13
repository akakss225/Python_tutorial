# 2
def solution(p):    
    answer = 0
    for i in range(len(p)):
        idx = [i]
        check = 0
        while idx:
            cur = idx.pop()
            if p[cur] == "<":
                next_idx = cur - 1
                if next_idx == -1:
                    check = 1
                    break
                else:
                    if p[next_idx] == ">":
                        break
                    else:
                        idx.append(next_idx)
            else:
                next_idx = cur + 1
                if next_idx == len(p):
                    check = 1
                    break
                else:
                    if p[next_idx] == "<":
                        break
                    else:
                        idx.append(next_idx)
        if check == 1:
            answer += 1
    return answer

def solution(p):
    answer = 0
    answer = 0
    dp = [False] * len(p)
    for i in range(len(p)):
        idx = [i]
        check = 0
        while idx:
            cur = idx.pop()
            if dp[cur] == True:
                check = 1
                break
            if p[cur] == "<":
                next_idx = cur - 1
                if next_idx == -1:
                    check = 1
                    break
                else:
                    if p[next_idx] == ">":
                        break
                    else:
                        idx.append(next_idx)
            else:
                next_idx = cur + 1
                if next_idx == len(p):
                    check = 1
                    break
                else:
                    if p[next_idx] == "<":
                        break
                    else:
                        idx.append(next_idx)
        if check == 1:
            answer += 1
            dp[i] = True
    
    return answer

def solution(p):
    answer = 0
    dp = [False] * len(p)
    for i in range(len(p)):
        idx = [i]
        while idx:
            cur_idx = idx.pop()
            if p[cur_idx] == "<":
                if cur_idx == 0:
                    dp[i] = True
                    break
                else:
                    next_idx = cur_idx - 1
                    if p[next_idx] == ">":
                        break
                    else:
                        if dp[next_idx] == True:
                            dp[i] = True
                            break
                        idx.append(next_idx)
            else:
                if cur_idx == len(p)-1:
                    dp[i] = True
                    break
                else:
                    next_idx = cur_idx + 1
                    if p[next_idx] == "<":
                        break
                    else:
                        if dp[next_idx] == True:
                            dp[i] = True
                        idx.append(next_idx)
        if dp[i] == True:
            answer += 1
    return answer

p = "<<<>>>"
p = ">>><<>>"
print(solution(p))


# 3

from itertools import combinations

def solution(arr, k, t):
    answer = 0
    for i in range(k, len(arr)+1):
        for j in list(combinations(arr, i)):
            if sum(j) <= t:
                answer += 1
    return answer

# 4

def solution(e, k):
    answer = []
    for i in range((len(e)-k)//2+1):
        answer.append(e[-1-i:-k-1-i:-1])
    
    return answer
    


e = [5, 1, 9, 8, 10, 5]
k = 3
print(solution(e,k))


# 5
