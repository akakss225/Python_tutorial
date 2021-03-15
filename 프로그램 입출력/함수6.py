#유효범위

a = 1
#함수 내부에서는 지역변수로써 사용된다.
def vartest(a):
    a += 1
    return a
#따라서 함수를 나오면, 영향력이 사라진다.
print(vartest(a))
print(a)