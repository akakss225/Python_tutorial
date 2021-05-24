'''
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
'''

def solution(numbers):
    result = ''
    for i in range(len(numbers)):
        a = 0
        max = [0,0,0,0]
        idx = 0
        while a < len(numbers):
            x = list(map(int, list(str(numbers[a]))))
            if max[0] < x[0]:
                max = x
                idx = numbers.index(numbers[a])
            elif max[0] == x[0]:
                if len(max) < len(x):
                    if len(x) == 2 and  max[0] < x[1]:
                        max = x
                        idx = numbers.index(numbers[a])
                elif len(max) == len(x) and len(max) == 2:
                    if max[1] < x[1]:
                        max = x
                        idx = numbers.index(numbers[a])
                elif len(max) == len(x) and len(max) == 3:
                    if max[1] < x[1]:
                        max = x
                        idx = numbers.index(numbers[a])
                    elif max[1] == x[1]:
                        if max[2] < x[2]:
                            max = x
                            idx = numbers.index(numbers[a])
                elif len(max) == len(x) and len(max) == 4:
                        if max[1] < x[1]:
                            max = x
                            idx = numbers.index(numbers[a])
                        elif max[1] == x[1]:
                            if max[2] < x[2]:
                                max = x
                                idx = numbers.index(numbers[a])
                            elif max[2] == x[x]:
                                if max[3] < x[3]:
                                    max = x
                                    idx = numbers.index(numbers[a])
            a += 1
        result = result + str(numbers.pop(idx))
    return result

numbers = [6,10,2]

print(solution(numbers))

'''
def solution(numbers):
    answer = ''
    max = [0,0,0,0]
    for i in range(len(numbers)):
        idx = 0
        a = 0
        while a < len(numbers):
            x = list(map(int , list(str(numbers[a]))))
            if max[0] < x[0]:
                max = x
                idx = numbers.index(numbers[a])
            elif max[0] == x[0]:
                if len(max) < len(x):
                    if max[0] < x[1]:
                        max = x
                        idx = numbers.index(numbers[a])
                else:
                    if max[1] < x[0]:
                        max = x
                        idx = numbers.index(numbers[a])
            elif len(max) < len(x):
                if max[0] < x[1]:
                    max = x
                    idx = numbers.index(numbers[a])
            a += 1
        answer += str(numbers.pop(idx))
    return answer

numbers = [90,908,89,898,10,101,1,8,9]
print(solution(numbers))
'''