# 설탕 배달


import sys

input = sys.stdin.readline

N = int(input())

d = [-1, -1, -1]

for i in range(3, N+1):
    if i % 5 != 0 and i % 3 != 0:
        if i - 5 >= 0:
            if d[i - 5] != -1:
                d.append(d[i-5] + 1)
            elif d[i - 3] != -1:
                d.append(d[i - 3] + 1)
            else:
                d.append(-1)
        elif i - 3 >= 0:
            if d[i - 3] != -1:
                d.append(d[i - 3] + 1)
            else:
                d.append(-1)
    elif i % 5 == 0:
        d.append(int(i / 5))
    elif i % 5 != 0 and i % 3 == 0:
        if d[i - 5] != -1:
            d.append(d[i - 5] + 1)
        else:
            d.append(int(i / 3))

print(d[N])


