#3.	Leer N  elementos, de a uno por vez. Generar y emitir la sumatoria de sus componentes de posición par de acuerdo a la posición ingresada
ac=0
for i in range (10):
    num=int(input("ingrese un valor: ")) #cast o casting
    if i%2==0:
        ac=ac+num
print("el total acumulado es:", ac)