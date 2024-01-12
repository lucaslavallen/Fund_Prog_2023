# leer un vector n elementos, de a uno por vez y a la vez generar y emitir la sumatoria de sus componentes 

vector = [0,0,0,0]


suma = 0
def cargar(vector):
    for i in range(0,4):
        vector[i] = int(input("ingrese un numero: "))


def sumatoria(suma):
    for i in range(0,3):
        if i % 2 ==0:
            suma=suma+vector[i]
            return suma

cargar(vector)

sumatoria(suma)

print("la sumatoria es ", sumatoria(suma))