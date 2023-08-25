# Diseñar una función que calcule potencias de forma xn y un programa que haga uso de la 
# misma, para distintos valores de x y n.
 
def potencia(num, exp):
    resultado = num**exp
    return resultado

num = int(input("ingrese un numero: "))
exp = int(input("ingrese exponente: "))

print("el resultado es: ", potencia(num, exp))