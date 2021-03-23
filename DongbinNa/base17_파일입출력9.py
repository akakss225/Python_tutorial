def process(filename):
    # with as 구문으로 close를 하지 않아도 자동적으로 열고 닫아주게 만들어줌
    # 즉, 현재 메소드가 실행되고, 끝날때 자동적으로 할당을 끝내줌.
    with open('new.txt', 'r') as f :
        dict = {}
        data = f.read()
       
        for i in data:
            # 이 경우, 모든 스펠링에 기본적으로 1이라는 값을 할당해 주고,
            # 반복이 된다면, +1을 시켜주는 조건문을 의미함.
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
    return dict

# 만든 dictionary에 메소드를 적용시킴
dict = process('new.txt')
# 이후 보기쉽게 빈도수의 크기에 따라 내림정렬을 해줌 리스트[(튜플형태)]
dict = sorted(dict.items(), key= lambda a : a[1], reverse= True)

for data, count in dict:
    if data == '\n' or data == " ":
        continue
    else:
        print('%d번 출현 :[%c]'%(count, data))



