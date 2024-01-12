# metodos para el examen
import os 
os.system('cls')
# 1. metodo de ordenamiento

# metodo burbuja 
lista = [2,4,7,9,13,5,1]

def metodo_burbuja(lista):
    n = len(lista)
    for i in range(n-1): #ciclo padre "i"
        for j in range(n-1-i): # ciclo hijo "j"
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j] 


metodo_burbuja(lista)
print(lista)

# metodo binario -> Busqueda Binario

# primero se emplea el ordenamiento burbuja y luego la busqueda binaria

buscado = 9
pri = 0
ult = len(lista)-1
pos = 0
while (pos == 0) and (pos <= ult):
    med = (pri+ult) 
    if lista[med] == buscado:
        pos = med
    elif lista[med] >= buscado:
        ult = med -1 
    else: pri = med +1
if pos != 0: print(f"el numero buscado es {pos}")

print(lista)

# cargar una matriz cuadrada o 2x2

matriz = [[0,0] , [0,0]]

for i in range (len(matriz)):
    for j in range (len(matriz)): # si y solo si la matriz es cuadrada se usa en len()
        matriz[i][j] = int(input("ingrese un numero: "))

print (matriz)


# cargar una matriz rectangular 

matria_A = [[0,0,0], [0,0,0]]

for a in range (len(matria_A)):
    for b in range (len(matria_A[0])):
        matria_A[a][b] = int(input("ingrese numeros: "))



# arreglo de registros

personas = [0,0,0,0]

def ingresar_persona():
    nombre=input("Ingrese el nombre de la persona: ")
    apellido=input("Ingrese el apellido de la persona: ")
    edad=int(input("Ingrese la edad de la persona: "))

    # creacion del diccionario
    persona = {
        'nombre':nombre,
        'apellido':apellido,
        'edad':edad,
    }
    return persona # retonar el diccionario


def cargar_persona(lim, personas):
    op = int(input("ingrese un numero 1 - continuar 0 - salir"))
    while (op == 1) and lim < (len(personas)):
        nueva_persona = ingresar_persona()
        personas[lim] = nueva_persona
        lim += 1
        print()
        if lim < (len(personas)):
            op = int(input("ingrese 1 continuar 0 exit"))
    return lim 


lim = 0
limite = cargar_persona(lim,personas)





