import turtle as t


'''
t.shape('turtle')
for i in range(4):
    t.forward(100)
    t.left(90)
'''

'''
t.shape('turtle')
t.color('red')
t.fillcolor('blue') # 1.색칠할 색을 고름
t.begin_fill() # 2.색칠할 준비 
t.circle(100) # 3.원을 먼저그림
t.end_fill() # 4.색칠후 종료
'''

'''
t.shape('turtle')
t.color('red')
t.fillcolor('yellow')
t.begin_fill()
t.circle(100)
t.end_fill()

t.forward(100)
t.color('yellow')
t.fillcolor('blue')
t.begin_fill()
t.circle(100)
t.end_fill()

t.forward(100)
t.color('blue')
t.fillcolor('red')
t.begin_fill()
t.circle(100)
t.end_fill()
'''

'''
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
'''

'''
n = 60
t.shape('turtle')
t.bgcolor('black')
t.pencolor('green')
t.speed(0)

for i in range(n):
    t.circle(100)
    t.right(360 / n)
t.done()
'''

t.shape('turtle')
t.speed(0)
for i in range(400):
    t.forward(i)
    t.right(91)
t.done()
