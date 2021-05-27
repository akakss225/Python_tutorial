# 문제 설명
# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# numbers는 길이 1 이상 7 이하인 문자열입니다.
# numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

def prime(num):
    if num <= 1:
        return False
    elif num == 2 or num == 3:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def solution(numbers):
    temp_list = []
    if len(numbers) < 3:
        for i in numbers:
            number = list(map(str, numbers)).sort()
            number.remove(i)
            for j in number:
                if prime(int(i+j)) == True:
                    if (i+j) not in temp_list:
                        temp_list.append(i+j)
                if prime(int(i)) == True:
                    if i != j:
                        temp_list.append(i)
    elif len(numbers) == 3:
        for i in numbers:
            number = list(map(str, numbers))
            number.remove(i)
            for j in number:
                number.remove(j)
                for k in number:
                    if prime(int(i+j+k)) == True:
                        if (i+j) not in temp_list:
                            temp_list.append(i+j)
                    if prime(int(i)) == True:
                        if i != j:
                            temp_list.append(i)
    elif len(numbers) == 4:
        for i in numbers:
            number = list(map(str, numbers))
            number.remove(i)
            for j in number:
                number.remove(j)
                for k in number:
                    number.remove(k)
                    for x in number:
                        if prime(int(i+j+k+x)) == True:
                            if (i+j) not in temp_list:
                                temp_list.append(i+j)
                        if prime(int(i)) == True:
                            if i != j:
                                temp_list.append(i)
    elif len(numbers) == 5:
        for i in numbers:
            number = list(map(str, numbers))
            number.remove(i)
            for j in number:
                number.remove(j)
                for k in number:
                    number.remove(k)
                    for x in number:
                        number.remove(x)
                        for y in number:
                            if prime(int(i+j+k+x+y)) == True:
                                if (i+j) not in temp_list:
                                    temp_list.append(i+j)
                            if prime(int(i)) == True:
                                if i != j:
                                    temp_list.append(i)
    elif len(numbers) == 6:
        for i in numbers:
            number = list(map(str, numbers))
            number.remove(i)
            for j in number:
                number.remove(j)
                for k in number:
                    number.remove(k)
                    for x in number:
                        number.remove(x)
                        for y in number:
                            number.remove(y)
                            for z in number:
                                if prime(int(i+j+k+x+y+z)) == True:
                                    if (i+j) not in temp_list:
                                        temp_list.append(i+j)
                                if prime(int(i)) == True:
                                    if i != j:
                                        temp_list.append(i)
    elif len(numbers) == 7:
        for i in numbers:
            number = list(map(str, numbers))
            number.remove(i)
            for j in number:
                number.remove(j)
                for k in number:
                    number.remove(k)
                    for x in number:
                        number.remove(x)
                        for y in number:
                            number.remove(y)
                            for z in number:
                                number.remove(z)
                                for u in number:
                                    if prime(int(i+j+k+x+y+z+u)) == True:
                                        if (i+j) not in temp_list:
                                            temp_list.append(i+j)
                                    if prime(int(i)) == True:
                                        if i != j:
                                            temp_list.append(i)
    answer = len(temp_list)
    return answer

numbers = "0135231"
print(solution(numbers))