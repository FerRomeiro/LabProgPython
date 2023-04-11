# Fernando Romero
# Crea dos listas de 10 números enteros cada una y
# realiza una multiplicación de los elementos con el mismo índice en ambas listas.

lista_numeros_uno=[1,2,3,4,5,6,7,8,9,10]
lista_numeros_dos=[11,12,13,14,15,16,17,18,19,20]
resultados=[]
for numeros_uno in range(len(lista_numeros_uno)):
    resultados.append(lista_numeros_uno[numeros_uno]*lista_numeros_dos[numeros_uno])

print(resultados)