# Fernando Romero
# Crea una lista de números enteros y pide al usuario que ingrese otro número entero. 
# Luego, busca el número ingresado en la lista y 
# muestra la posición en la que se encuentra. Si el número no se encuentra en la lista,
# muestra un mensaje indicando que no se encontró


respuesta= "y"
lista_numeros=[]

while respuesta=="y":
    numero=input("Ingrese un numero: ")
    numero_ingresado=int(numero)
    lista_numeros.append(numero_ingresado)



    respuesta=input("ingresa otro numero? y/n: ")

print("Numeros ingresado: ",lista_numeros)
    
otro_numero = input("Ingrese otro numero: ")
otro_numero_ingresado=int(otro_numero)

for buscar_numero in range(len(lista_numeros)):
    if lista_numeros[buscar_numero] == otro_numero_ingresado:
        print("El numero {}, se encuentra en la posicion {} de la lista".format(otro_numero_ingresado,buscar_numero+1))
    else:
        print("No se encontro el numero")

