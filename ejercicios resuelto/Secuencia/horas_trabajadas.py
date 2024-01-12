#3.	Dadas las horas trabajadas por un operario y el valor de las mismas, determinar que sueldo percibe dicho
#operario. Se solicita indicar cuanto cobraría si se aplican descuentos del 20%
horas=float(input("ingrese las horas trabajadas: "))
#horas*=100 está comentado
#print(horas)
valor=float(input("ingrese un valor de pago por hora: "))
sueldo=(horas*valor)-(horas*valor)*0.20
print(sueldo)