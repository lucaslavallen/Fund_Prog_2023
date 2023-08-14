#4. Ídem anterior, pero considerando que se le debe aplicar los descuentos correspondientes 
# por ley, los mismos son del 20%. Mostrar el sueldo a cobrar.

horas = float(input("ingresar las horas trabajadas "))

valor= float(input("ingrese el valor de la hora "))

sueldo = (horas*valor)

print("tu salario es ", sueldo)-((horas*valor)*0.20) 