# 지도는 한 변의 길이가 n인 정사각형 배열 형태로, 각 칸은 "공백"(" ") 또는 "벽"("#") 두 종류로 이루어져 있다.
# 전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있다. 각각 "지도 1"과 "지도 2"라고 하자. 지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽이다. 지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다.
# "지도 1"과 "지도 2"는 각각 정수 배열로 암호화되어 있다.
# 암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1, 공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열이다.
from collections import deque as dq

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        ar1 = dq(list(bin(arr1[i])[2:]))
        ar2 = dq(list(bin(arr2[i])[2:]))
        
        if len(ar1) < n:
            while len(ar1) != n:
                ar1.appendleft('0')
        if len(ar2) < n:
            while len(ar2) != n:
                ar2.appendleft('0')
        tmp = ''
        for j in range(n):
            if ar1[j] == '1' or ar2[j] == '1':
                tmp += '#'
            else:
                tmp += ' '
        answer.append(tmp)
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

print(solution(n, arr1, arr2))