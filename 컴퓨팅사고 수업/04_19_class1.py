def typeofInt(a):
    if a == 0:
        print('0입니다.')
    
    elif a < 0:
        print('음의 정수입니다.')
    
    else:
        print('양의 정수입니다.')
        
def factorial(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * factorial(a-1)

def calc_area(a):
    area = 3.14 * a**2
    return area

def get_sum(start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += i
    return sum


    
#typeofInt(3)
#typeofInt(0)
#typeofInt(-3)

'''
score = int(input('Write your score '))

if score == 100:
    print('A+')
elif score >= 90:
    print('A')
elif score >= 80:
    print('B+')
elif score >= 70:
    print('B')
elif score >= 60:
    print('C+')
elif score >= 50:
    print('C')
else:
    print('F')
'''

'''
x = int(input('구구단 몇단인가요?'))

for i in range(1,10):
    print(x,'*', i,'=',x*i)
'''

'''
i = 1
while i <= 10:
    print(i)
    i += 1
print('끝')
'''

'''
print(factorial(4))
'''

'''
List = ['인하', '대학교', '14학번', '송수민']

for i in List:
    print(i,end='')
    
print(List[0:2])
'''

#print(calc_area(3))

#print(get_sum(1,10))