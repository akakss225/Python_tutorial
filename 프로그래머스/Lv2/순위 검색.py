from itertools import combinations
from bisect import bisect_left

# 시간효율 그지...
def solution(info, query):
    answer = [0] * len(query)
    for i in info:
        count = [k for k in range(len(i)) if i[k] == " "]
        for j in range(len(query)):
            condition = query[j].split(" ")
            check = 1
            for c in condition:
                if c == "and" or c == "-":
                    continue
                if c.isdigit():
                    if int(c) > int(i[count[-1]:]):
                        check = 0
                        break
                else:
                    if c not in i:
                        check = 0
                        break
            if check:
                answer[j] += 1
    return answer

# 조금 개선.
def solution(info, query):
    answer = [0] * len(query)
    for i in range(len(info)):
        person = info[i].split(" ")
        for j in range(len(query)):
            check = 1
            for condition in query[j].split(" "):
                if condition == "-" or condition == "and":
                    continue
                if condition.isdigit():
                    if int(condition) > int(person[-1]):
                        check = 0
                        break
                else:
                    if condition not in person:
                        check = 0
                        break
            if check:
                answer[j] += 1
    return answer

def solution(information, query):
    answer = []
    info_dict = dict()
    for i in range(len(information)):
        info = information[i].split()
        info_key = info[:-1]
        info_value = info[-1]
        
        for j in range(len(info_key)+1):
            for c in combinations(info_key, j):
                temp = "".join(c)
                if temp in info_dict:
                    info_dict[temp].append(int(info_value))
                else:
                    info_dict[temp] = [int(info_value)]
    for k in info_dict:
        info_dict[k].sort()
    
    for q in query:
        condition = q.split()
        condition_key = condition[:-1]
        condition_val = condition[-1]
        
        while "and" in condition_key:
            condition_key.remove("and")
        while "-" in condition_key:
            condition_key.remove("-")
        condition_key = "".join(condition_key)
        print(condition_key)
        
        if condition_key in info_dict:
            scores = info_dict[condition_key]
            
            if scores:
                under = bisect_left(scores, int(condition_val))
                answer.append(len(scores) - under)
        else:
            answer.append(0)
    return answer





info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]

print(solution(info, query))
