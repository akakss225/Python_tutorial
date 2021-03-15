a = 'Life is too short\nYou need Python'
b = """Life is too short
You need Python"""

x = "Python"
y = " is fun" 

z = "20010331Rainy"

print(a)    
print(b)
print(x+y)

print(a[0])
print(a[-2])
print(a[0:4])
##어떠한 변수 에 대괄호가 들어가고 ::로 나눠주는데,##
##이는 순서대로 이상 : 미만 : 간격 을 의미한다.##
##위의 [0:4]이면, 0번째부터 4번째 미만, 즉 3번째까지 출력하라를 의미##
print(z[:8])