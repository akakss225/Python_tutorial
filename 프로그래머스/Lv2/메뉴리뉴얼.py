# IDEA
# 1. orders 에서 각각 주문한 종류에 대하여 course를 돌며 모든 코스메뉴 종류를 조합으로 구함
# 2. (1) 에서 구한 조합을 temp list에 넣고, 만약 temp list에 다음 메뉴에 포함된 값이 있으면, combi에 넣어줌
# 3. combi를 돌며, 메뉴에 대한 HashMap을 만들어줌. key = menu / value = 중복된 횟수
# 4. value값으로 내림차순 정렬을 한 후, 다시 course를 돌며, 각 코스에서 가장 큰 수를 answer에 append
# 5. 오름차순 answer를 return 해줌.


# Code Review
# 우선, 가짓수 별로 조합을 해야하므로, len(course) * len(orders) * (최소)len(orders[0])!의 시간복잡도를 갖음.
# 또한 추가로 len(combi) 의 시간복잡도와, len(course) * len(menu) 의 시간복잡도가 추가된다.
# 즉, 굉장히 비효율적인 코드... 효율성을 고려한 코드로 ReFactoring 과정을 한번 해봐야 할듯 하다.

from itertools import combinations

def solution(orders, course):
    # 정답을 담을 list
    answer = []
    
    # 최소 2번 이상 짝지어진적 있는 메뉴를 담을 list
    combi = []
    
    # 모든 세트메뉴가 될 수 있는 조합을 담을 list
    temp = []
    
    for i in course:
        for j in orders:
            # 주문에 대하여 만들 수 있는 모든 조합을 구한 cur list를 만듬.
            cur = list(combinations(sorted(j), i))
            
            # cur을 돌면서, temp 와 확인 한뒤, temp에 존재하면 combi에 넣어줌
            for k in cur:
                if k in temp:
                    combi.append(k)
                else:
                    # temp 에 없다면, temp에 먼저 넣어줌.
                    temp.append(k)
    
    # 총 몇번이나 같은 메뉴가 동시에 주문이 되었는지 counting할 map을 만들어줌.
    menu = dict()
    for i in combi:
        # retrun 형식을 맞춰주기 위한 key값을 설정.
        if "".join(i) in menu:
            # menu에 있다면, value 값을 +1 해줌
            menu["".join(i)] += 1
        else:
            # menu에 없다면, 등록해줌.
            menu["".join(i)] = 1
    
    # 각 course별로, 가장 많이 주문된 세트를 구해야하기 때문에,
    # dict을 value 값에 따른 내림차순으로 정렬해주어야 함.
    menu = sorted(menu.items(), key=lambda x:x[1], reverse=True)
    
    # 각 course별 최댓값을 구하기위한 반복문
    for i in course:
        big = 0
        for j in menu:
            # 메뉴에 따라 big값을 갱신하며, 가장 많이 주문된 것들만 answer에 담아줌.
            if len(j[0]) == i and big <= j[1]:
                big = j[1]
                answer.append(j[0])
    # answer가 스펠링을 기준으로 정렬되게 해서 return해줌.
    return sorted(answer)


o = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
c = [2,3,4]	

print(solution(o, c))