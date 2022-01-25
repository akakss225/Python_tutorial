from itertools import combinations

def prime_num(a):
    for i in range(2, a//2+1):
        if a % i == 0:
            return False
    return True

def solution(nums):
    p = list(combinations(nums, 3))
    answer = 0
    for i in p:
        a = sum(i)
        if prime_num(a):
            answer += 1
    return answer

nums = [1,2,3,4]

print(solution(nums))
