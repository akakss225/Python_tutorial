# 문제 설명
# 조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
# ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

# 조이스틱을 각 방향으로 움직이면 아래와 같습니다.

# ▲ - 다음 알파벳
# ▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
# ◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
# ▶ - 커서를 오른쪽으로 이동 (마지막 위치에서 오른쪽으로 이동하면 첫 번째 문자에 커서)
# 예를 들어 아래의 방법으로 "JAZ"를 만들 수 있습니다.

# - 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
# - 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
# - 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
# 따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
# 만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

# 제한 사항
# name은 알파벳 대문자로만 이루어져 있습니다.
# name의 길이는 1 이상 20 이하입니다.
# 입출력 예
# name	return
# "JEROEN"	56
# "JAN"	23

def solution(name):
    answer = 0
    count = list(min(ord(i) - ord("A"), ord("Z") - ord(i) + 1) for i in name)
    idx = 0
    while True:
        answer += count[idx]
        count[idx] = 0
        if sum(count) == 0:
            return answer
        
        r = l = 1
        idx_r = 1 + idx
        idx_l = idx - 1
        
        while count[idx_r] == 0:
            if idx_r >= len(name):
                idx_r = 0
                r += 1
            else:
                idx_r += 1
                r += 1
        while count[idx_l] == 0:
            if idx_l < -(len(name)):
                idx_l = -1
                l += 1
            else:
                idx_l -= 1
                l += 1
    
        if l > r:
            answer += r
            idx += r
        else:
            answer += l
            idx -= l


# def solution(name):
#     count = 0
#     route = [min(ord(i) - ord("A"), ord("Z") - ord(i) + 1) for i in name]
#     cur = 0
#     first = 1
#     while sum(route) != 0:
#         count += route[cur]
#         route[cur] = 0
#         r = l = 1
#         if first == 1 and cur != 0:
#             first = 0
#         if sum(route) == 0:
#             return count
#         while route[cur + r] == 0 and cur + r < len(name) -1:
#             r += 1
#         while route[cur - l] == 0 and abs(cur - l) < len(name) - 1:
#             l += 1
        
#         if first == 1 and l != r:
#             ll = l + 1
#             while route[cur - ll] == 0 and abs(cur - ll) < len(name) - 1:
#                 ll += 1
#             ll - 1
#             if ll < l:
#                 cur += r
#                 count += r
#             else:
#                 cur -= l
#                 count += l
#             continue
        
#         if l == r:
#             rr = ll = r + 1
#             while route[cur + rr] == 0 and cur + rr < len(name) - 1:
#                 rr += 1
#             while route[cur - ll] == 0 and abs(cur - ll) < len(name) - 1:
#                 ll += 1
#             # if first == 1:
#             #     if ll - 1 >= l:
#             #         cur += r
#             #         count += r
#             #     else:
#             #         cur -= l
#             #         count += l
#             # else:
#             if ll < rr:
#                 cur += r
#                 count += r
#             else:
#                 cur -= l
#                 count += l
#         else:
#             if l > r:
#                 cur += r
#                 count += r
#             else:
#                 cur -= l
#                 count += l
#     return -1

# def solution(name):
#     answer = 0
#     count = list(min(ord(i) - ord("A"), ord("Z") - ord(i) + 1) for i in name)
#     idx = 0
#     check = 1
#     while True:
#         answer += count[idx]
#         count[idx] = 0
#         if idx != 0:
#             check = 0
#         if sum(count) == 0:
#             return answer
        
#         r = l = 1
#         idx_r = 1 + idx
#         idx_l = idx - 1
        
#         while count[idx_r] == 0:
#             if idx_r >= len(name):
#                 idx_r = 0
#                 r += 1
#             else:
#                 idx_r += 1
#                 r += 1
#         while count[idx_l] == 0:
#             if idx_l < -(len(name)):
#                 idx_l = -1
#                 l += 1
#             else:
#                 idx_l -= 1
#                 l += 1
        
