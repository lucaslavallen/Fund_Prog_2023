# Hacer un algoritmo que:
# - Lea una lista de números de teclado que culmina con uno negativo.
# - Los ordene en forma creciente y Visualice la lista ordenada.
# - Buscar si existe el Nº 27 en la lista.

import os 

os.system('cls')

vector = [0,0,0,0,0]


def cargar(lim):
  num = int(input("ingrese un numero: "))
  while (num != -1) and lim < len(vector):
    vector [lim] = num
    lim +=1
    num = int(input("vuelva a ingresar un numero: "))
  return (lim)


def burbuja(vector):
    for i in range(0,(len(vector)-1)-1):
        for j in range(0,len(vector)-1-i):
            if vector[j]>vector[j+1]:
                aux=vector[j]
                vector[j]=vector[j+1]
                vector[j+1]=aux



def busqueda(vector,lim, buscado, pos):
    pri=0
    ult=len(vector)-1
    while (pos==0) and (pri<=ult):
        med=(pri+ult)//2
        if vector[med]==buscado:
            pos=med
        elif vector[med]>=buscado:
            ult=med-1
        else:
            pri=med+1   
    return(pos)

def mostrar_vector(vector):
    print(vector)

buscado=27
lim = 0
cargar(lim)
pos=0
mostrar_vector(vector)
burbuja(vector)  
mostrar_vector(vector)
x=busqueda(vector,lim, buscado, pos)
if x!=0: print('el buscado está en: ', x)
else: print('el buscado no está en la lista')







