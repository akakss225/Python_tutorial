# 구구단 출력하기
# 함수이름 : Muliplication_table
# 변수이름 : number

def Muliplication_table():
    number = int(input())
    for i in range(1,10):
        print(number,'*',i,'=',number*i)

print(Muliplication_table())

        