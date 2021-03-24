oder = [0,0,0]

for i in range(0,4):
    if i < 3:
        oder[i] = input('주문하고 싶은 음식을 입력하세요')
        print('주문내역:',oder[i])
    else:
        print(",".join(oder),'주문 되었습니다.')
    
