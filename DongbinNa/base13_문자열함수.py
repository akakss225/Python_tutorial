# 문자열 자료형의 함수

# 문자열 자료형 뒤집기
str = 'Hello World'
print(str[::-1])

# len() : 문자열 길이를 출력
print(len(str))

# isalpha() : 특정한 문자열이 문자로만 이루어져 있는지 확인
print(str.isalpha()) # 공백이 들어가면 False.
str2 = '송수민'
print(str2.isalpha())

# isdigit() : 특정한 문자열이 숫자로만 이루어져 있는지 확인
print(str.isdigit()) # 공백이 들어가면 False.
str3 = '123123'
print(str3.isdigit())

# isalnum() = 특정한 문자열이 문자와 숫자로만 이루어져 있는지 확인
print(str.isalnum()) # 공백이 들어가면 False.
str4 = 'abc123'
print(str4.isalnum())

# join(리스트 자료형) : 여러개의 문자열을 구분자와 함께 합치는 함수.
list = ['Hello', 'World','홍길동']
print('_'.join(list))

# sorted() : 각 문자를 정렬
str5 = 'helloworld'
list2 = sorted(str5) # 리스트형태로 오름차순 출력
print(list2) 
print(''.join(list2))

# split(문자열 토큰) : 문자열을 토큰에 따라서 분리하는 함수
str6 = 'I wanna watch a movie'
list3 = str6.split(' ')
print(list3)

# find() : 문자열에서 찾고자하는 문자열의 인덱스 넘버를 출력
str7 = 'I like you'
print(str7.find('like')) #찾고자 하는 문자열이 존재하지않으면 -1출력
                         #또한 같은 문자열이 여러번 등장하면, 가장 먼저 발견한 값을 출력

# upper() / lower() : 문자열을 대문자 혹은 소문자로 반환
str8 = 'Hello World'
print(str8.upper())
print(str8.lower())

# strip() : 좌우로 특정한 문자열을 제거하는 함수
str9 = "  Hello World  "
str9_1 = 'tHello Worldt'
print(str9.strip()) # 기본적으로 아무값도 안들어가면 좌우 공백을 제거해줌
print(str9.lstrip()) # lstrip은 좌변의 공백을 제거
print(str9.rstrip()) # rstrip은 우변의 공백을 제거
print(str9_1.strip('t')) 

# eval() : 문자열 수식 계산함수.
exp = '(203 + 705)*3-(30/6)'
print(eval(exp))
