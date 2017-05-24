# -*- coding: utf-8 -*-
"""
Created on Wed May 10 12:53:54 2017

@author: 22B
"""

##var = "hola como estas yo muy bien"

##print(var[:: -1])


vari =str(input("Ingrese frase a invertir: "))

vari2 = vari

## Para invertir la frase ingresada
print(str(vari[::-1]))


print("se ha registrado con exito revise el archivo 2")

def creartxt():
    archi=open("2.txt","w")
    archi.close()
    
def grabartxt():
    archi=open("2.txt","a")
    archi.write("Nombre: Ricardo Quinzo")
    archi.write("\n")
    archi.write("\n")
    archi.write('frase normal: ')
    archi.write(str(vari2))
    archi.write("\n")
    archi.write("\n")
    archi.write('Frase invertida: ')
    archi.write(str(vari[::-1]))
    archi.close()
    
creartxt()
grabartxt()
    