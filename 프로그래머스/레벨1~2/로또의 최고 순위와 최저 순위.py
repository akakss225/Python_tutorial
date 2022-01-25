
def solution(lottos, win_nums):
    answer = []
    garbage = []
    result = []
    while lottos:
        for i in range(len(lottos)):
            check = 0
            for j in win_nums:
                if lottos[i] == j:
                    answer.append(lottos[i])
                    lottos.remove(lottos[i])
                    check = 1
                    break
            if check == 1:
                break
            garbage.append(lottos[i])
            lottos.remove(lottos[i])
            break
    if len(answer) == 6:
        result.append(1)
        result.append(1)
    elif len(answer) == 5:
        result.append(2)
        if garbage.count(0) > 0:
            result.append(result[0] - 1)
        else:
            result.append(2)
    elif len(answer) == 4:
        result.append(3)
        if garbage.count(0) > 0:
            result.append(result[0] - garbage.count(0))
        else:
            result.append(3)
    elif len(answer) == 3:
        result.append(4)
        if garbage.count(0) > 0:
            result.append(result[0] - garbage.count(0))
        else:
            result.append(4)
    elif len(answer) == 2:
        result.append(5)
        if garbage.count(0) > 0:
            result.append(result[0] - garbage.count(0))
        else:
            result.append(5)
    elif len(answer) == 1:
        result.append(6)
        if garbage.count(0) > 0:
            result.append(result[0] - garbage.count(0))
        else:
            result.append(6)
    else:
        result.append(6)
        if garbage.count(0) == 6:
            result.append(1)
        elif garbage.count(0) == 1:
            result.append(6)
        else:
            result.append(result[0] - garbage.count(0))
    
    return sorted(result)

def solution2(lottos, win_nums):
    answer = 0
    rank = {0 : 6, 1 : 6, 2 : 5, 3 : 4, 4 : 3, 5 : 2, 6 : 1}
    cnt_0 = lottos.count(0)
    for i in lottos:
        if i in win_nums:
            answer += 1
        
    return sorted([rank[answer], rank[answer+cnt_0]])


a = [44, 1, 0, 0, 31, 25]
b = [31, 10, 45, 1, 6, 19]
print(solution2(a,b))