#유효범위

a = 1
#함수 내부에서는 지역변수로써 사용된다.
def vartest(a):
    a += 1
    return a
#따라서 함수를 나오면, 영향력이 사라진다.
print(vartest(a))
print(a)
#영향을 주기 위해서는 
# a = vartest(a)를 함수밖에 써주어 a에 할당해주면 된다.

#혹은 함수를 짤 때 변수 a를 지역변수가 아닌 전역변수로써 설정한다
#def vartest():
#    global a
#    a += 1