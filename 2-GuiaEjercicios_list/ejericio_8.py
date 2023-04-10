# Fernando Romero
# Crea una lista con los nombres de tus 5 libros favoritos y
# luego imprime solo los primeros 3 libros de la lista.


libros=[]

for library in range(5):
    ingrese_libro = input("Ingrese libro: ")
    libros.append(ingrese_libro)
print(libros[0],libros[1],libros[2])