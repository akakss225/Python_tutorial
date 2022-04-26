# 2xN 타일링

import sys
input = sys.stdin.readline

N = int(input())

result = [0, 1, 2]

for i in range(3, N+1):
    result.append((result[i-1] + result[i-2]) % 10007)

print(result[N])