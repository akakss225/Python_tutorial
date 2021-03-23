f = open('new.txt', 'w')

f.close()

A = open('new.txt', 'a')

data = 'Life is too short\nYou need Python\nAnd that is the reason why I study the Python'

A.write(data)

A.close()
