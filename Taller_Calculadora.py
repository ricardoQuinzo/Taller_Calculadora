from tkinter import *


def Suma():
    total = int(num1.get()) + int(num2.get())
    print(total)


    
    

tk=Tk()
ent1 = IntVar()
ent2 = IntVar()
num1 = Entry(tk, textvariable = ent1)
num2 = Entry(tk, textvariable = ent2)
num1.pack()
num2.pack()

suma= Button(tk, text="SUMA", command = Suma)
suma.pack()





