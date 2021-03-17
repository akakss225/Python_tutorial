passward = "1q2w3e4r!"
pass_flag = False

for i in range(1,6):
    user_id = input("ID를 입력해 주세요 : ")
    user_passward = input("비밀번호를 입력해 주세요 : ")
    count = 5 - i

    if user_passward == passward:
        print("%s님 환영합니다!" % user_id)
        pass_flag = True
        break
    else:
        if count > 0:
            print("잘못된 비밀번호입니다.")
            print("%d번 틀렸습니다. %d번 남았습니다." %(i ,count))

if pass_flag == False:
    print("비정상적인 접근입니다.")