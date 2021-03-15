money = 2000
card = 1

if (money >= 3000) | card:
    print("택시를 타고 가라")
else :
    print("걸어가라")

if (money >= 3000) & card:
    print("택시를 타고 가라")
else :
    print("걸어가라")

if 1 in [1,2,3]: # 왼쪽의 값이 오른쪽에 존재하느냐? <<< in 사용
    print("택시를 타고 가라")
else :
    print("걸어가라")

if 1 not in [1,2,3]: # 왼쪽의 값이 오른쪼에 존재하지 않느냐? <<< not in 사용
    print("택시를 타고 가라")
else :
    print("걸어가라")
