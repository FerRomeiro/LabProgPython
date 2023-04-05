# Fernando Romero
# Crea una lista vacía y pide al usuario que ingrese una palabra. 
# Luego, muestra la primera letra de la palabra. Repite 
# este proceso hasta que el usuario ingrese una palabra que comience con la letra "z".

lista = []


for palabras in range(19):
    palabra = input("Ingrese una palabra: ")
    if palabra[0] == "z":
        break
    lista.append(palabra)

print(lista)