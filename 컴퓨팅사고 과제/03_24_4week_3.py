f = open('new.txt','r')

data = f.read()
data2 = f.readlines()
print(data)
print(data2)
f.close()