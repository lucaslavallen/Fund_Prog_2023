#cuenta la cantidad de números positivos de una lista
c=0
for i in range(1,6,1): #no incluye el ultimo elemento lo hace hasta LS=n-1 y por defecto comienza en cero, el paso por defecto es 1
    n=int(input("ingrese valor: "))
    if n>0:
        c+=1
print("la cantidad de positivos es: ", c)