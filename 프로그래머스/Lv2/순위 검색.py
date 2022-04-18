
def solution(info, query):
    answer = [0] * len(query)
    people = dict()
    for i in range(len(info)):
        people[i] = info[i].split(" ")
    conditions = []
    for i in range(len(query)):
        temp = query[i].split(" ")
        while "-" in temp or "and" in temp:
            if "-" in temp:
                temp.remove("-")
            if "and" in temp:
                temp.remove("and")
        conditions.append(temp)
    
    for i in range(len(people)):
        for condition in range(len(conditions)):
            check = 1
            for c in conditions[condition]:
                if c in people[i]:
                    continue
                else:
                    if c.isdigit():
                        if int(people[i][-1]) >= int(c):
                            continue
                        else:
                            check = 0
                            break
                    else:
                        check = 0
                        break
            if check == 1:
                answer[condition] += 1
    
    return answer

def solution(info, query):
    answer = [0] * len(query)
    conditions = []
    for i in range(len(query)):
        temp = query[i].split(" ")
        while "-" in temp or "and" in temp:
            if "-" in temp:
                temp.remove("-")
            if "and" in temp:
                temp.remove("and")
        conditions.append(temp)
    
    for i in range(len(info)):
        for condition in range(len(conditions)):
            check = 1
            for c in conditions[condition]:
                if c in info[i]:
                    continue
                else:
                    if c.isdigit():
                        if int(info[i][-3:]) >= int(c):
                            continue
                        else:
                            check = 0
                            break
                    else:
                        check = 0
                        break
            if check == 1:
                answer[condition] += 1
    return answer


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

def solution(info, query):
    answer = 0
    information = dict()
    for i in range(len(info)):
        information[i] = info[i].split(" ")[:-1]
        information[i].append(int(info[i].split(" ")[-1]))
    conditions = dict()
    for i in range(len(query)):
        condition = []
        for j in query[i].split(" "):
            if j == "and" or j == "-":
                continue
            else:
                if j.isdigit():
                    condition.append(int(j))
                else:
                    condition.append(j)
        conditions[i] = condition
    
    return conditions




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
