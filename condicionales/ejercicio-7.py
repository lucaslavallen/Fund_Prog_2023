#  Deducir si un número leído (distinto de cero) es positivo o negativo

num1 = float(input("ingrese un numero: "))
cont = 0
negativo = 0
if num1 > 0:
    print("el numero es positivo")
elif num1 < 0:
    print("el numero es negativo")
else :
    print("el valor es cero, ¡ingrese un numero != 0 !")