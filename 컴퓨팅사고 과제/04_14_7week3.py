from tkinter import *

def bAction():
    print('고맙습니다')
def bBaction():
    print('아얏, 아파요')


window = Tk()

buttonA = Button(window, text='누르세요', command = bAction)
buttonB = Button(window, text='누르지마세요', command = bBaction)

buttonA.pack()
buttonB.pack()
