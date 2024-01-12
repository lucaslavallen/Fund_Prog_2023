#ej 1 tp condicional
num=int(input("ingrese un numero para clasificar: "))
#recordar que las palabras reservadas van en minusculas
if num>0:
    print("es positivo")
elif num<0:
        print("es negativo")
else:
    print("es cero")