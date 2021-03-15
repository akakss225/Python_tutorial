#def 함수명 (매개변수) :
#    <수행할 문장1>
#    <수행할 문장2>
#    ...
#    return 리턴 값

def sum(a, b):
    result = a + b
    return result
print(sum(1, 2))

#입력값이 없어도 출력값만을 나타낼 수 있음.
def say():
    return "Hi"

print(say())

#반대로 출력값이 없어도 나타낼 수 있음.
def sum2(a, b):
    print("%d, %d의 합은 %d입니다." %(a, b, a+b))
sum2(1, 2)
