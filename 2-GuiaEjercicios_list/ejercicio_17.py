# Fernando Romero
# Crea dos listas de números y encuentra los elementos que se encuentran en ambas listas.

lista_uno=[1,2,3,4]
lista_dos=[1,2,5,6]

lista_iguales=[]

for numeros in lista_uno:
    if numeros in lista_dos:
        lista_iguales.append(numeros)

print(lista_iguales)