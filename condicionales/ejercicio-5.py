 # Ingresar un par de valores, emitirlos, y si ambos son positivos, emitir también su promedio

n = 0
c = 0
suma = 0

while n >= 0:
    n = int(input("ingrese un numero: "))
    if n > 0:
     c += 1
     suma = suma + n

print("el total de numeros positivos es: ",c)
print("su promedio es:",suma/c)

# se puede hacer sin el while