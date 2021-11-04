def solution(record):
    answer = []
    enter = "님이 들어왔습니다."
    leave = "님이 나갔습니다."
    dic = {}
    for i in record:
        if i.split()[0] == "Enter" or i.split()[0] == "Change":
            dic[i.split()[1]] = i.split()[2]
            dic[i.split()[1]] = i.split()[2]
    for i in record:
        if(i.split()[0] == "Enter"):
            answer.append(dic[i.split()[1]] + enter)
        elif(i.split()[0] == "Leave"):
            answer.append(dic[i.split()[1]] + leave)
    
    return answer
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))
