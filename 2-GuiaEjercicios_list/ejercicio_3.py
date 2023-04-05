# Fernando Romero
# Crea una lista vacía y pide al usuario que ingrese números enteros 
# hasta que ingrese un número negativo. 
# Luego, muestra la suma de todos los números ingresados.

lista = []

for positivos in range(100):
    numeros = input("Ingrese un numero: ")
    numero_ingresado = int(numeros)
    if numero_ingresado < 0:
        break
    lista.append(numero_ingresado)

print(lista)



