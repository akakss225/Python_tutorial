#함수 이름은 GuGu, 단수를 입력하면, 입력한 단수의 구구단이 출려된다.
#리스트를 사용하여 나타낸다.

num = int(input("정수를 입력해 주세요 : "))

def GuGu(n):
    result = []
    for i in range(1,10):
        result.append(n * i)
    return result

print(GuGu(num))

