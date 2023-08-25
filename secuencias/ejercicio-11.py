# Un millonario excéntrico tenía tres hijos: Carlos, José y Marta. Al morir dejó el siguiente 
# legado: A José le dejó 4/3 de lo que le dejó a Carlos. A Carlos le dejó 1/3 de su fortuna. A 
# Marta le dejo la mitad de lo que le dejó a José. Preparar un algoritmo para darle la suma 
# a repartir e imprima cuanto le tocó a cada uno.

# marta 2/3


fortuna = float(input("cargue fortuna del millonario:"))

jose =  fortuna / 0.75 

carlos = 0.33 / jose

marta = 0.375 / fortuna

print("legado de jose es " , jose)
# print(f"legado de carlos es ${carlos}")
# print(f"legado de marta es ${marta}")