# Ejercicio 7:
# Fernando Romero 
# Dada la siguiente lista: 
# [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58] 
#mostrar solo los números pares. 

lista_numeros = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]

for numeros in lista_numeros:
    pares = numeros%2
    if pares == 0:
        print("numeros pares son : ",numeros)