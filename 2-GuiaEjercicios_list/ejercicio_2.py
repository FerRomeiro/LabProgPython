# Fernando Romero
# Crea una lista con 5 números enteros. 
# Luego solicita un nuevo número y 
# reemplaza el tercer elemento de la lista por el número ingresado. 
# Finalmente imprime todos los números

#lista = range(0,5) #
lista = [0,1,2,3,4,5]

nuevo_numero = input("Ingrese un numero: ")
numero_ingresado = int(nuevo_numero)
lista[2] = numero_ingresado
print("Lista: ",lista)
