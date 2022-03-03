# 조건
# 입력으로는 str1과 str2의 두 문자열이 들어온다. 
# 각 문자열의 길이는 2 이상, 1,000 이하이다.
# 입력으로 들어온 문자열은 두 글자씩 끊어서 다중집합의 원소로 만든다. 
# 이때 영문자로 된 글자 쌍만 유효하고, 기타 공백이나 숫자, 특수 문자가 들어있는 경우는 그 글자 쌍을 버린다. 
# 예를 들어 "ab+"가 입력으로 들어오면, "ab"만 다중집합의 원소로 삼고, "b+"는 버린다.
# 다중집합 원소 사이를 비교할 때, 대문자와 소문자의 차이는 무시한다. 
# "AB"와 "Ab", "ab"는 같은 원소로 취급한다.
# 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력한다.



# IDEA
# 1. 두 문자열 str1 / str2 에 대하여, 각각 2문자씩 끊어서 dict1 / dict2 만듬
# 2. 만약, 두 문자씩 쪼갠것 중에 영문자가 아닌것이 있으면, 없앤다.
# 3. dict의 key는 각각의 word이고, value는 나온 횟수이다.
# 4. dict1을 돌며, 겹치는게 있으면, 교집합에는 min(dict1, dict2) 을 더해준다.
# 5. dict1을 돌며, 겹치는게 있으면, 합집합에는 max(dict1, dict2) 를 더해주고, 겹치지 않는것도 더해준다.
# 6. dict2를 돌며, 겹치지 않는것만 합집합에 더해준다.
# 7. 수식 사용.


from curses.ascii import isalpha

def solution(str1, str2):
    dict1 = dict()
    dict2 = dict()
    
    # 합집합
    uni = 0
    # 교집합
    inter = 0
    
    for i in range(len(str1)-1):
        word1 = str1[i]
        word2 = str1[i+1]
        if isalpha(word1) and isalpha(word2):
            word = word1.upper() + word2.upper()
            if word in dict1:
                dict1[word] += 1
            else:
                dict1[word] = 1
    
    for i in range(len(str2)-1):
        word1 = str2[i]
        word2 = str2[i+1]
        if isalpha(word1) and isalpha(word2):
            word = word1.upper() + word2.upper()
            if word in dict2:
                dict2[word] += 1
            else:
                dict2[word] = 1
    
    for i in dict1:
        if i in dict2:
            inter += min(dict1[i], dict2[i])
            uni += max(dict1[i], dict2[i])
        else:
            uni += dict1[i]
    for i in dict2:
        if i in dict1:
            continue
        else:
            uni += dict2[i]
    
    if uni == 0 and inter == 0:
        return 65536
    return int(float(inter/uni*65536))

str1 = "FRANCE"
str2 = "french"

print(solution(str1, str2))