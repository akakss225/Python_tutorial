from tkinter import *
from random import *

def roll():
    text.delete(0.0, END)
    text.insert(END, str(randint(1, 6)))

window = Tk()

text = Text(window, width=1, height=1)
buttionA = Button(window, text='주사위를 굴리려면 버튼을 누르세요', command=roll)
text.pack()
buttionA.pack()
