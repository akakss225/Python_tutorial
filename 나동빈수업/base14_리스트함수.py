# 인스턴스.index(원소) : 리스트 내 특정한 원소의 인덱스를 찾기
list1 = ['나동빈', '강중구', '이태일', '박한울', '이상욱']
print(list1.index('이태일'))
#print(list.index('송수민'))

# 인스턴스.reverse() : 리스트의 원소를 뒤집기
list2 = [1, 2, 3]
list2.reverse()
print(list2) # = print(list[::-1])

# sum(리스트 자료형) : 리스트의 모든 원소의 합 출력
print(sum(list2))

# range() : 특정 범위 지정
# list(범위) : 특정 범위의 원소를 가지는 리스트를 반환
my_range = range(5, 10)
print(my_range)
#list = list(my_range)
#print(list)

# all(인스턴스) / any(인스턴스) : 리스트의 모든 원소가 참인지 판별 / 하나라도 참인지 확인

list3 = [False, True, False, False]
print(all(list3))
print(any(list3))

# enumerate(인스턴스) : 리스트에서 인덱스와 원소를 함께 추출
my_list = ['홍길동', '허준', '콩쥐', '팥쥐', '신데렐라']
print(enumerate(my_list)) # 오브젝트를 만들었다는 의미. 출력하기 위해선 아래처럼.
result = list(enumerate(my_list)) # 튜플 형태로 인덱스와 값으로 나눠서 나옴.
print(result)

for i, k in enumerate(my_list):
    print('[인덱스 :',  i,'] 이름 :',k)

# 인스턴스.sort() : 리스트의 원소를 정렬
my_list.sort()
print(my_list)

# 인스턴스.count() : 특정한 원소의 갯수를 추출
print(my_list.count('신데렐라'))

# del : 리스트의 특정 원소를 제거(인덱스)
list4 = [123,456,789,0]
print(list4)
del list4[1]
print(list4)

# insert(인덱스, 원소) : 리스트에 특정 원소를 삽입
list5 = [1,2,3,4,5]
print(list5)
list5.insert(5, 6)
print(list5)
list5.insert(0, 0)
print(list5)

# append() : 리스트 가장 마지막에 원소를 추가
list6 = [1,2,3,4,5,6,7]
print(list6)
list6.append(8)
print(list6)