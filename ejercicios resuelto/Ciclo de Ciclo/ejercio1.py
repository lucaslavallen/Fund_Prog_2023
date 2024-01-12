# 1 - Se tiene el monto disponible para abonar los sueldos de los empleados de una empresa, 
#   la propuesta es que el/la estudiante plantee el ejercicio
#   para abonar los sueldos hasta que no se disponga más de fondos. 
#   Incluya las modificaciones que crea necesarias para mostrar la cantidad de sueldos abonados. 
#   Determine además en el caso que posea fondos determinados por cada una de las tres sucursales de una empresa, 
#   ¿cómo diseñaría el algoritmo para que cumpla con el objetivo?

import os

os.system ('cls')

monto = float(input('Ingrese el monto inicial para abonar sueldos: $ '))
contador_total = 0

for i in range(3):
    print('¿Quiere ingresar un monto de sueldo para la sucursal', i + 1, '(S/N): ')
    opcion = input()

    cont = 0

    while opcion == 'S' or opcion == 's':
        sueldo = float(input("Ingrese sueldo: "))
        if monto > 0 and monto >= sueldo:
            monto -= sueldo
            cont += 1
        else:
            print('Monto insuficiente')
            print ('Tiene un saldo de $:',monto)

        print('¿Quiere ingresar otro? (S/N)')
        opcion = input()

    print ('Cantidad de sueldos pagados en sucursal',i+1,':',cont)
    contador_total += cont

print(f"Cantidad total de sueldos pagados: {contador_total}")
