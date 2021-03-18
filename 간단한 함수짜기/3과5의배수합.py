#1000미만의 자연수를 입력받으면,
#그 입력받은 수보다 작은 3과 5의 배수의 총 합을 구한다.

num = int(input("1000 미만의 자연수를 입력해주세요 : "))

def sum(n):
    three = 0
    five = 0
    
    for i in range(1, n):
        if i*3 >= n :
            break
        else:
            three = three + i*3
    
    for i in range(1, n):
        if i*5 >= n:
            break
        else:
            five = five + i*5
        
    return three + five

print(sum(num))


    
