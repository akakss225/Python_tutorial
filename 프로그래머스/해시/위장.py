def solution(clothes):
    result = []
    d = dict()
    for i in range(len(clothes)):
        d[i] = clothes[i][1]
        result.append([i])
            
    for i in range(len(d)):
        l = [d[i]]
        temp = [i]
        for j in range(i + 1, len(d)):
            temp_2 = [i]
            if d[j] not in l and j not in temp:
                temp.append(j)
                temp_2.append(j)
                l.append(d[j])
                a = sorted(temp_2)
                if a not in result:
                    result.append(a)
        if temp not in result:
            result.append(temp)
    return result


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def solution(clothes):
    d = dict()
    answer = 1
    for i in clothes:
        if i[1] in d:
            d[i[1]] += 1
        else:
            d[i[1]] = 1
    
    for i in d:
        answer *= d[i] + 1
    
    return answer

clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
# clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"], ["mask", "face"]]
# clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
# clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"], ["yellowhat", "headgear"]]
# clothes = [["crow_mask", "face"], ["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(clothes))