resultado = [[0, 0], [0, 0]]
matriz_1=[[78, 3], [4, 5]]
matriz_2=[[6, 3], [1, 2]]
for i in range(len(matriz_1)):#varia entre 0 y 1, recordar que el limite superior es lim-1
    for j in range(len(matriz_1)):
	    resultado[i][j] = (matriz_1[i][j] + matriz_2[i][j])
print(resultado)
