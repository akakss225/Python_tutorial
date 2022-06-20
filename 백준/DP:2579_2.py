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
result = [[stair[0], 0]]
result_sum = result[-1][0]

if stair[first] < stair[second]:
    result.append([stair[second], second])
    result_sum += result[-1][0]
    first += 2
    second += 2
else:
    result.append([stair[first], first])
    result_sum += result[-1][0]
    first += 2
    second += 2

while first < len(stair) or second < len(stair):
    if result[-2][1] + 2 == first and result[-1][1] + 1 == first:
        result.append([stair[second], second])
        result_sum += result[-1][0]
        first += 2
        second += 2
        continue
    else:
        if second > len(stair) - 1:
            result.append([stair[first], first])
            result_sum += result[-1][0]
            break
        else:
            if stair[first] < stair[second]:
                result.append([stair[second], second])
                result_sum += result[-1][0]
                first += 2
                second += 2
            else:
                result.append([stair[first], first])
                result_sum += result[-1][0]
                first += 2
                second += 2
print(result_sum)