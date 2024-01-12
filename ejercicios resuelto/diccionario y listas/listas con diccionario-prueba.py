#Se crea una lista
personas=[0,0,0,0,0,0]

#Definir una función para ingresar datos de una persona en un diccionario
def Ingresar_persona():
    nombre=input("Ingrese el nombre de la persona: ")
    apellido=input("Ingrese el apellido de la persona: ")
    edad=int(input("Ingrese la edad de la persona: "))
    ciudad=input("Ingrese la ciudad de la persona: ")

    persona={
        'nombre':nombre,
        'apellido':apellido,
        'edad':edad,
        'ciudad':ciudad
    }

    return persona

#Cargar con s
#ciclo mientras 
def Cargar_personas(lim,personas):
    opcion=input("Ingrese s para cargar una persona:  ")
    while (opcion=='s' and lim<(len(personas))):
        nueva_persona=Ingresar_persona()
        personas[lim]=nueva_persona
        lim+=1
        print()
        if lim<(len(personas)):
            opcion=input("Ingrese s para cargar una persona:  ")
    return lim


def Mostrar_personas(personas,limite):
   for i in range(0,limite,1):
       per = personas[i]
       print("Nombre:", per['nombre'])
       print("Apellido:", per['apellido'])
       print("Edad:", per['edad'])
       print("Ciudad:", per['ciudad'])
       print()
#también se puede imprimir de esta forma: print("Nombre:", personas[i]['nombre'])

def edades(personas,limite,total_edades):
    for i in range (0,limite,1):
        total_edades+=personas[i]['edad']
    return total_edades

def promedio_edades(personas,total_edades,limite):
    promedio = total_edades / (limite)
    return promedio

lim=0
total_edades=0
promedio=0
limite=Cargar_personas(lim,personas)
print('la cantidad de personas cargadas es',limite)
Mostrar_personas(personas,limite)

#si no se incrementó limite, significa que no tenemos elementos en la lista para calcular promedio de edades
if limite != 0:
    total=edades(personas,limite,total_edades)
    promedio = promedio_edades(personas, total, limite)
print("El promedio de las edades es:", promedio)