# Sea un lote de Números enteros positivos que finaliza con un cero que no debe ser procesado. Generar un vector con dichos valores y calcular la productoria de sus componentes. 

vector = [0,0,0,0,0]
lim = 0

        
def cargar(lim):
  num = int(input("ingrese un numero: "))
  while num != 0 and lim < len(vector):
    vector [lim] = num
    lim +=1
    num = int(input("vuelva a ingresar un numero: "))
  return (lim)


def multi(vector,lim):
  producto=1
  for i in range(lim):
    producto = producto * vector[i]
  print(producto)


lim = cargar(lim)
multi(vector, lim)

