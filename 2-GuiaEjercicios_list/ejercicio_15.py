# Fernando Romero
# Crea una lista de números enteros
# y luego encuentra la suma de los números en índices impares.

lista_numeros=[1,2,3,4,5,6,7,8,9,10]
#suma=[]
acumulador  = 0
for numeros in range(len(lista_numeros)):
    if numeros % 2 == 0:
        #suma.append()
        acumulador=acumulador+lista_numeros[numeros]

print(acumulador)