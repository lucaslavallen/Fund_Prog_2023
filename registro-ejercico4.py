
# En un edificio se administran sesenta departamentos (6 por piso); con el fin de cobrar a cada dueño 
# la cuota de gastos correspondiente al último mes. Se registran los gastos de: energía eléctrica, gas, 
# guardias, lavandería y conserjería de cada departamento.
# Crear la estructura que lo almacene, el proceso de carga y emitir al final un listado con los 
# importes que por cada concepto debe pagar cada propietario, además utilizar un vector 
# auxiliar para cargar el importe total que se debe pagar por departamento.
import os
os.system('cls')

def edificios():
    energia_electric = float(input("ingrese costo de electricidad: ")) #valor de la electricidad
    gas = float(input("ingrese gasto de gas:"))
    guardia = float(input("ingrese gastos de seguridad: "))
    lavanderia = float(input("ingrese gasto de lavanderia: "))
    consej_depto = float(input("ingrese gasto de consejeria de depto: "))

    gastos = {
        'energia': energia_electric,
        'gas': gas,
        'guardia':guardia,
        'lavanderia':lavanderia,
        'consejo-depto': consej_depto
    }
    return gastos




def Mostrar_personas(limite):
   for i in range(0,61):
       A = limite
       print("luz:", A['energia'])
       print("gas:", A['gas'])
       print("guardia:", A['guardia'])
       print("lavanderia:", A['lavanderia'])
       print("consejero:", A['consejo-depto'])
       print()


 


limite = edificios()
Mostrar_personas(limite)
