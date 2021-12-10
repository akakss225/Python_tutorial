a = "Life is too short, You need Python"

print(a[0:4])

b = "20211210Rainy"
c = 12345
print("I eat %d apples" % 3)
print("I eat %s apples" % "five")
print("I eat {0} apples".format(3))
print("I ate {0} apples. so I was sick for {1} days.".format(5, "three"))

def isStr(a):
    return " ".join(a)

q = ["Life", "is", "too", "short", "you", "need", "python"]
print(isStr(q))

print("{0:<10}".format("hi"))
print("{0:>10}".format("hi"))
print("{0:^10}".format("hi"))
print("{0:=^10}".format("hi"))

print("hobby".count("b"))

print("Python is the best choice".find("b"))
print("Python is the best choice".find("k"))

print("{0:^10}".format("hi").rstrip() + "python")

print(a.split())

print([1,2] + [3,4,5])

p = [1,2,3,4,5]
p.remove(3)
print(p)
print(sorted(p, reverse=True))
print(p)
p.insert(2,3)
print(p)
p.reverse()
print(p)


dic = {"name" : "pey" , "phone" : "0119993323", "birth" : "1118"}

print(dic["name"], dic["phone"], dic["birth"])


money = True
if money:
    print("take a taxi")
else:
    print("walk")

pocket = ['paper', 'cellphone']
card = True
if "money" in pocket:
    print("take a taxi")
elif card:
    print("take a taxi")
else:
    print("walk")

num_list = ["one", "two", "three"]
for i in num_list:
    print(i, end=" ")


print()


num_tuple = [(1, 2), (3, 4), (5, 6)]
for i,j in num_tuple:
    print(i + j)

def add(a,b):
    return a+b
print(add(1,2))

def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result
print(add_many(1,2,3,4,5,6,7,8,9,10))

add2 = lambda a, b : a+b

print(add2(3,4))



