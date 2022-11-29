# 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 
# 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 
# 예를 들어 strings가 ["sun", "bed", "car"]이고 
# n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.

def solution(strings, n):
    strings.sort()
    answer = []
    arr = []
    for i in range(len(strings)):
        arr.append([strings[i][n], i])
    arr.sort()
    for i in arr:
        answer.append(strings[i[1]])
    return answer

strings = ["sun", "bed", "car"]
n = 1

print(solution(strings, n))


def strange_sort(strings, n):
    return sorted(strings, key=lambda x: x[n])