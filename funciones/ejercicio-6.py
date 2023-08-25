# Escribir un programa que, utilizando procedimientos con parámetros, lea desde el 
# teclado las unidades y el precio que quiere comprar, y en función de las unidades 
# introducidas le haga un descuento o no.

max = 3

def descuentos(precio, unidade):
    if unidade >= max:
        desc = precio * unidade * 0.2
        print("se descontaron: ", desc)
    else:
        print("no cumple el monto minimo de unidades.")
    

precio = int(input("ingrese precio del producto: "))
unidade = int(input("ingrese cantidad de unidades: "))

descuentos(precio, unidade)