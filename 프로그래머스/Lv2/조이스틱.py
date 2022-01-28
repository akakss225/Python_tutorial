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
    count = 0
    route = [min(ord(i) - ord("A"), ord("Z") - ord(i) + 1) for i in name]
    
    cur = 0
    first = 1
    while True:
        count += route[cur]
        route[cur] = 0
        if cur != 0:
            first = 0
            
        if sum(route) == 0:
            return count
        
        r = l = 1
        while route[cur - l] == 0:
            l += 1
        while route[cur + r] == 0:
            r += 1
        
        if first == 1:
            rr = ll = 2
            while route[cur - ll] == 0 and abs(cur - ll) < len(name) - 1:
                ll += 1
            while route[cur + rr] == 0 and cur + rr < len(name) - 1:
                rr += 1
            if ll < rr:
                cur += r
                count += r
            else:
                cur -= l
                count += l
        else:
            if l > r:
                cur += r
                count += r
            else:
                cur -= l
                count += l

name = "JEROEN"
# name = "ABAAB"
name = "JAN"
# name = "JAZ"
name = "ABAAAAAABB"
# name = "AAAA"
# name = "BAABA"
# name = "BBABAAAB"
# name = "BBBBAABABA"

print(solution(name))