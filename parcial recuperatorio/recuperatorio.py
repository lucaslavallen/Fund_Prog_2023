# Se desea crear un programa para administrar una biblioteca de libros. Cada libro tiene la siguiente información:

# - Título del libro.

# - Autor del libro.

# - ISBN (Número Internacional Normalizado del Libro).

# - Cantidad de ejemplares disponibles.

# - Categoría 

# SE DEBE UTILIZAR ORDENAMIENTO BURBUJA Y  BÚSQUEDA BINARIA 

# El programa debe permitir realizar las siguientes operaciones:

# a- Cargar libros: definir la estructura a cargar, teniendo en cuenta que el usuario puede ingresar información sobre libros y salir cuando lo desee

# b- Listar libros: Mostrar la lista de libros ordenados por autor y categoría con su información completa

# c- Buscar libro: Permitir al usuario buscar un libro por su ISBN y mostrar su información si existe.

# d- Actualizar cantidad de ejemplares: El usuario puede ingresar el ISBN de un libro y una cantidad para aumentar la cantidad de ejemplares disponibles, se solicita realizar la función para actualizar dicha cantidad

# e- Calcular la cantidad total de ejemplares: Calcular y mostrar la cantidad total de ejemplares en la biblioteca de los libros que pertenecen a la categoría ciencia ficción 
import os
os.system('cls')
vector = [0,0,0,0,0]

def ingresar_libro():
    titulo = str(input("ingrese titulo: "))
    autor = str(input("ingrese autor: "))
    isbn = int(input("ingrese ISBN: "))
    ejemplares = int(input("cantidad ejemplares: "))
    categoria = str(input("ingrese su categoria: "))

    libro = {
        'titulo': titulo,
        'autor': autor,
        'isbn': isbn,
        'ejemplares': ejemplares,
        'categoria': categoria
    }
    return libro


# a- Cargar libros: definir la estructura a cargar, teniendo en cuenta que el usuario puede ingresar información sobre libros y salir cuando lo desee

def cargar_libro(vector,lim):
    op = str(input("ingrese s para continuar")).upper()
    while (op == 's') and lim < len(vector):
       nuevo_libro = ingresar_libro()
       vector[lim] = nuevo_libro
       lim +=1
    if (op == 's') and lim < len(vector):
             op = str(input("ingrese s para continuar")).upper()
    return lim

# b- Listar libros: Mostrar la lista de libros ordenados por autor y categoría con su información completa
def burbuja(vector,limite,campo1,campo2):
     for i in range(limite -1):
          for j in range (limite -1 -i):
               actual = vector[j][campo1] + vector[j][campo2]
               siguiente = vector[j+1][campo1] + vector[j+1][campo2]
               if actual > siguiente:
                    aux = actual
                    vector[j] = siguiente
                    vector[j+1] = aux
                    
# c- Buscar libro: Permitir al usuario buscar un libro por su ISBN y mostrar su información si existe.




# d- Actualizar cantidad de ejemplares: El usuario puede ingresar el ISBN de un libro y una cantidad para aumentar la cantidad de ejemplares disponibles, se solicita realizar la función para actualizar dicha cantidad



lim = 0

limite = cargar_libro(vector,lim)
campo1 = 'autor'
campo2 = 'categoria'
burbuja(vector,limite,campo1,campo2)


