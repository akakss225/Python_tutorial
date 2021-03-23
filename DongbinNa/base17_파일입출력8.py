with open('input.txt','r',encoding='UTF-8') as f:
    list = f.readlines()
    for i, data in enumerate(list):
        print('%d번째 줄 : %s' %(i+1 , data), end= "")

