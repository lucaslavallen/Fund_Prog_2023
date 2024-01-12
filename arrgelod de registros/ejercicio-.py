# 1- Se tienen los datos de los afiliados que realizan aportes a obras sociales, de cada
# uno se almacena Apellido y nombre, Obra social, Monto de cuota y cantidad de
# integrantes del grupo familiar.
# Se pide:
# a- Realice un subprograma que cargue los datos hasta que el usuario lo desee.
# b- Listado ordenado por Obra Social y apellido y nombre.
# d- Mostrar total aportado a esta obra social por todos sus afiliados (IOSPER).
# e- Calcular total de familias que poseen más de 6 integrantes en su grupo familiar, 
# y de éstos mostrar solo los que aportan más de 10000 pesos.
# f- Mostrar si Pablo Benitez es afiliado, de ser asi mostrar la cantidad de integrantes
# del grupo familiar y la obra socia
import os
os.system('cls')

datos = [0,0,0,0,0]
# informacion de las personas 

def persona():
    nombre = str(input("ingrese su nombre: "))
    apellido = str(input("ingrese su apellido: "))
    obraSocial = str(input("ingrese su obra social: "))
    montoCuota = int(input("ingrese monto de su cuota: "))
    integrantes = int(input("ingrese cantidad de integrantes de su familia: "))




    DATE={
        "nombre":nombre,
        "apellido": apellido,
        "obraSocial": obraSocial,
        "montoCuota":montoCuota,
        "integrantes":integrantes
    }

    return(DATE)


# cargar las personas
def cargarPersona(lim, datos):
    op = int(input("ingrese 0 para continuar / 1 para salir:"))
    while (op == 0 ) and lim<(len(datos)):
        nueva_persona = persona()
        datos[lim] = nueva_persona
        lim +=1
        if lim<(len(datos)):
            op=int(input("ingrese 0 para continuar / 1 para salir:"))
    return lim 



# metodo burbuja de ordenamiento

def burbuja(datos, limite):
    for i in range(limite - 1):
        for j in range(limite - 1 - i):
            nombre_apellido_actual =  datos[j]['obraSocial'] +  datos[j]['apellido'] + datos[j]['nombre'] 
            nombre_apellido_siguiente = datos[j + 1]['obraSocial'] + datos[j + 1]['apellido']  + datos[j + 1]['nombre'] 
            if nombre_apellido_actual > nombre_apellido_siguiente:
                aux = datos[j]
                datos[j] = datos[j + 1]
                datos[j + 1] = aux


def montoAportado(datos,limite):
    total = 0
    for i in range (0,limite,1):
        if ['obraSocial'] == 'iosper':
           total += datos[i]['montoCuota']
           
    return total



def Mostrar_personas(datos, limite):
   for i in range(0, limite, 1):
       per = datos[i]
       print("nombre:", per['nombre'])
       print("Apellido:", per['apellido'])
       print('obraSocial',per['obraSocial'])
       print("montoCuota:", per['montoCuota'])
       print("integrantes:", per['integrantes'])
       print()





lim = 0

person = cargarPersona(lim,datos)
burbuja(datos,person)
Mostrar_personas(datos, person)

print(f"datos de la persona{person}")

print (montoAportado(datos, lim))

# def iosper ()
#     total = 0
#     for i in range(0,limite,1)
#     total += afiliado[i]['cuota']
#     return total