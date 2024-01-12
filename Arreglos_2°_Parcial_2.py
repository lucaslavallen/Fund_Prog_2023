# Examen tipo segundo parcial
# Se tiene una lista de los inscriptos a un concurso de canto. 
# De cada uno se tiene: apellido y nombre, edad, canción que interpretará y autor de la misma.
# Se pide:
# A – Definir la estructura necesaria para representar el problema y cargarla con los datos de cada concursante.
# B - Calcular promedio de edad de los concursantes.
# C - Crear una lista con los concursantes menores de 18 años.
# D - Listado ordenado por apellido y nombre de todos los concursantes.
# E – Determinar si existe al menos una canción cuya autora es Adele.
# F - Listado ordenado por autores de las canciones que se interpretarán.
# G - Determinar porcentaje de menores a 18 años sobre el total.
# ---------------------------------------------------------------------------------------------------------------

# Punto A
personas=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def Ingresar_persona():
    nombre=input("Ingrese el nombre de la persona: ").upper() #.upper() pasa todo el texto a mayuscula
    apellido=input("Ingrese el apellido de la persona: ").upper()
    edad=int(input("Ingrese la edad de la persona: "))
    cancion=(input("Ingrese la canción a interpretar: ")).upper()
    autor=input("Ingrese el autor de la canción: ").upper()
    
    persona={
        'nombre':nombre,
        'apellido':apellido,
        'edad':edad,
        'cancion':cancion,
        'autor':autor
    }
    return persona

def Cargar_personas(personas, lim):
    opcion=input("Ingrese s para cargar una persona:  ").upper()
    while (opcion=='S' and lim<(len(personas))):
        nueva_persona=Ingresar_persona()
        personas[lim]=nueva_persona
        lim+=1
        print()
        if lim<(len(personas)):
            opcion=input("Ingrese s para cargar una persona:  ").upper()
    return lim

# Punto B
def promedio_de_Edad(personas,limite):
    total_edad=0
    for i in range (limite):
        total_edad+= personas[i]['edad']
    return (total_edad/limite)

# Punto C - Opción 1
def menores_de_18(personas,limite):
    for i in range (limite):
        if (personas[i]['edad'])<18:
            print(personas[i]['apellido']+' '+ personas[i]['nombre'])

# Punto C - Opción 2           
menores=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def menores_de_18_lista(personas,limite,limite_Menor):
    for i in range (limite):
        if (personas[i]['edad'])<18:
            menores[limite_Menor]=personas[i]
            limite_Menor+=1
    return(limite_Menor)
            
# Punto D
def burbuja(personas, limite,campo1,campo2):
    for i in range(limite - 1):
        for j in range(limite - 1 - i):
            persona_actual = personas[j][campo1] +' '+ personas[j][campo2]
            persona_siguiente = personas[j + 1][campo1] + ' '+ personas[j + 1][campo2]
            if persona_actual > persona_siguiente:
                aux = personas[j]
                personas[j] = personas[j + 1]
                personas[j + 1] = aux

def listado_alfa(personas, limite):
    for i in range (limite):
        print(personas[i]['apellido']+' '+ personas[i]['nombre'])

# Punto E - Opción 1
def Adele(personas, limite):
    cont=0
    for i in range (limite):
        if (personas[i]['autor'])=='ADELE':
            cont+=1
    return cont

# Punto E - Opción 2
def busqueda_binaria(personas, limite, buscado):
    pri = 0
    ult = limite-1
    pos = -1
    while (pos == -1) and (pri <= ult):
        med = (pri + ult) // 2
        if (personas[med]['autor'])== buscado:
            pos = med
        elif (personas[med]['autor']) >= buscado:
            ult = med - 1
        else:
            pri = med + 1
    return pos

# Punto F
def listado_autor(personas, limite):
    for i in range (limite):
        print(personas[i]['autor']+' - '+ personas[i]['cancion'])

# Punto G
def promedio_menores_18(personas,limite):
    cont=0
    for i in range (limite):
        if (personas[i]['edad'])<18:
            cont+=1
    return (cont*100/limite)

# Cuerpo Principal
print('--- Punto A')
lim=0
limite=(Cargar_personas(personas, lim)) 
print()
print('--- Punto B')
promed=(promedio_de_Edad(personas,limite)) 
print('El promedio de edad de los participantes es: ', promed)
print()
print('--- Punto C - opcion 1')
menores_de_18(personas,limite) 
print()
print('--- Punto C - Opción 2')
limite_Menor=0
Limite_nuevo=menores_de_18_lista(personas,limite,limite_Menor)
for i in range (Limite_nuevo):
    print(menores[i])
print()
print ('--- Punto D')
campo1='apellido'
campo2='nombre'
burbuja(personas, limite,campo1,campo2) 
listado_alfa(personas, limite)
print()
print ('--- Punto E - Opción 1')
cont=Adele(personas, limite) 
if cont!=0:
    print('el total de canciones de Adele son: ', cont)
else: print('No hay canciones de Adele')
print()
print ('--- Punto E - Opción 2')
campo1='autor'
campo2='cancion'
burbuja(personas, limite,campo1,campo2)
buscado='ADELE'
x=busqueda_binaria(personas,limite, buscado)
if x!=-1: print('existen al menos una cancion de',buscado)
else: print(buscado,' no está en la lista')
print()
print ('--- Punto F')
campo1='autor'
campo2='cancion'
burbuja(personas, limite,campo1,campo2)
listado_autor(personas, limite)
print()
print ('--- Punto G')
prom_menor = promedio_menores_18(personas,limite)
print("El porcentaje de menores de 18 años es: ", prom_menor)