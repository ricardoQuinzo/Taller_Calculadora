from tkinter import *


def Suma():
    total = int(num1.get()) + int(num2.get())
    print(total)

def Resta():
    total = int(num1.get()) - int(num2.get())
    print(total)

def Multiplicacion():
    total = int(num1.get()) * int(num2.get())
    print(total)

def Division():
    if int(num2.get()) == 0:
         print("error")
    else:
        total = total = int(num1.get()) / int(num2.get())
        print(total)
 
    
tk=Tk()
##definicion de variables a ingresar
ent1 = IntVar()
ent2 = IntVar()
num1 = Entry(tk, textvariable = ent1)
num2 = Entry(tk, textvariable = ent2)
num1.pack()
num2.pack()

suma = Button(tk, text="SUMA", command = Suma)
resta = Button(tk, text="RESTA", command = Resta)
multi= Button(tk, text="MULTIPLICACION", command = Multiplicacion)
division = Button(tk, text="DIVISION", command = Division)

suma.pack()
resta.pack()
multi.pack()
division.pack()




