# Dado el número matemático PI, se solicita al usuario que ingrese el valor del radio de una 
# circunferencia y calcule y muestre por pantalla el área y perímetro. (área = PI * radio2
# perímetro = 2 * PI * radio
import math

math.pi

radio = float(input("ingrese valor del radio: "))

area = (math.pi * radio**2)

permietro = (2 * math.pi * radio)

print("el area es: ", area)

print("perimetro es: ", permietro)