#         if check == 1:
#             rr = ll = 1
#             if r >= len(name) - 1:
#                 idx_rr = 0
#             else:
#                 idx_rr = r + 1
#             if l < -len(name) + 1:
#                 idx_ll = -1
#             else:
#                 idx_ll = l - 1
            
#             while count[idx_rr] == 0:
#                 if idx_rr >= len(name):
#                     idx_rr = 0
#                     rr += 1
#                 else:
#                     idx_rr += 1
#                     rr += 1
#             while count[idx_ll] == 0:
#                 if idx_ll < -len(name):
#                     idx_ll = -1
#                     ll += 1
#                 else:
#                     idx_ll -= 1
#                     ll += 1
            
#             if ll < rr:
#                 answer += r
#                 idx += r
#             else:
#                 answer += l
#                 idx -= l
#         else:
#             if l > r:
#                 answer += r
#                 idx += r
#             else:
#                 answer += l
#                 idx -= l
                
# def solution(name):
#     answer = 0
#     count = list(min(ord(i) - ord("A"), ord("Z") - ord(i) + 1) for i in name)
#     idx = 0
#     check = 1
#     while True:
#         answer += count[idx]
#         count[idx] = 0
#         if idx != 0:
#             check = 0
#         if sum(count) == 0:
#             return answer
        
#         r = l = 1
#         if idx + 1 > len(name) - 1:
#             idx_r = 0
#         else:
#             idx_r = 1 + idx
#         if idx - 1 < -len(name):
#             idx_l = -1
#         else:
#             idx_l = idx - 1
        
#         while count[idx_r] == 0:
#             if idx_r >= len(name):
#                 idx_r = 0
#                 r += 1
#             else:
#                 idx_r += 1
#                 r += 1
#         while count[idx_l] == 0:
#             if idx_l < -(len(name)):
#                 idx_l = -1
#                 l += 1
#             else:
#                 idx_l -= 1
#                 l += 1
#         if check == 1 and len(name) > 3:
#             rr = ll = 1
#             if r + 1 > len(name) - 1:
#                 idx_rr = 0
#             else:
#                 idx_rr = r + 1
#             if l - 1 < -len(name):
#                 idx_ll = -1
#             else:
#                 idx_ll = l - 1
            
#             while count[idx_rr] == 0:
#                 if idx_rr > len(name) - 1:
#                     idx_rr = 0
#                     rr += 1
#                 else:
#                     idx_rr += 1
#                     rr += 1
#             while count[idx_ll] == 0:
#                 if idx_ll < -len(name):
#                     idx_ll = -1
#                     ll += 1
#                 else:
#                     idx_ll -= 1
#                     ll += 1
#             if ll <= rr:
#                 answer += r
#                 idx += r
#             else:
#                 answer += l
#                 idx -= l
#         else:
#             if l > r:
#                 answer += r
#                 idx += r
#             else:
#                 answer += l
#                 idx -= l
                
def solution(name):
    answer = 0
    count = list(min(ord(i) - ord("A"), ord("Z") - ord(i) + 1) for i in name)
    idx = 0
    check = 1
    while True:
        answer += count[idx]
        count[idx] = 0
        if idx != 0:
            check = 0
        if sum(count) == 0:
            return answer
        
        r = l = 1
        if idx + 1 > len(name) - 1:
            idx_r = 0
        else:
            idx_r = 1 + idx
        if idx - 1 < -len(name):
            idx_l = -1
        else:
            idx_l = idx - 1
        
        while count[idx_r] == 0 and idx_r != idx:
            if idx_r >= len(name):
                idx_r = 0
                r += 1
            else:
                idx_r += 1
                r += 1
        while count[idx_l] == 0 and idx_r != idx:
            if idx_l < -(len(name)):
                idx_l = -1
                l += 1
            else:
                idx_l -= 1
                l += 1
        if check == 1:
            if r + 1 > len(name) - 1:
                rr = 0
            else:
                rr = r + 1
            if l - 1 < -len(name):
                ll = -1
            else:
                ll = l - 1
            rc = lc = 0
            while count[rr] != 0 and rr != idx_r:
                if rr > len(name) - 1:
                    rr = 0
                    rc += 1
                else:
                    rr += 1
                    rc += 1
            while count[ll] != 0 and ll != idx_l:
                if ll < -len(name):
                    ll = -1
                    lc += 1
                else:
                    ll -= 1
                    lc += 1
            if lc > rc:
                answer += r
                idx += r
            else:
                answer += l
                idx -= l
        else:
            if l > r:
                answer += r
                idx += r
            else:
                answer += l
                idx -= l
                
