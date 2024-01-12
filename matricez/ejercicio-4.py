# Dada una matriz rectangular realizar un programa que devuelva el mayor de los elementos 
# contenidos en ella, considerando solamente aquellos en los cuales la suma de sus subíndices es
# par. Es decir [1,1], [1,3], [1,5] [2,2], etc.

import os
os.system('cls')

matriz = [[0,0], [0,0]]

maximo = matriz [0][0]

def cargar(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
             matriz[i][j]= int(input('ingrese el elemento: '))



def sumar(matriz):
    ac = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if (i + j) % 2 == 0:
                if matriz[i][j] > ac:
                    ac = matriz[i][j]
    print(f'el numero mayor es: {ac}')



cargar(matriz)
sumar(matriz)

