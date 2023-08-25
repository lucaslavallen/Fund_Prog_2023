# Escribir una función lógica tal que dadas dos cadenas indique si la primera es más larga 
#  que la segunda

def contador(cadena1, cadena2):

    if cadena1 > cadena2:
        print("cadena 1 es mas larga")
    else:
        print("cadena 2 es mas larga")
        
    


cadena1 = str(input("ingrese cadena 1: "))
cadena2 = str(input("ingrese cadena 2: "))


contador(cadena1, cadena2)