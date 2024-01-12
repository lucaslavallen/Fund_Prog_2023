# Leer un vector de 10 elementos reales y emitir las siguientes leyendas según, 
# corresponda: “El vector tiene todas sus componentes positivas”, “El vector tiene 
# componentes negativas”, “El vector tiene algún cero”.

import os

os.system('cls')

vector = [0,0,0,0,0]

def leer(vector):
    for i in range (0,len(vector)):
        num = int(input("escribe un numero del 1 al 10: "))
    
    if num > 0:
        print("El vector tiene todas sus componentes positivas")
    elif num < 0:
        print("El vector tiene componentes negativas")
    if num == 0:
        print("tiene algun cero")

leer(vector)