import os,random # Para limpiar consola, se importa la librería os (sistema operativo)
# en Windows 'cls' y en Linux 'clear'
os.system('cls') 

def Crear_valores_random(Lista):
    for i in range(len(Lista)):
        nuevo_valor=random.randint(1,100)
        Lista[i]=nuevo_valor

def Imprimir_cada_uno_de_la_lista(Lista):
    for i in range(len(Lista)):
        print(Lista[i])

def Suma_total_lista(Lista):
    Total_suma = 0
    for i in range(len(Lista)):
        Total_suma += Lista[i]
    return Total_suma

def Cambiar_elemento(Lista):
    print(Lista)
    posicion = int(input('Ingresar la posición del elemento a cambiar: '))
    if 0 <= posicion < len(Lista):
        Lista[posicion] = int(input('Ingrese el nuevo valor: '))
    else:
        print('El valor de la posición es incorrecto')

def Menor_de_la_lista(Lista):
    el_menor=Lista[0]
    for i in range(len(Lista)):
        if el_menor > Lista[i]:
            el_menor = Lista[i]
    return(el_menor)

def numero_buscado(buscado):
    mensaje=""
    for i in range(len(Lista)):
        if buscado==Lista[i]:
            mensaje=(f"En valor {buscado} esta en la posicion: {i}")
        if mensaje == "": 
            mensaje=("En valor no esta")
    return (mensaje)

def Menu():
    print("Elige una opción")
    print()
    print("1 - Crear lista                          2 - cambiar cada elemento con valores random")
    print("3 - Imprimir lista                       4 - Imprimir elemento por elemento")
    print("5 - Cambiar un elemento                  6 - Suma de los elementos de la lista")
    print("7 - Mostrar el menor de los valores      8 - buscar un valor")
    print("9 - Salir")

Lista = []

opcion = 0
while opcion != 9:
    
    Menu()

    print()
    opcion = int(input('Ingrese la opcion: '))
    print()

    if opcion == 1:
        Tamaño_lista = int(input('Ingrese el tamaño de la lista: '))
        Lista = []  # Crea lista vacía
        for i in range(Tamaño_lista):
            Lista = Lista + [0] # Agrega 0 a la lista en cada posición
        print('Lista creada: ',Lista)

    elif opcion == 2:
        Crear_valores_random(Lista)

    elif opcion == 3:    
        print(Lista)

    elif opcion == 4:
        Imprimir_cada_uno_de_la_lista(Lista)

    elif opcion == 5:
        Cambiar_elemento(Lista)

    elif opcion == 6:
        total = Suma_total_lista(Lista)
        print("La suma total de los elementos de la lista es:", total)

    elif opcion == 7:
        menor = Menor_de_la_lista(Lista)
        print("El menor valor de la lista es: ", menor)

    elif opcion == 8:
        buscado=int(input('Ingrese el valor a buscar: '))
        print(numero_buscado(buscado))

    elif opcion == 9:
        print("Saliendo...")

    else:
        print("Opción inválida. Por favor, elige una opción del 1 al 9.")
        
    print()
    input('Teclee para continuar... ')
    os.system('cls')