import os,random
os.system('cls')

Vector = []
Tamanio = 10

def burbuja(lista,lim):
    for i in range(0,(len(lista)-1)-1):
        for j in range(0,len(lista)-1-i):
            if lista[j]>lista[j+1]:
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
                print(aux, Vector)


for i in range(Tamanio):
    Vector = Vector + [0] # Agrega 0 a la lista en cada posición

print('Lista creada: ', Vector)    
input()

for i in range(len(Vector)):
    nuevo_valor=random.randint(1,100)
    Vector[i]=nuevo_valor

print('Lista nueva: ', Vector)

input()

lim=0
burbuja(Vector,lim)

print('Lista ordenada: ', Vector)