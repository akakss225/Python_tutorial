from collections import deque as deq

def solution(new_id):
    answer = deq(new_id)
    result = ""
    while answer:
        cur = answer.popleft()
        if result == "" and cur == ".":
            continue
        if cur.isalpha():
            result += cur.lower()
        elif cur.isdigit():
            result += cur
        elif cur == "." and result[-1] == ".":
            continue
        elif cur == "-" or cur == "." or cur == "_":
            result += cur
    
    if result == "":
        return "aaa"
    if len(result) >= 16:
        result = result[:15]
    while True:
        if result[-1] == ".":
            result = result[:-1]
        else:
            break
    if len(result) <= 2:
        while len(result) < 3:
            result += result[-1]
        return result
    return result
        
new_id = "...!@BaT#*..y.abcdefghijklm"
new_id = "z-+.^."
new_id = "=.="
new_id = "abcdefghijklmn.p"

print(solution(new_id))