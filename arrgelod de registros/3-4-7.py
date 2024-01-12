# 3- Se tiene una clase de 30 estudiantes, 
# para c/u se almacenan los siguientes datos:
# - Nro_estudiante
# - Nombre
# Nota Se pide:
# a- Lista de alumnos con sus respectivas notas
# ordenados alfabéticamente.
# b- Nro. de estudiante con mayor nota.
# c- Nombre de estudiante de menor nota.
# d- Nota que obtuvo la alumna Laura Suárez.
vector=[0,0,0,0]

def dic():
  num=int(input("numero de estudiante")),
  nom=str(input("Nombre de estudiante")),
  nota=float(input("Nota del alumno"))
  

  DATOS={
    "n":num,
    "nombre":nom,
    "nota":nota
  }
  return(DATOS)

def carga(vector,lim):
  for i in range(len(vector)):
    rta=str(input("Desea cargar Alumno"))
    while rta=="s" and lim <len(vector):
      vector[lim]=dic()
      lim+=1
    if lim<len(vector):
      rta=str(input("desea cargar Alumno"))
    return(lim)
  # ordenados alfabéticamente.
def ordenarNombres(vector, limite):
    for i in range(limite - 1):
        for j in range(limite - i - 1):
            if vector[j]["nombre"] > vector[j + 1]["nombre"]:
                aux=vector[j]
                vector[j]=vector[j+1]
                vector[j+1]=aux
# a- Lista de alumnos con sus respectivas notas
def mostrarvector(vector,lim):
   for i in range(lim):
      print(vector[i])

# b- Nro. de estudiante con mayor nota.
def notamay(vector,lim):
   for i in range(lim):
      max=0 #nota minima(1)//maxima(10)
      if vector[i]["nota"]>max:
         max=vector[i]["nota"]
         info=vector[i]["n"]
   print(f"el alumno con la mayor nota es el Nº: {info}, con nota: {max}")
      
# c- Nombre de estudiante de menor nota.
def notamin(vector,lim):
   for i in range(lim):
      min=11 #nota minima(1)//maxima(10)
      if vector[i]["nota"]<min:
         min=vector[i]["nota"]
         info=vector[i]["nombre"]
   print(f"el alumno con la menor nota es el Nº: {info}, con nota: {min}")

# d- Nota que obtuvo la alumna Laura Suárez.
def busca(vector,lim):
   buscado=str(input("Nombre del buscado"))
   for i in range(lim):
    if vector[i]["nombre"]== buscado:
       nota=vector[i]["nota"]
       print(f"Nota Del alumno {buscado}: {nota}")
       break

lim=0
carga(vector,lim)
ordenarNombres(vector, lim)
mostrarvector(vector,lim)
notamay(vector,lim)
busca(vector,lim)

# 4- Escribir un programa que lea los valores 
# de c/campo de un registro de stock de un almacén. Los 
# campos son:
# - Cod_art: integer;
# - Descripción: string [30];
# - Cantidad: word; (0 ..65535)
# - Precio_unitario: real; 
# Se pide además:
# a- Cargar datos hasta que el cod_art = 0.
# b- Mostrar del artículo más caro, cantidad en existencia. 
# c- Dado un cod_articulo ver si existe.
# d- Mostrar si este almacén vende queso “Don Bautista”. 
# e- Mostrar el artículo con menor existencia.
# f- Mostrar cual es el artículo más barato.

vector=[0,0,0,0]
def dic(aux):
        articulo=int(input("codigo de articulo: "))
        descripcion=str(input("descripción: "))
        cantidad=int(input("Cantidad: "))
        precio=float(input("Precio unitario: "))
        
        DATO={
       "articulo":articulo,
       "descripcion":descripcion,
       "cantidad":cantidad,
       "precio":precio
       }

# a- Cargar datos hasta que el cod_art = 0.
def carga(vector,lim):
    rta=str(input("desea cargar? s/n"))
    while rta=="si" and lim<len(vector):
        vector[lim]=dic()
        if lim<len(vector) and vector[lim]["articulo"]!=0:
            rta=str(input("desea cargar? s/n"))
    return(lim)

# b- Mostrar del artículo más caro, cantidad en existencia. 
def artcaro(vector,lim):
   for i in range(lim):
     articulo=""
     cant=0
     if vector[i]["precio"]>cant:
            cant=vector[i]["precio"]
            articulo=vector[i]["descripcion"]

# c- Dado un cod_articulo ver si existe.
# d- Mostrar si este almacén vende queso “Don Bautista”.
def busca(vector,lim):
   for i in range(lim):
        buscado=str(input("Ingrese el buscado"))
        if vector[i]["articulo"]==buscado:
            print(f"existe, información general: {vector[i]}")

# e- Mostrar el artículo con menor existencia.

#basandome en un catálogo o en la cantidad ingresada?

# f- Mostrar cual es el artículo más barato.
def artbarato(vector,lim):
   for i in range(lim):
     cant=999999999.99
     articulo
     if vector[i]["precio"]<cant:
            cant=vector[i]["precio"]
            articulo=vector[i]["descripcion"]
     print(f"articulo más barato: {articulo} con un precio de: {cant}")


# En una empresa se guardan los códigos de 
# empleados, edades, los sueldos y la antigüedad 
# en años (Nº entero). Se pide calcular: 
# a- Sueldo del empleado más antiguo y edad. 
# b- Sueldo del empleado más nuevo y edad. 
# c- Promedio de sueldos. d- Promedio de edades.
vector=[0,0,0,0]

def dic():
   nombre=str(input("nombre: "))
   empleado=str(input("codigo empleado: "))
   edad=int(input("edad del empleado: "))
   sueldo=float(input("Sueldo: "))
   antiguedad=int(input("Antiguedad: "))

   DATO={
      "nombre":nombre,
      "cod":empleado,
      "edad":edad,
      "sueldo":sueldo,
      "antiguedad":antiguedad
   }

def carga(vector,lim):
   rta=str(input("carga de usuario?? s/n"))
   while rta=="s":
      vector[lim]=dic()
      if lim<len(vector):
         rta=str(input("carga de usuario?? s/n"))


# a- Sueldo del empleado más antiguo y edad. 
def antiguo(vector,lim):
   for i in range(lim):
      antiguo=0
      if vector[lim]["antiguedad"]>antiguo:
         antiguo=vector[lim]["antiguedad"]
         todo=vector[lim]
   print("Empleado más antiguo: ",todo["nombre"])
   print("Edad: ",todo["edad"])
   print("Antiguedad: ", todo["antiguedad"])

# b- Sueldo del empleado más nuevo y edad. 
def antiguo(vector,lim):
   for i in range(lim):
      antiguo=9999
      if vector[lim]["antiguedad"]<antiguo:
         antiguo=vector[lim]["antiguedad"]
         todo=vector[lim]
   print("Empleado más joven: ",todo["nombre"])
   print("Edad: ",todo["edad"])
   print("sueldo: ", todo["sueldo"])

# c- Promedio de sueldos. 
def promediosueldo(vector,lim):
   for i in range(lim):
      total+=vector[lim]["sueldo"]
   print(f"promedio de sueldos: {total/lim}")

# d- Promedio de edades.
def promedioedad(vector,lim):
   for i in range(lim):
      total+=vector[lim]["edad"]
   print(f"promedio de sueldos: {total/lim}")

