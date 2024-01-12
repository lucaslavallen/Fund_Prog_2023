
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

