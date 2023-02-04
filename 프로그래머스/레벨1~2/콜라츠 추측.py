# 1-1. 입력된 수가 짝수라면 2로 나눕니다. 
# 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다. 
# 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다. 

def solution(num):
    count = 1
    if num == 1:
        return 0
    while count < 500:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num * 3 + 1
        if num == 1:
            return count
        count += 1
    return -1

num = 626331
print(solution(num))