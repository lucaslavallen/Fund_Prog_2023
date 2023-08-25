# Escribir una función par tal que indique si un número es par o impar

def parOimpar(num):
    if num % 2 == 0:
        print("el nuemro es par")
    else:
        print("el numero es impar")

num = int(input("ingrese un numero: "))

parOimpar(num)