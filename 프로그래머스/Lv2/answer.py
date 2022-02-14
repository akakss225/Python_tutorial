# <!-- 문제
#   배열과 수를 주어주는데
#   배열의 인접한 요소들끼리의 차이가 주어진 수 이하가 되도록 하기 위해 두개의 요소를 스위칭하는데
#   이때 최소로 바꾸면서 인접요소끼리의 차이가 주어진 수 이하일 경우의 수를 반환해라
#   만약 아무리 바꿔도 주어진 수 이하로 인접요소끼리 차이를 좁힐 수 없다면 -1을 반환해라.
# -->


def solution(l, k):
    answer = 0
    idx = 0
    while True:
        if idx + 1 >= len(l):
            return answer
        
        cur = l[idx]
        next = l[idx + 1]
        
        if abs(cur - next) > k:
            if cur > next:
                changed = idx + 1
                fixed = idx
            else:
                changed = idx
                fixed = idx + 1
                
            min_num = 99999999
            min_idx = -1
            for i in range(idx + 2, len(l)):
                if abs(l[i] - l[fixed]) <= k and min_num > l[i]:
                    min_num = l[i]
                    min_idx = i
                    
            
            if min_num == 99999999:
                return -1
            
            l[changed], l[min_idx] = l[min_idx], l[changed]
            answer += 1
            idx += 1
        else:
            idx += 1



l = [10, 40, 30, 20]
k = 20
# l = [3, 7, 2, 8, 6, 4, 5 ,1]
# k = 3
# l = [6, 9, 11, 4, 5, 2]
# k = 4

print(solution(l, k))
