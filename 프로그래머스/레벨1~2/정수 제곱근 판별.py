# 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.
import math

def solution(n):
    if math.sqrt(n) - int(math.sqrt(n)) > 0:
        return -1
    return int(math.pow(math.sqrt(n) + 1, 2))

n = 121
print(solution(n))