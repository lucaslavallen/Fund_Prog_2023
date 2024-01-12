matriz=[[0,0],[0,0]]
for i in range(len(matriz)):
    for j in range(len(matriz)): #solo si la matriz es cuadrada
	    matriz[i][j]=int(input('ingrese el elemento: '))
print(matriz)