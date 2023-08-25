
# Escribir un procedimiento que calcule el factorial de un Nº entero usando parámetro valor 
# y variable.
import os
os.system('cls')
  
def factorial(num1):
    fact = 1
    for i in range(1, num1+1):
        fact = fact * i
        
    return fact

num1 = int(input("ingrese numero: "))

print("el factorial de ", factorial(num1))        
      