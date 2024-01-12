# Supongamos que tienes una lista de pedidos de entrega de alimentos a domicilio. De cada pedido, se tienen los siguientes datos:

#     Nombre del cliente.

#     Dirección de entrega.

#     Total del pedido en pesos.

#     Hora de entrega estimada.

# NOTA: Deben utilizar funciones o procedimientos, su correspondiente invocación, como asi también ordenamiento burbuja y Búsqueda Binaria.

# Se pide:

#     Cargar las estructura que corresponda, hasta que el usuario desee.

#     Mostrar el Total de pedidos.

#     Mostrar el porcentaje que representa el total del pedido del cliente "ClienteVIP" sobre el total de todas las ventas.

#     Cantidad de pedidos con dirección de entrega en una zona específica (por ejemplo, "Centro de la ciudad").

#     Hora promedio de entrega estimada de todos los pedidos.

import os 
os.system('cls')


pedidos = [0,0,0,0]
def ingresar_pedidio():
    nombre_cliente = str(input("ingrese nombre del cliente: "))
    direccion = str(input("ingrese su direccion: "))
    total_del_pedido = float(input("ingrese el total del pedido: "))
    tiempo_de_entrega = float(input("ingrese tiempo estimado: "))

    pedido = {
        'nombre_de_cliente': nombre_cliente,
        'direccion': direccion,
        'total_del_pedido': total_del_pedido,
        'tiempo_de_entrega': tiempo_de_entrega
    }
    return (pedido)



def cargar_pedido(lim,pedidos):
    op = str(input("Ingrese s para cargar una persona: ")).upper()
    while (op == 'S') and lim < (len(pedidos)):
        nuevo_pedido = ingresar_pedidio()
        pedidos[lim] = nuevo_pedido
        lim += 1
        print()
        if lim < (len(pedidos)):
            op = str(input("Ingrese s para cargar una persona: ")).upper()
    return lim

# Listado ordenado por el total del pedido.
def ordenamiento(pedidos,limite):
    for i in range(limite -1):
        for j in range (limite -1 -i):
            pedido_actual = pedidos[j]['total_del_pedido']
            pedido_sig = pedidos[j+1]['total_del_pedido']
            if pedido_actual < pedido_sig:
                aux = pedidos[j]
                pedidos[j] = pedidos[j+1]
                pedidos[j+1] = aux
                
    return pedidos
    


#  Determinar si el cliente con nombre "ClienteVIP" ha realizado algún pedido
def busqueda_binaria(pedidos):
    buscado='vip'
    pri=0
    ult=len(pedidos)-1
    pos=0
    while (pos == 0) and (pri <= ult):
        med = (pri + ult) // 2
        if pedidos[med]['nombre_de_cliente'] == buscado:
            pos = med
            print('el cliente hizo un pedido')
        elif pedidos[med]['nombre_de_cliente'] > buscado:
            ult = med - 1
        else:
            pri = med + 1
            print('no realizo ningun pedido.')
    if pos!=0: print('el buscado está en: ', pos)
    print(pedidos)
    return (pos)




# Mostrar el porcentaje que representa el total del pedido del cliente "ClienteVIP" sobre el total de todas las ventas.
def promedio(pedidos,limite):
    total_pedido=0
    for i in range (limite):
        total_pedido += pedidos[i]['total_del_pedido']
    return (total_pedido*limite)/100

def Mostrar_pedidos(pedidos,limite):
   for i in range(0,limite,1):
       per = pedidos[i]
       print("Nombre:", per['nombre_de_cliente'])
       print("direccion:", per['direccion'])
       print("total:", per['total_del_pedido'])
       print("tiempo:", per['tiempo_de_entrega'])
       print()

# Hora promedio de entrega estimada de todos los pedidos.


#  Cantidad de pedidos con dirección de entrega en una zona específica (por ejemplo, "Centro de la ciudad").





cont = 0
lim = 0
limite = cargar_pedido(lim,pedidos)
print('...punto B')
print('desordenada')
Mostrar_pedidos(pedidos,limite)
ordenamiento(pedidos,limite)
print('ordenada')
Mostrar_pedidos(pedidos,limite)
busqueda_binaria(pedidos)
print("promedio: ")
promedio(pedidos,limite)
print('...puntoC')
direcciones(pedidos)

