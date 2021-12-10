def solution(s):
    answer = 1
    
    while s:
        for i in range(1,len(s)+1):
            pre = s[i-1]
            current = s[i]
            if pre == current:
                s = s[:i-1] + s[i+1:]
                break
            

    return answer
s = 1
print(solution(s))