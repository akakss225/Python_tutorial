# 1, 2 ,3 더하기

import sys

input = sys.stdin.readline


T = int(input())

d = [0, 1, 2, 4, 7]


for i in range(4, 11):
    d.append(d[i] + (d[i-2] - d[i-3]) + (d[i-1] - d[i-2]) + (d[i] - d[i-1]))

for i in range(T):
    N = int(input())
    print(d[N])

