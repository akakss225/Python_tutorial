# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)
import math

def check(n):
    if n % 2 != 0:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    return False

def solution(n):
    answer = 2
    if n == 2:
        return 1
    if n == 3:
        return 2
    for i in range(4, n+1):
        if check(i):
            answer += 1
    return answer

def solution2(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

n = 10
print(solution2(n))