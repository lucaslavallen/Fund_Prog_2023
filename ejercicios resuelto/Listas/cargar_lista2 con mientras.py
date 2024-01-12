numeros=[0,0,0,0,0,0,0,0,0,0,0,0]

def cargar_lista2(numeros,lim):
    num= int(input('ingrese un número: '))
    while num!=0 and lim<len(numeros)-1:
        lim+=1
        numeros[lim] = num
        num= int(input('ingrese un número: '))
    return(lim)

def mostrar_lista(numeros,limite): 
    for i in range(0,limite,1):
        print (numeros[i])


lim=-1
limite=cargar_lista2(numeros,lim)
print("el limite es", limite)
mostrar_lista(numeros, limite)

