# def solution(s):
#     i = 0
#     while s:
#         if i + 1 < len(s):
#             if s[i] == s[i+1]:
#                 s = s[:i] + s[i+2:]
#                 i = 0
#                 continue
#             else:
#                 i += 1
#                 continue
#         else:
#             return 0
#     return 1


def solution(s):
    i = 0
    stack = list(s[::-1])
    visited = []
    while stack:
        if len(visited) == 0:
            cur = stack.pop()
            visited.append(cur)
        else:
            cur = stack.pop()
            if visited[-1] == cur:
                visited.pop()
            else:
                visited.append(cur)
    if len(visited) != 0:
        return 0
    return 1
    

s = "baabaa"
s = "cdcd"
print(solution(s))