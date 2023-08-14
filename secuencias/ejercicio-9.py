# De los y las estudiantes de Fundamentos de Programación se desea saber qué porcentaje 
# de personas menores a 20 años se encuentran cursando la materia. El programa debe 
# solicitar al usuario que ingrese la cantidad total de estudiantes menores a 20 años y el 
# total.


estudiantesDeFp = int(input("ingrese alumnos menores de 20 años: "))

estudiantesTotales = int(input("ingrese cantidad de alumnos: "))

porcentajeDeMenores = (estudiantesDeFp / estudiantesTotales) * 100

print("menores que estan cursando en la catedra son: ", porcentajeDeMenores, "%")