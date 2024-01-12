



# datos:
# nombre 
#numero de identificacion (ni)
#edad
#promedio de calidficaciones 
#carrera

import os
os.system('cls')

vector = [0,0,0,0]

def ingresar_estudiante():
    nombre = str(input("ingrese su nombre: "))
    numero_iden = int(input("ingrese numero de identificacion: "))
    edad = int(input("ingrese su edad: "))
    promedio = float(input("ingrese su promedio: "))
    carrera = str(input("ingrese su carrera: "))

    estudiante = {
        'nombre':nombre,
        'numero_iden':numero_iden,
        'edad':edad,
        'promedio':promedio,
        'carrera':carrera
    }
    return estudiante



# 1) registrar estudiantes
def cargar_estudiante(vector,lim):
    op = str(input("ingrese s para continuar: ")).upper()
    while (op == 'S') and lim < len(vector):
        nuevo_est = ingresar_estudiante()
        vector[lim] = nuevo_est
        lim +=1
        if op == 'S' and lim < len(vector):
            op = str(input("ingrese s para continuar: ")).upper()
    return lim



# 2) mostrar la lista de estudiantes 
def ordenamiento(limite,vector,campo1):
    for i in range(limite -1):
        for j in range(limite-1-i):
            actual = vector[j][campo1]
            siguiente = vector[j+1][campo1]
            if actual > siguiente:
                aux = vector[j]
                vector[j] = vector[j+1]
                vector[j+1] = aux


def mostrar_estudiante(vector,limite):
     for i in range (0,limite,1):
        per = vector[i]
        print("nombre", per['nombre'])
        print("numero_iden", per['numero_iden'])
        print("edad", per['edad'])
        print("promedio", per['promedio'])
        print("carrera", per['carrera'])
        print()
       
# busqueda binaria
def busqueda_binaria(vector, limite, buscado):
    pri = 0 
    ult = limite-1 
    pos = -1
    while (pos == -1) and (pri <= ult):
        med = (pri + ult) // 2
        if (vector[med]['numero_iden']) == buscado: 
            pos = med
        elif (vector[med]['numero_iden']) >= buscado: 
            ult = med - 1 
        else: 
            pri = med + 1
    return pos 

#no hice el 4to punto 


# Calcular y mostrar el promedio general de calificaciones para los estudiantes de la carrera Licenciatura en Sistemas de Información
def total(limite,vector):
    prom = 0
    for i in range(limite):
        prom += vector[i]['promedio']
    return (prom / limite)


# Calcular la cantidad de estudiantes mayores a 30 años que estudian Ingeniería en Telecomunicaciones

def mayores_30(vector,limite):
    acum = 0
    for i in range(limite):
        if vector[i]['edad'] > 30 and (vector[i]['carrera']) == "teleco":
            acum +=1
    return acum


lim = 0
limite = cargar_estudiante(vector,lim)
campo1 = 'nombre'
# metodo burbuja
print('ordenado alfabeticamente...')
ordenamiento(limite,vector,campo1)
# mostrar estudiantes
mostrar_estudiante(vector,limite)
# busqueda binario
print('ordenado por identificador de estudiantes...')
campo1 = 'numero_iden'
ordenamiento(limite,vector,campo1)
mostrar_estudiante(vector,limite)
buscado = int(input("ingrese identificacion del estudiantes: "))
x = busqueda_binaria(vector, limite, buscado)
if x != -1:
    print('se encuentra en ', x)
else:
    print('no esta en la lista')

#promedio de los alumnos de sistemas
print('promedio de estudiantes en general')
y = total(limite,vector)
print('promedio de los alumnos es: ',y)

# mayores de 30
print('cantidad de mayores que cursan teleco...')
mayo = mayores_30(vector,limite)
print('total de mayores de 30: ',mayo)
