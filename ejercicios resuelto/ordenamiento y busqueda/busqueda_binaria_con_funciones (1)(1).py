lista=['rossana','maría','elias','javier','python','frida']

#Ordenamiento Burbuja
def burbuja(lista,lim):
    for i in range(0,(len(lista)-1)-1):
        for j in range(0,len(lista)-1-i):
            if lista[j]>lista[j+1]:
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux


def busqueda_binaria(lista,lim, buscado, pos):
    pri=0
    ult=len(lista)-1
    while (pos==0) and (pri<=ult):
        med=(pri+ult)//2
        if lista[med]==buscado:
            pos=med
        elif lista[med]>=buscado:
            ult=med-1
        else:
            pri=med+1   
    return(pos)

def mostrar_lista(lista):
    print(lista)


buscado=input('ingrese el dato a buscar: ')  
pos=0
lim=len(lista)  
mostrar_lista(lista)
burbuja(lista, lim)
mostrar_lista(lista)
x=busqueda_binaria(lista,lim, buscado, pos)
if x!=0: print('el buscado está en: ', x)
else: print('el buscado no está en la lista')
