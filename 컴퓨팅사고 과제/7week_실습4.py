import turtle as t

t_color = 'yellow'
t_bgcolor = 'black'
t_shape = 'turtle'
t_speed = 8

t.shape(t_shape)
t.color(t_color)
t.bgcolor(t_bgcolor)
t.speed(t_speed)

for i in range(9):
    t.forward(50)
    t.right(160)
    t.forward(50)
    t.left(80)

t.done()