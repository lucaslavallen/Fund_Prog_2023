# Escribir una función lógica de dos parámetros enteros que devuelva True si uno divide al 
# otro y False en caso contrario

def divide(num1, num2):
    if num1 % num2 == 0:
     print("True")
    else:
       print("False")
       

num1 = int(input("ingrese numero 1: "))
num2 = int(input("ingrese numero 2: "))

divide(num1, num2)