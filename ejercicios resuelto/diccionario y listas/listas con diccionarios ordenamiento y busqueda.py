personas=[0,0,0,0]

#Definir una función para ingresar datos de una perrsona en un diccionarios
def Ingresar_persona():
    nombre=input("Ingrese el nombre de la persona: ")
    apellido=input("Ingrese el apellido de la persona: ")
    edad=int(input("Ingrese la edad de la persona: "))
    peso=float(input("Ingrese el peso de la persona: "))

    persona={
        'nombre':nombre,
        'apellido':apellido,
        'edad':edad,
        'peso':peso,

    }
    return persona

#Cargar con con ciclo mientras 
def Cargar_personas(lim, personas):
    opcion=input("Ingrese s para cargar una persona:  ")
    while (opcion=='s' and lim<(len(personas))):
        nueva_persona=Ingresar_persona()
        personas[lim]=nueva_persona
        lim+=1
        print()
        if lim<(len(personas)):
            opcion=input("Ingrese s para cargar una persona:  ")
    return lim


def Mostrar_personas(personas, limite):
   for i in range(0, limite, 1):
       per = personas[i]
       print('ubicación',i)
       print("Nombre:", per['nombre'])
       print("Apellido:", per['apellido'])
       print("Edad:", per['edad'])
       print("Peso:", per['peso'])
       print()


def Mas_60_anios(personas, limite):
    total60 = 0
    for i in range (0, limite, 1):
        if personas[i]['edad']>60:
            total60+=1
    return total60


def Porcentaje_50kg(personas, limite):
    porc = 0
    total=0
    for i in range (0, limite, 1):
        if personas[i]['peso']<50:
            total+=1
    porc=(total*100)/(limite)
    return porc

#Ordenamiento Burbuja por mas de un campo
def burbuja(personas, limite):
    for i in range(limite - 1):
        for j in range(limite - 1 - i):
            nombre_apellido_actual = personas[j]['apellido'] + personas[j]['nombre']
            nombre_apellido_siguiente = personas[j + 1]['apellido'] + personas[j + 1]['nombre']
            if nombre_apellido_actual > nombre_apellido_siguiente:
                aux = personas[j]
                personas[j] = personas[j + 1]
                personas[j + 1] = aux


def busqueda_binaria(personas, limite, buscado):
    pri = 0
    ult = limite - 1
    pos = -1
    while (pos == -1) and (pri <= ult):
        med = (pri + ult) // 2
        if personas[med]['apellido'] == buscado:
            pos = med
        elif personas[med]['apellido'] >= buscado:
            ult = med - 1
        else:
            pri = med + 1
    return pos


lim=0
limite=Cargar_personas(lim, personas)
print()
print('la cantidad de personas cargadas son:', limite)
print()
Mostrar_personas(personas, limite)
print()
print('la cantidad de personas mayores a 60 años son: ',Mas_60_anios(personas, limite))
print()
print('El porcentaje de personas con peso menor a 50Kg es:',Porcentaje_50kg(personas, limite))
print()
print('la cantidad de personas cargadas son:', limite)
print()

burbuja(personas, limite)
Mostrar_personas(personas, limite)
buscado=input('ingrese el apellido a buscar: ')  
x=busqueda_binaria(personas, limite, buscado)

if x!=-1: print('el buscado está en: ', x)
else: print('el buscado no está en la lista')
print()