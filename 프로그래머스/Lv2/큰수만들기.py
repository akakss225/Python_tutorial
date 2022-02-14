from collections import deque
from aem import con

from sklearn.metrics import jaccard_score

def solution(number, k):
    answer = list(number)
    
    n = 0
    idx = 0
    while n != k:
        big = int(answer[idx])
        if big < int(answer[idx + 1]):
            answer.remove(str(big))
            n += 1
            idx = 0
        else:
            idx += 1
    
    return "".join(answer)

def solution(number, k):
    n = 0
    idx = 0
    while n != k:
        check = 0
        big = int(number[idx])
        if big < int(number[idx + 1]):
            number = number[:idx] + number[idx+1:]
            n += 1
        else:
            for i in range(1, k-n+1):
                if int(number[idx + i]) > big:
                    number = number[:idx] + number[idx+i:]
                    n += i
                    check = 1
                    break
            if check == 1:
                continue
            else:
                idx += 1
    
    return number

def solution(number, k):
    n = 0
    idx = 0
    while n != k:
        if len(set(number)) == 1:
            number = number[k - n:]
            break
        big = int(number[idx])
        if big < int(number[idx + 1]):
            number = number[:idx] + number[idx+1:]
            n += 1
            idx = 0
        else:
            idx += 1
    
    return number

def solution(number, k):
    idx = 0
    while k != 0:
        if len(set(number)) == 1:
            number = number[k:]
            break
        big = int(number[idx])
        if big < int(number[idx + 1]):
            number = number[:idx] + number[idx+1:]
            k -= 1
        elif big > int(number[idx + 1]):
            number = number[:idx+1] + number[idx+2:]
            k -=1
        else:
            idx += 1
    return number

def solution(number, k):
    idx = 0
    while k != 0:
        if len(set(number)) == 1:
            number = number[k:]
            break
        big = int(number[idx])
        if big < int(number[idx + 1]):
            number = number[:idx] + number[idx+1:]
            k -= 1
        elif big == int(number[idx + 1]):
            idx += 1
        else:
            count = 1
            while big > int(number[idx + count]) and idx + count < len(number) - idx - 1:
                count += 1
            if count - 1 < k:
                number = number[:idx] + number[idx+count:]
                k -= count
            else:
                idx += 1
        
    return number

def solution(number, k):
    for i in range(k):
        for x in range(len(number)):
            for y in range(x+1, len(number)):
                if int(number[x]) < int(number[y]):
                    number = number[:x] + number[x+1:]
                    break
                elif int(number[x]) > int(number[y]):
                    number = number[:y] + number[y+1:]
                    break
                else:
                    continue
            break
    return number

def solution(number, k):
    for i in range(k):
        nums = []
        for j in range(len(number)):
            lastest = number[:j] + number[j+1:]
            nums.append(lastest)
            bigest = max(nums)
            if lastest != bigest:
                number = max(nums)
                break
    return number

def solution(number, k):
    for i in range(k):
        check = len(number)
        for j in range(1, len(number)):
            pre = number[:j-1] + number[j:]
            cur = number[:j] + number[j+1:]
            if int(pre) > int(cur):
                number = pre
                break
        if check == len(number):
            number = number[:-1]
    return number

def solution(number, k):
    while k != 0:
        check = len(number)
        for j in range(1, len(number)):
            pre = number[:j-1] + number[j:]
            cur = number[:j] + number[j+1:]
            if int(pre) > int(cur):
                number = pre
                break
        if check == len(number):
            number = number[:-1]
        k -= 1
    return number

def solution(number, k):
    idx = 0
    while k != 0:
        first = number[0]
        if idx == 0:
            for i in range(1, len(number)):
                if first == number[i]:
                    idx += 1
                else:
                    break
        check = len(number)
        for j in range(idx, len(number)-2):
            pre = number[:j] + number[j+1:]
            cur = number[:j+1] + number[j+2:]
            if int(pre) > int(cur):
                number = pre
                break
        if check == len(number):
            number = number[:-1]
        k -= 1
    return number



# IDEA
# 제공된 number의 index는 고정된 상태로, 제거할 숫자의 갯수 k가 주어졌을 때
# 제거후, 가장 큰 숫자가 되게 해야함
# 1. 되도록이면, max값이 맨 앞에 오는게 좋음
# 2. 앞에서부터 확인해서, 작은 숫자를 일단 지우는게 좋음
# 3. 만약 제거할 숫자만큼 앞 숫자가 작은것만 있다면, 앞숫자만 다 지우는게 좋음
# 4. 맨앞에 적당히 큰 숫자가 왔다면, 그 뒤의 숫자 중 작은걸 지우면 됨.




number = "1924"
k = 2
# number = "1231234"
# k = 3
# number = "4177252841"
# k = 4
# number = '77777'
# k = 1
# number = "1000000"
# k = 1


print(solution(number, k))