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

now = [1]

while True:
    if first < N:
        if second < N:
            if second + 1 - now[-1] == 3:
                result += stair[first]
                now.append(first+1)
            else:
                if stair[first] < stair[second]:
                    result += stair[second]
                    now.append(second+1)
                else:
                    result += stair[first]
                    now.append(first+1)
        else:
            if now[-1] - now[-2] == 1:
                break
            else:
                now.append(N)
                result += stair[N-1]
                break
    else:
        break
    first += 2
    second += 2

print(result)