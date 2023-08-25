# Escribir un procedimiento de Geometría tal que dado el alto y ancho de un rectángulo calcule 
# el área
 

def geometria(num1, num2):
    area = num1 * num2
    return (area)


num1 = int(input("ingrese el alto: "))
num2 = int(input("ingrese el ancho: "))

print(" el rectangulo es: ", geometria(num1, num2))
