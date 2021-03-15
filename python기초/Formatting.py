num = 10
day = "three"
name = '송수민'
a = "I ate %d apples. so I was sick for %s days." % (num, day)

b = "I ate {number} apples. so I was sick for {days} days. ".format(days='three',number=10)

c = f"나의 이름은 {name} 입니다."
print(a)
print(b)
print(c)