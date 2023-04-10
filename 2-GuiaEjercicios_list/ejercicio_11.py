# Fernando Romero
# Crea una lista de palabras y pide al usuario que ingrese una palabra. 
# Luego, muestra todas las palabras de la lista que tienen la misma longitud que la palabra ingresada.

lista_palabras = ["casa","perro","medicina","veterinaria","gato"]

palabra = input("ingrese palabra: ")


for palabras in lista_palabras:

    if palabras == palabra:
        print("La palabra esta en la lista")
        break

if palabra!=palabras:
    print("La palabra no esta en la lista")
