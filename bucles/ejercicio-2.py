#Calcular la suma y el producto de los números pares comprendidos entre 20 y 500

s = 0 
p = 1

for num in range(20,500):
    if num % 2 == 0: #verificar si el numero es par 
        s += 1
        p *= num


print("suma de los numeros: ", s)
print("producto de los numeros: ", p)