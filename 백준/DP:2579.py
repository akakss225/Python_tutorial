# 계단오르기

import sys

input = sys.stdin.readline

N = int(input())

stair = []

for i in range(N):
    stair.append(int(input()))
stair.reverse()

first = 1
second = 2
result = stair[0]

now = []
while True:
    if first < N:
        if second < N:
            if stair[first] < stair[second]:
                result += stair[second]
                now.append(second)
            else:
                result += stair[first]
                now.append(first)
        else:
            if now[-1] - now[-2] == 1:
                break
            else:
                now.append(N-1)
                result += stair[N-1]
                break
    first += 2
    second += 2

print(result)