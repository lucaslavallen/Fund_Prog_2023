matriz=[[78,13,23], [4,5,24],[3,4,33]]
for i in range(len(matriz)):#varia entre 0 y 1
    for j in range(len(matriz)):
	    if i==j:
                print(matriz [i][j]) #imprime elementos de la diagonal principal