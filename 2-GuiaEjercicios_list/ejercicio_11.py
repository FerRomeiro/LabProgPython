# Fernando Romero
# Crea una lista de palabras y pide al usuario que ingrese una palabra. 
# Luego, muestra todas las palabras de la lista que tienen la misma longitud que la palabra ingresada.

lista_palabras = ["casa","perro","medicina","veterinaria","gato"]

palabra = input("ingrese palabra: ")


for palabras in lista_palabras:

    if palabras == palabra:
        
        for indice in range(len(lista_palabras)):
            if lista_palabras[indice] == palabra:
                bandera=True
                #print(len(lista_palabras[2])) OSEA USO LEN(([0])) APARECE EL NUMERO DE LETRAS
                #len() PARA SABER LA CANTIDAD DE ELEMENTOS
                #range() LO USAMOS EN EL FOR COMO CONTADOR
                break

if bandera==True:
    print("La palabra {} esta en la lista y esta en el indice {}".format(palabra,indice+1))
else:
    print("La palabra no esta en la lista")
