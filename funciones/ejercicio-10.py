# Escribir un procedimiento digito, que determine si un carácter es uno de los dígitos de 0 a 
# 9.

def digito(num):
    if num >=0 and num <= 9:
        print("usted ingreso un numero de 0 al 9")
    else:
        print("usted eligio otro digito")

num = int(input("ingrese un valor"))

digito(num)