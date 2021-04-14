# turtle 별그리기 
# 반복문 o 변수 x

import turtle as t

t.shape('turtle')
t.color('yellow')
t.bgcolor('black')
t.speed(8)

t.begin_fill()
for i in range(6):
    t.forward(10)
    t.right(120)
    t.forward(10)
    t.left(60)
t.end_fill()
t.done()
