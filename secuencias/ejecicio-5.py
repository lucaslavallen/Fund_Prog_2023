#  Hallar el área de un cuadrado, cuyos lados tienen la longitud de la hipotenusa de un 
# triángulo rectángulo y cuyos catetos son dados.

# Area de un cuadrado

import math 

ladoA = float(input("ingrese lado A: "))

ladoB = float(input("ingrese lado B:"))

area = (ladoA*ladoB)

print("el area de un cuadrado es:", area)


# Area de un triangulo rectangulo

base = float(input("ingrese base: "))

altura = float(input("ingrese altura: "))

areaT = (base*altura)/2

print("el area de un triangulo rectangulo es: ", areaT)