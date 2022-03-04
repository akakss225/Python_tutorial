# IDEA
# 1. 3가지 연산자에 대하여, 순열을 구한다
# 2. 만들어진 연산자 순열을 사용한 반복문을 실행한다.
# 3. 문자열을 돌며, 현재 연산자 기준 좌, 우를 확인해 계산한다.
# 4. 계산된 숫자를 원래 문자열이 있던 index에 넣어준다.
# 5. 계산이 끝나면 list에 남은 숫자를 절댓값을 씌워 answer에 추가해준다.

from itertools import permutations

def solution(e):
    # 우선순위에 따른 계산값을 넣어줄 list
    answer = []
    
    # 연산자의 우선순위를 나타낼 순열 생성
    oper = list(permutations(["*", "+", "-"]))
    
    # 우선순위에 따른 반복문 실행
    for i in oper:
        
        # 계산을 위해 e를 list화 해줌.
        a = list(e)
        
        # 우선순위가 설정된 연산자 list를 돌 반복문
        for j in i:
            
            # 연산자가 a list에 존재한다면 반복문 실행
            while j in a:
                
                # 연산자의 index를 구해줌
                idx = a.index(j)
                
                # 연산자를 기준으로 좌/우 를 확인하며 숫자인 경우까지만 index를 구해줌
                left = idx - 1
                right = idx + 1
                while a[left].isdigit() and left >= 0:
                    left -= 1
                while a[right].isdigit() and right < len(a)-1:
                    right += 1
                
                # right값이 list의 마지막 인덱스인 경우
                # 또한 right값이 바로 다음인 경우
                # right에 +1을 해줌. >> 포함이 되어야하기 때문
                if right == len(a)-1 or right == idx + 1:
                    right += 1
                # left값이 0 이 아닌경우
                # 동시에 left 값이 바로 옆이 아닌 경우
                # left에 +1을 해줌. >> 포함이 되면 안되기 때문
                if left != 0:
                    if left != idx - 1:
                        left += 1
                
                # 계산되어야할 범위를 표시할 cal 변수 생성
                cal = a[left:right]
                # eval 메소드를 계속 사용하기 위해, str형태로 만들어줌.
                cal = str(eval("".join(cal)))
                # 원래 a list의 계산이 되는 구간을 제외 하고,
                # 동일한 위치에 계산된 값 cal을 삽입해줌.
                a = a[:left] + [cal] + a[right:]
                
        # 우선순위에 대한 반복문이 다 끝났을 때
        # 이 경우, 숫자 앞에 -값이 붙어있다면, a 에 값이 여러개가 올 수 있음
        # 따라서, a 가 하나가 아닌경우, 그대로 전부 계산해 주면 됨.
        # 만일 하나인 경우, 그 값을 answer에 추가해줌.
        if len(a) != 1:
            answer.append(abs(eval("".join(a))))
        else:
            answer.append(abs(int(a[0])))
    
    # 정답은 answer에 존재하는 값중 가장 큰 값이 됨.
    return max(answer)


e = "100-200*300-500+20"
# e = "50*6-3*2"
# e = "2*2*2*2*2-2*2*2"
# e = "200-300-500-600*40+500+500"
# e = "177-661*999*99-133+221+334+555-166-144-551-166*166-166*166-133*88*55-11*4+55*888*454*12+11-66+444*99"
print(solution(e))