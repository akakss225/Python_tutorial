f = open('input.txt','r',encoding='UTF-8')

f.seek(9)
data = f.read()
print(data)
f.close()
