from collections import deque

def solution(n):
    answer = ""
    temp = n
    while temp != 0:
        share = temp // 3
        trash = temp % 3
        if trash != 0:
            if trash == 1:
                answer = "1" + answer
            else:
                answer = "2" + answer
        else:
            answer = "4" + answer
            share -= 1
        temp = share
    return answer

print(solution(5))
    