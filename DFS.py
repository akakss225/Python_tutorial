answer = 0

def dfs(idx, value, numbers, target):
    global answer
    n = len(numbers)
    if value == target and idx == n:
        answer += 1
        return
    elif value != target and idx == n:
        return
    dfs(idx+1, value+numbers[idx], numbers, target)
    dfs(idx+1, value-numbers[idx], numbers, target)

def solution(numbers, target):
    global answer
    dfs(0, 0, numbers, target)
    return answer

n = [1, 1, 1, 1, 1]
t = 3

print(solution(n, t))