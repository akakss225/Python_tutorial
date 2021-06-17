# 재귀함수로, 이는 일종의 함수를 스택 자료구조를 이용해 호출하는 방식을 사용한다.

def reculsive(i):
    if i == 100:
        return
    print(i ,'번째 재귀함수에서,' , i + 1 ,'번째 재귀함수를 호출합니다.')
    reculsive(i+1)
    print(i,'번째 재귀함수를 종료합니다.')
    
reculsive(1)