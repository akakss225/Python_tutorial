f = open('input.txt','r',encoding='UTF-8')

list = f.readlines()
print(list)

for i, data in enumerate(list):
    print("%d번째 줄 : %s" %(i + 1, data), end='')

f.close()

