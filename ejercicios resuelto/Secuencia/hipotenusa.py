#ejercicio 2 guia 1 - Dadas las longitudes de los dos catetos de un triángulo rectángulo, hallar la longitud de la hipotenusa
cat1=float(input("ingrese el valor del primer cateto: "))
cat2=float(input("ingrese el valor del segundo cateto: "))
           #** es potencia - para aplicar raiz cuadrada es equivalente a  **1/2
hipotenusa=((cat1**2)+(cat2**2))**(1/2)  # o 0.5 si es cúbica **1/3
print(hipotenusa)
