f = open('input.txt', 'r', encoding='UTF-8')

count = 0
while count < 3 :
    data = f.readline()
    count += 1
    print('%d번째 줄 : %s' %(count, data))

list = f.readlines()
print(list)
f.close()
