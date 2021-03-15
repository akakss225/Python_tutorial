#기본값 설정도 가능하다 << 출력할 때 생략 가능.
def say_myself(name, age, man=True):
    print("나의 이름은 %s입니다." %name)
    print("나의 나이는 %d입니다."%age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("송수민", 27)
say_myself("홍길동", 27,False)
