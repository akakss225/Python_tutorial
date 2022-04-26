# 1로 만들기

# 주어진 수까지 for 문을 돌며 진행
# x - 1 or x / 2 or x / 3 조건에서 이전에 계산된 숫자가 있다면, 그 연산 횟수를 더해줌

import sys
input = sys.stdin.readline
X = int(input())

rs = [0, 0, 1, 1]

for i in range(4, X+1):
    if i % 2 != 0 and i % 3 != 0:
        rs.append(rs[i - 1]+1)
    elif i % 2 != 0 and i % 3 == 0:
        if rs[i - 1] >= rs[int(i / 3)]:
            rs.append(rs[int(i / 3)] + 1)
        else:
            rs.append(rs[i - 1] + 1)
    elif i % 2 == 0 and i % 3 != 0:
        if rs[i - 1] >= rs[int(i / 2)]:
            rs.append(rs[int(i / 2)] + 1)
        else:
            rs.append(rs[i - 1] + 1)
    else:
        if rs[i - 1] >= rs[int(i / 2)]:
            if rs[int(i / 2)] >= rs[int(i / 3)]:
                rs.append(rs[int(i / 3)] + 1)
            else:
                rs.append(rs[int(i / 2)] + 1)
        else:
            if rs[i - 1] >= rs[int(i / 3)]:
                rs.append(rs[int(i / 3)] + 1)
            else:
                rs.append(rs[i - 1] + 1)

print(rs)