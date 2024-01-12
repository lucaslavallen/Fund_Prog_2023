lista = [3,1,5,7]

def burbuja(lista):
    for i in range(0,(len(lista)-1)-1):
        for j in range(0,len(lista)-1-i):
            if lista[j]>lista[j+1]:
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
                print(lista)
               

burbuja(lista)