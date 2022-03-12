# 펠린드롬
def palindrome(s):
    for i in range(len(s)//2):
        if s[i] == s[-i-1]:
            continue
        else:
            return False
    return True

# 정답
def solution(s):
    result = []
    if len(s) == 1:
        return 1
    for i in range(len(s)-1):
        for j in range(len(s)-1, 0, -1):
            if s[i] == s[j]:
                if palindrome(s[i:j+1]):
                    result.append(j-i+1)
                    if max(result) > result[-1]:
                        break
    if len(result) == 0:
        return 1
    return max(result)