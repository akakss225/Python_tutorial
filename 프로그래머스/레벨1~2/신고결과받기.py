# def solution(id_list, report, k):
#     answer = dict()
#     count = [0] * len(id_list)
#     for i in id_list:
#         answer[i] = []
#     for i in report:
#         cur = i.split()
#         answer[cur[0]].append(cur[1])
#         count[id_list.index(cur[1])] += 1
#     return count




def solution(id_list, report, k):
    answer = {i : [] for i in id_list}
    report = set(report)
    count = [0] * len(id_list)
    result = [0] * len(id_list)
    mail = []
    for i in report:
        cur = i.split()
        answer[cur[0]].append(cur[1])
        count[id_list.index(cur[1])] += 1
    for i in range(len(count)):
        if count[i] >= k:
            mail.append(id_list[i])
    for i in range(len(count)):
        for j in mail:
            if j in answer[id_list[i]]:
                result[i] += 1
    return result

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

print(solution(id_list, report, k))