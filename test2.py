from itertools import permutations
s = "abca"
l = []
s = list(map(''.join, permutations(s, len(s))))
for j in s:
    c = 0
    for i in range(1, len(j)):
        if j[i-1] == j[i]:
            c += 1
    if c == 0:
        l.append(j)
print(l)

def solution(donut):
    answer = 0
    check = 0
    if donut % 5 == 0:
        box = donut / 5
        answer += box
        check = 1
    elif donut < 0:
        check = 1
        return "판매불가"
    donut -= 3
    answer += 1
    if check == 0:
        solution(donut)
    return answer

donut = 11

print(solution(donut))