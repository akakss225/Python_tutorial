# 연산
print(5 + 2)
print(5 - 2)
print(5 * 2)
print(5 / 2)
print(5 ** 2)
print(5 // 2)
print(5 % 2)
print(5 - (2 + 1))

print()
# 논리
print(3 == 3)
print(3 != 3)
print(3 < 5)
print(3 > 5)
print(3 <= 3)
print(3 >= 3)

print()
# 반복
for i in range(5):
    print(i)

i = 0
while i < 5:
    print(i)
    i += 1
list = ['가','나','다','라','마']

for i in list:
    print(i)
print()
# 함수
def hello():
    print('안녕')

hello()

print()
# 진수변환
# 암기하자
###########
value = 60 ####
b = bin(value) # 2진수
o = oct(value) # 8진수
h = hex(value) # 16진수
print(b,o,h) #############
print(format(value,'#b')) #
print(format(value,'#o')) #
print(format(value,'#x')) #
##########################

print()
# 반복문을 이용한 팩토리얼 구현

num = 8
factorial = 1
while num != 1:
    factorial *= num
    num -= 1
print(factorial)

result = 1
for i in range(1,9):
    result *= i
print(result)

# 재귀함수를 이용한 팩토리얼 구현
def _factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * _factorial(num-1)

print(_factorial(8))

print()
def circle_area(r):
    return 3.14 * r ** 2

print(circle_area(4))

print()
def sum(start, end):
    result = 0
    for i in range(start, end+1):
        result += i
    return result
print(sum(1,10))

print()
'''
menu = []
for i in range(3):
    menu.append(input('메뉴를 선택해주세요 :'))
    print('주문내역 :',menu[i])
print(','.join(menu),'주문 완료되었습니다.')

print()
'''

