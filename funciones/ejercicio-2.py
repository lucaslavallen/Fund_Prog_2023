# 2. Ídem para el perímetro.

def perimetro(num1, num2):
    peri = num1 * 2 + num2 * 2
    return peri

num1 = int(input("ingrese el lado1: "))
num2 = int(input("ingrese el lado2: "))

print(" el perimetro es: ", perimetro(num1, num2))