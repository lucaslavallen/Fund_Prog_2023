# . Escribir una función que tenga un parámetro de tipo entero y que devuelva la letra P si el 
# Nº es positivo y N si es negativo o cero

def posOneg(num1):
    if num1 > 0:
        print("P")
    elif num1 <= 0:
        print("N")

num1 = int(input("ingrese un numero: "))

posOneg(num1)