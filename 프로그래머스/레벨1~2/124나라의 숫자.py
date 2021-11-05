import math

def threepow(n):
    result = 0
    for i in range(1, n+1):
        result += int(math.pow(3,i))
    return result

def nums(n):
    count = 1
    while True:
        if threepow(count) >= n:
            return count
        else:
            count += 1

def solution(n):
    answer = ''
    shareList = []
    if n < 4:
        return str(n)
    
    count = nums(n)
    
    
    
    return answer

n = 12

print(solution(n))