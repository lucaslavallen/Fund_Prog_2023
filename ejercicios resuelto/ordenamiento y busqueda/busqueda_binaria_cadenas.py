#Ordenamiento Burbuja
lista=['rossana','maría','elias','javier','python','frida']
for i in range(0,(len(lista)-1)-1):
        for j in range(0,len(lista)-1-i):
                if lista[j]>lista[j+1]:
                        aux=lista[j]
                        lista[j]=lista[j+1]
                        lista[j+1]=aux
#Búsqueda Binaria
buscado='maría'
pri=0
ult=len(lista)-1
pos=0
while (pos==0) and (pri<=ult):
        med=(pri+ult)//2
        if lista[med]==buscado:
            pos=med
        elif lista[med]>=buscado:
                ult=med-1
        else: pri=med+1   
if pos!=0: print('el buscado está en: ', pos)
print(lista)