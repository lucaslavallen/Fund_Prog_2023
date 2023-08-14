
# Diseñe un algoritmo que determine el porcentaje de: Alumnos promocionados, Alumnos 
# regularizados, Alumnos desaprobados y Alumnos libres, teniendo como datos cantidad de 
# alumnos que cumplen con cada condición.

totalAlumnos = int(input("ingrese cantidad de alumnos: "))
promocionados = int(input("cantidad de alumnos promocionados: "))
regularizados = int(input("cantidad de alumnos regularizados: "))
desaprobados = int(input("cantidad de alumnos desaprobados: "))
libres = int(input("cantidad de alumnos libres: "))


porcentajePromocion = (promocionados*100)/totalAlumnos

print("promociono el: ", porcentajePromocion, "%")

porcentajeRegualar = (regularizados*100)/totalAlumnos

print("regularizo el: ", porcentajeRegualar, "%")

porcentajeDesaprobado = (desaprobados*100)/totalAlumnos

print("desaprobo el: ", porcentajeDesaprobado, "%")

porcentajeLibre = (libres*100)/totalAlumnos

print("quedo libre el: ", porcentajeLibre, "%")