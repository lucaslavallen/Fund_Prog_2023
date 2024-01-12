
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

