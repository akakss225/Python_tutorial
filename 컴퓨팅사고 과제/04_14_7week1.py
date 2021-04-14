# Module
# 일종의 부품.

# ex) math : fabs()절댓값 / ceil()올림 / floor()내림 / trunc()버림 / gcd()최대공약 / factiorial() / sqrt()제곱근

import turtle as t
import math
'''
print(math.ceil(3.1))
print(math.floor(3.9))
print(math.sqrt(2.9))
print(math.pi)
'''
'''
colors = ['red', 'purple', 'blue', 'green', 'yellow' , 'orange']

t.bgcolor('black')
t.speed(0)
t.width(3)
length = 10
while length < 400:
    t.forward(length)
    t.pencolor(colors[length%6])
    t.right(89)
    length += 5
'''
t.shape('turtle')
t.bgcolor('black')
t.color('green')
t.speed(0)

n = 50
for x in range(n):
    t.circle(100)
    t.left(360/n)