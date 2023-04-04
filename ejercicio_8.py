
# Ejercicio 8:
# Fernando Romero 
# Dada la siguiente lista: 
# [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58] 
# mostrar el número repetido

lista_numeros = [82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58]

# for i in range(len(lista_numeros)):
#     print(lista_numeros[i]) #82, 3, 49, 38, 94, 85, 95, 92, 64, 8, 75, 37, 97, 45, 12, 64, 48, 78, 29, 58
repetidos = []
for numeros in lista_numeros:
    if lista_numeros.count(numeros) > 1 and numeros not in repetidos:
        repetidos.append(numeros)
print("Los numeros repetidos son: ",repetidos)