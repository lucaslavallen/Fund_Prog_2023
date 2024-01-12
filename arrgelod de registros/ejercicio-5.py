# En una librería se almacenan los datos de x cantidad de libros, por cada libro se tiene la siguiente
# información: código y stock. Realizar un programa que informe cuando se deba reponer stock de
# cada libro, considerando stock mínimo = 3 libros.


import os 
os.system('cls')

libros = [0,0,0,0]

def dic():
    codigo = int(input("ingrese codigo del libro: "))
    stock = int(input("ingrese cantidad de stock: "))

    libreria={
        "codigo":codigo,
        "stock":stock
    }
    return(libreria)
   


def cargarLibro(lim, libros):
    op = int(input("ingrese 0 para continuar / 1 para salir:"))
    while (op == 0 ) and lim<(len(libros)):
        nuevo_libro = dic()
        libros[lim] = nuevo_libro
        lim +=1
        if lim<(len(libros)):
            op=int(input("ingrese 0 para continuar / 1 para salir:"))
    return lim 




def ventaLibro(limite,libros):
    for i in range (0, limite,1):
        if libros[i]['stock'] < 3:        
            print("falta stock de", libros[i]['codigo'])
        
    



lim= 0
limite=cargarLibro(lim,libros)
ventaLibro(limite,libros)

print('la cantidad de libros cargadas son',limite)



  
