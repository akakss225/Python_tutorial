# turtle 별그리기 
# 반복문 o 변수 o

import turtle as t

t_color = 'yellow'
t_bgcolor = 'black'
t_shape = 'turtle'
t_speed = 8

t.shape(t_shape)
t.color(t_color)
t.bgcolor(t_bgcolor)
t.speed(t_speed)

t.begin_fill()
for i in range(6):
    t.forward(10)
    t.right(120)
    t.forward(10)
    t.left(60)
t.end_fill()
t.done()