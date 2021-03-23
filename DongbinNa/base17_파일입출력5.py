f = open('input.txt','r',encoding='UTF-8')

data = f.read()

print(list(data))
print(type(data))

f.close()
