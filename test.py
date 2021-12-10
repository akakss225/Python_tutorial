def solution(s):
    while s:
        check = len(s)
        for i in range(0,len(s)):
            if i != 0:
                pre = s[i-1]
            else:
                pre = ''
            current = s[i]
            if pre == current:
                s.replace(pre+current,"",1)
                break
        check_after = len(s)
        if check == check_after:
            return 0
    return 1
s = "abbabb"
print(solution(s))