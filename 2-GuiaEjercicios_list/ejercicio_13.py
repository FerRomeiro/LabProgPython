# Fernando Romero
# Crea una lista de números y encuentra el promedio de todos los números en la lista.


lista_numeros=[1,2,3,4,5]
acumulador_numeros=0

for numeros in lista_numeros:
    acumulador_numeros = acumulador_numeros + numeros
    promedio_numeros=acumulador_numeros/len(lista_numeros)

print("El promedio: ",promedio_numeros)