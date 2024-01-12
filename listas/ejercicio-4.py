# Generar y emitir el vector A = (1,0,1,0,1,0, ...) de N elementos.

A = [0,0,0,0,0]


def genrador (A):
    for i in range(0,len(A),2):
        A[i]=1
        print(A)

genrador(A)

