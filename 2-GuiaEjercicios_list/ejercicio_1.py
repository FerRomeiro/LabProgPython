# Fernando Romero
# Crea una lista con los números del 1 al 10 e imprime solo los números impares.

#lista = [0,1,2,3,4,5,6,7,8,9]
lista = range(0,10)

for numero in lista:

    if numero % 2 != 0:
        print(numero)

#con while:
# numero = 0
# while numero < len(lista):
#     if numero % 2 != 0:
#         print(numero)
#     numero = numero + 1

