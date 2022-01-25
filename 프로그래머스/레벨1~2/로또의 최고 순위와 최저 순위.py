# 모두일치 >> 1등
# 5개 >> 2등
# 4개 >> 3등
# 3개 >> 4등
# 2개 >> 5등
# 1개 이하 >> 6


def solution(lottos, win_nums):
    answer = []
    garbage = []
    while lottos:
        for i in range(len(lottos)):
            for j in win_nums:
                if lottos[i] == j:
                    answer.append(lottos[i])
                    lottos.remove(lottos[i])
                    break
            garbage.append(lottos[i])
            lottos.remove(lottos[i])
            break
    
    return answer



a = [44, 1, 0, 0, 31, 25]
b = [31, 10, 45, 1, 6, 19]
print(solution(a,b))