# Ejercicio 6: 
# Fernando Romero
# Utilizar For 
# Dada la siguiente lista: 
# [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58] 
# mostrar el mayor. 
lista_numeros = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
maximo = lista_numeros[0]

for numero in lista_numeros:
    
    if numero > maximo:
        maximo = numero   

print("El mayor es: ", maximo)
#print(type(numero))

# lista_numeros = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
# maximo = lista_numeros[0]
# i = 0
# while(i < len(numeros)): #len es la cantidad de elementos q tenes en la lista
#     if(lista_numeros[i] > maximo):
#         maximo = lista_numeros[i]
#     i += 1
# print("El mayor es ", maximo)
