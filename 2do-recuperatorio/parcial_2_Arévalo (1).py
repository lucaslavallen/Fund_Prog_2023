lista=[0,0]

buscado="san sebastian"



def cargar_registro():

    barrio=input("ingrese nombre del barrio: ")
    serv_clu=input("si tiene servicio de cloacas ingrese si, de lo contrario ingrese no: ")
    familias=int(input("ingrese numero de familias: "))

    barrio_lista={
        'barrio':barrio,
        'serv_clu':serv_clu,
        'familias':familias
    }
    return barrio_lista


def cargar_lista(lista):
    for i in range(len(lista)):
        lista[i]=cargar_registro()
    return lista

print(cargar_lista(lista))

cantidad=len(lista)
print("la cantidad de barrios son:",cantidad)



acum=0
for i in range(len(lista)):
    acum+=lista[i]['familias']
    
prom=acum//cantidad
print("el promedio de familias por barrio es de: ",prom)

sinclu=0
for i in range(len(lista)):
    if lista[i]['serv_clu']=='no':
        sinclu+=1
print('la cantidad de barrios sin cloaca es de:',sinclu)



def burbuja(lista):
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j]['barrio']>lista[j+1]['barrio']:
                aux=lista[j]
                lista[j]=lista[j+1]
                lista[j+1]=aux
    return lista

print(burbuja(lista))



def busqueda(lista,buscado):
    pos=-1
    pri=1
    ult=len(lista)
    while pos==-1 and pri<ult:
        med=(pri+ult)//2
        if lista[med]==buscado:
            pos=med
        elif lista[med]['barrio']>buscado:
            ult=med-1
        else: ult=pri+1
    return pos

indice_busc=busqueda(lista,buscado)
print("el barrio buscado esta en el indice:", indice_busc)


("el promedio que representa el barrio san sebastian con respecto a los demas es de: ",(lista[indice_busc]['familias']*100/acum))


#2_
matriz=[[2,3],[5,4]]
acum_enteros=0
for i in range(len(matriz)):
    for j in range(len(matriz)):
        if i==j :
            if (matriz[i][j])%2==0:
                acum_enteros+=1
print("la cantidad de numeros enteros en la diag principal es:", acum_enteros)

