# .Solicitar al usuario que ingrese el precio de un producto al inicio del año, y el precio del 
# mismo producto transcurrido un determinado tiempo. El usuario debe mostrar cuál fue el 
# porcentaje de aumento que tuvo ese producto en el año.

precio = float(input("ingrese precio producto: "))

numero = float(input("ingrese nuevo valor: "))

nuevoPrecio = 0


nuevoPrecio = (numero * 100) / precio


print(f"porcentaje es ${nuevoPrecio}")