def solution(name):
    answer = 0
    count = list(min(ord(i) - ord("A"), ord("Z") - ord(i) + 1) for i in name)
    idx = 0
    first = 1
    while True:
        answer += count[idx]
        count[idx] = 0
        
        if sum(count) == 0:
            return answer
        
        if first == 1:
            r = l = 1
            while count[r] == 0:
                r += 1
            while count[-l] == 0:
                l += 1
                
            if 0 in count[1:] and len(count) > 3:
                rr = r + 1
                ll = l + 1
                rrcount = llcount = 1
                
                while count[rr] != 0:
                    if rr > len(count) - 1:
                        rr = 0
                        rrcount += 1
                    else:
                        rr += 1
                        rrcount += 1
                while count[-ll] != 0:
                    if -ll < -len(count):
                        ll = -1
                        llcount += 1
                    else:
                        ll += 1
                        llcount += 1
                if ll >= rr:
                    idx += r
                    answer += r
                else:
                    idx -= l
                    answer += l
            else:
                if l > r:
                    idx += r
                    answer += r
                else:
                    idx -= l
                    answer += l
            first = 0
        else:
            r = idx + 1
            l = idx - 1
            rcount = lcount = 1
            while count[r] == 0:
                if r == len(count) - 1:
                    r = 0
                    rcount += 1
                else:
                    r += 1
                    rcount += 1
            while count[l] == 0:
                if l == 0 or l == -len(count):
                    l = len(count) - 1
                    lcount += 1
                else:
                    l -= 1
                    lcount += 1
            
            if lcount >= rcount:
                idx += rcount
                answer += rcount
            else:
                idx -= lcount
                answer += lcount


def dfs(node, graph):
    
    result = []
    for i in graph[node]:
        s = [i]
        route = [node]
        
        while True:
            cur = s.pop()
            
            if cur not in route:
                route.append(cur)
                s.extend(graph[cur])
            else:
                result.append(route)
                break
    return result

def solution(name):
    answer = 0
    count = list(min(ord(i) - ord("A"), ord("Z") - ord(i) + 1) for i in name)
    
    index = 0
    while True:
        answer += count[index]
        count[index] = 0
        if sum(count) == 0:
            return answer
        left_route = []
        right_route = []
        left, right = 0, 0
        
        for i in range(1, len(count)):
            x = index - i
            if x < -len(count):
                x = -1
            left_route.append([x, count[x]])
            left += count[x] + 1
        for i in range(-1, -len(count), -1):
            if left_route[i][1] == 0:
                left -= 1
            else:
                break
        
        for i in range(1, len(count)):
            x = index + i
            if x > len(count) - 1:
                x = 0
            right_route.append([x, count[x]])
            right += count[x] + 1
        
        for i in range(-1, -len(count), -1):
            if right_route[i][1] == 0:
                right -= 1
            else:
                break
        
        ll, rr = 1, 1
        while count[index + rr] == 0:
            rr += 1
        while count[index - ll] == 0:
            ll += 1
        
        if left > right:
            index += rr
            answer += rr
        else:
            index -= ll
            answer += ll
    






name = "JEROEN"
name = "ABAAB"
# name = "JAN"
# name = "JAZ"
# name = "AABAAAAABBA"
# name = "AAAA"
# name = "BAABA"
# name = "BBABAAAB"
# name = "ABAAAAAAAAABA"
# name = "BBBBAAAABA"

print(solution(name))