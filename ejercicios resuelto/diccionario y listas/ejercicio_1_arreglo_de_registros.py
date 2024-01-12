# Se declara un vector que va a contener al conjunto de personas
# como es el colectivo se la pone en plural
personas=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# Definir una función para ingresar datos de una persona en un diccionarios
def Ingresar_persona():
    # Se va guardando en cada variable la información de cada persona
    nombre=input("Ingrese el nombre de la persona: ")
    apellido=input("Ingrese el apellido de la persona: ")
    edad=int(input("Ingrese la edad de la persona: "))
    peso=int(input("Ingrese el peso de la persona: "))
    genero=input("Ingrese el género de la persona: ")
    altura=float(input("Ingrese la altura de la persona: "))
    piel=input("Ingrese el color de piel de la persona: ")
    ojos=input("Ingrese el color de ojos de la persona: ")
    nacionalidad=input("Ingrese la nacionalidad de la persona: ")

    # Se confecciona el diccionario, a cada campo le asignamos el valor cargado previamente
    # formando asi cada individuo
    persona={
        'nombre':nombre,
        'apellido':apellido,
        'edad':edad,
        'peso':peso,
        'genero':genero,
        'altura':altura,
        'piel':piel,
        'ojos':ojos,
        'nacionalidad':nacionalidad
    }
    return persona # Retorna el diccionario con la información de una persona

#Cargar con con ciclo mientras 
def Cargar_personas(lim,personas): # lim comienza en 0
    opcion=input("Ingrese s para cargar una persona: ")
    while (opcion=='s' and lim<(len(personas))):
        nueva_persona=Ingresar_persona() # La Variable llama a la función la cual le retorna un diccionario
        personas[lim]=nueva_persona # Ahora el Vector en la posición lim guarda el diccionario
        lim+=1 # lim se incrementa en 1
        print()
        if lim<(len(personas)):
            opcion=input("Ingrese s para cargar una persona: ")
    return lim # Retorna la cantidad de elemento cargados que es igual al próximo subindide del vector


def Mostrar_personas(personas,limite):
   for i in range(0,limite,1):
       per = personas[i]
       print("Nombre:", per['nombre'])
       print("Apellido:", per['apellido'])
       print("Edad:", per['edad'])
       print("Peso:", per['peso'])
       print("genero:", per['genero'])
       print("Altura:", per['altura'])
       print("Color de Piel:", per['piel'])
       print("Color de Ojos:", per['ojos'])
       print("Nacionalidad:", per['nacionalidad'])
       print()

def Mas_60_anios(personas,limite):
    total60 = 0
    for i in range (0,limite,1):
        if personas[i]['edad']>60:
            total60+=1
    return total60

def Cantidad_Mujeres_170(personas,limite):
    total_mujeres = 0
    for i in range (0,limite,1):
        if personas[i]['genero']=='mujer' and personas[i]['altura']>1.70:
            total_mujeres+=1
    return total_mujeres

def Porcentaje_50kg(personas,limite):
    porc = 0
    total=0
    for i in range (0,limite,1):
        if personas[i]['peso']<50:
            total+=1
    porc=(total*100)/(limite)
    return porc

def Porcentaje_Hombres_Cubanos(personas,limite):
    cubanos = 0
    total=0
    for i in range (0,limite,1):
        if personas[i]['nacionalidad']=='cubano' and personas[i]['genero']=='hombre' :
            total+=1
    cubanos=(total*100)/(limite)
    return cubanos

def Porcentaje_Mujeres_Argentinas(personas,limite):
    argentinas = 0
    total=0
    for i in range (0,limite,1):
        if personas[i]['nacionalidad']=='argentina' and personas[i]['genero']=='mujer' :
            total+=1
    argentina=(total*100)/(limite)
    return argentina

lim=0
limite=Cargar_personas(lim,personas)
print('la cantidad de personas cargadas son',limite)
Mostrar_personas(personas,limite)
print('la cantidad de personas mayores a 60 años son: ',Mas_60_anios(personas,limite))
print('la cantidad de mujeres con mas de 1.70 de altura son: : ',Cantidad_Mujeres_170(personas,limite))
print('la cantidad de hombres cubanos son: : ',Porcentaje_Hombres_Cubanos(personas,limite))
print('la cantidad de mujeres argentinas son: : ',Porcentaje_Mujeres_Argentinas(personas,limite))