# 시퀀스

string = 'Hello World'
list = ['H','e','l','l','o','W','o','r','l','d']
tuple = ('H','e','l','l','o','W','o','r','l','d')

print(string)
print(list)
print(tuple)

print(string[0])
print(list[0])
print(tuple[0])

print(string[0:5])
print(list[0:5])
print(tuple[0:5])

for i in range(0, len(string)):
    if i < len(string)-1:
        print(string[i],end="")
    else:
        print(string[i])
for i in range(0, len(list)):
    if i < len(list)-1:
        print(list[i], end="")
    else:
        print(list[i])
for i in range(0, len(tuple)):
    if i < len(tuple)-1:
        print(tuple[i], end="")
    else:
        print(tuple[i])        

list2 = ['P','y','t','h','o','n']
print(list + list2)