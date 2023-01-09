def solution(n, m):
    answer = ''
    star = '*' * n
    for i in range(m):
        if i == m-1:
            answer += star
        else:
            answer += star + '\n'
    return answer

n = 5
m = 3
print(solution(n, m))