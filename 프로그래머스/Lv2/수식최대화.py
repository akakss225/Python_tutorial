# IDEA
# 1. 3가지 연산자에 대하여, 순열을 구한다
# 2. 만들어진 연산자 순열을 사용한 반복문을 실행한다.
# 3. 문자열을 돌며, 현재 연산자 기준 좌, 우를 확인해 계산한다.
# 4. 계산된 숫자를 원래 문자열이 있던 index에 넣어준다.
# 5. 이때, 계산된 숫자가 음수이고 처음일 경우, 음수 그대로 넣어주고 숫자가 중간일 경우 절댓값을 넣어준다.


from itertools import permutations

def solution(expression):
    answer = []
    oper = list(permutations(["*", "+", "-"]))
    
    for i in oper:
        a = list(expression)
        num = 0
        for j in i:
            while j in a:
                idx = a.index(j)
        
                left = -1
                right = 1
                while a[idx+left].isdigit() and idx+left >= 0:
                    left -= 1
                while a[idx+right].isdigit() and idx+right < len(a)-1:
                    right += 1
                if idx + right == len(a)-1:
                    right += 1
                if left != -1:
                    cal = a[idx+left+1:idx+right]
                    cal = str(eval("".join(cal)))
                    a = a[:idx+left+1] + [cal] +  a[idx+right:]
                else:
                    cal = a[idx+left:idx+right]
                    cal = str(eval("".join(cal)))
                    a = a[:idx+left+1] + [cal] +  a[idx+right:]
                if len(a) == 2:
                    num = int(a[-1])
                    break
        answer.append(abs(num))
    return answer


e = "100-200*300-500+20"

print(solution(e))