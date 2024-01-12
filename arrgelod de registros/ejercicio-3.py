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
