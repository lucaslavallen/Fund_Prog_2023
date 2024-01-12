# 1 se tiene una lista con los barrios de una ciudad. de cada uno se tiene:
# - nombre 
# - si tiene servicios de claocas [si/no]
# - cantiad de habitantes por familias 

# se pide:

# B-determinar si el barrio san sebastian esta cargado en la lista
# c-porcenetaje que representa la cantidad de familias del barrio san sebastian sobre el total de familias que habitan en todos los barrios
# e-cantidad de barrios sin servicios de cloacas
# f-promedio de familas por barrio

# 2-se tiene una matriz cuadrda cargada con numeros,determinar y mostrar la cantidad de numeros pares que se encuentren en la diagonal principal,.

import os
os.system('cls')
ciudad = [0,0,0,0,0,0,0]

def ingrese_barrio():
    nombre = str((input("ingresar nombre de barrio: ")))
    servicio_cloacas = str((input("ingrese si tiene servicios [Si/No]: ")))
    cantidad_habitantes = float(input("ingrese cantidad de habitantes x familias: "))


    barrio = {
        'nombre':nombre,
        'servicio_cloacas':servicio_cloacas,
        'cantidad_habitantes':cantidad_habitantes
    }
    return barrio


def cargar_barrio(lim, ciudad):
    opcion = str(input("Ingrese s para cargae un barrio:  ")).upper()
    while (opcion =='S' and lim<(len(ciudad))):
        nuevo_barrio = ingrese_barrio()
        ciudad[lim]=nuevo_barrio
        lim +=1
        print()
        if lim<(len(ciudad)):
            opcion= str(input("Ingrese s para cargae un barrio:  ")).upper()
    return lim

# A-listado ordenado por barrio
def burbuja(ciudad, limite,campo1,campo2):
    for i in range(limite - 1):
        for j in range(limite - 1 - i):
            actual = ciudad[j][campo1] + ' ' + ciudad[j][campo2]
            siguiente = ciudad[j+1][campo1] + ciudad[j+1][campo2]
            if actual > siguiente:
                aux = ciudad[j]
                ciudad[j]=ciudad[j+1]
                ciudad[j+1]=aux
                

def mostrar_barrios(ciudad,limite):
    for i in range (0,limite,1):
        barrios = ciudad[i]
        print("nombre", barrios['nombre'])
        print("cloacas", barrios['servicio_cloacas'])
        print("cantidad_habitantes", barrios['cantidad_habitantes'])
        print()
   

# B-determinar si el barrio san sebastian esta cargado en la lista
def ordenamiento(limite,ciudad,buscado):
    pri = 0
    ult = limite - 1
    pos = -1
    while (pos == -1) and (pri <= ult):
        med = (pri + ult) // 2
        if ciudad[med]['nombre'] == buscado:
            pos = med
        elif ciudad[med]['nombre'] >= buscado:
            ult = med - 1
        else:
            pri = med + 1
    return pos

# c-porcenetaje que representa la cantidad de familias del barrio san sebastian sobre el total de familias que habitan en todos los barrios
def total(limite,ciudad):
    total_familias=0
    for i in range(limite):
       total_familias += ciudad[i]['cantidad_habitantes']
    return total_familias


def subtotal(limite,ciudad):
    sub = 0
    for i in range(limite):
        if ciudad[i]['nombre'] == buscado:
            sub += ciudad[i]['cantidad_habitantes']
    return sub
    

def porcentaje(y,z):
    porc = (z*100)//y
    return porc

# f-promedio de familas por barrio
def promedio(limite,y):
    prom = y/limite
    print(prom,'%')
    return prom

# e-cantidad de barrios sin servicios de cloacas
def cloacas(limite,ciudad):
    sin_servicios = 0
    for i in range(limite):
        if ciudad[i]['servicio_cloacas'] == "no":
            sin_servicios +=1
    return sin_servicios



lim = 0
limite = cargar_barrio(lim, ciudad)
campo1 = 'nombre'
campo2 = 'servicio_cloacas'
burbuja(ciudad,limite,campo1,campo2)
mostrar_barrios(ciudad,limite)
buscado = str(input("ingrese barrio a buscar: "))
x = ordenamiento(limite,ciudad,buscado)
if x!=-1: print('el barrio buscado esta: ', x)
else: print('el barrio no esta cargado')
print()
y = total(limite,ciudad)
print(y)
z = subtotal(limite,ciudad)
print(z)
porcen = porcentaje(y,z)
print(porcen,'%')
promedio(limite,y)
print(cloacas(limite,ciudad))