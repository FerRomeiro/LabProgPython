'''
Fernando Romero

Ejercicio 3:
Ingresar 5 números enteros, distintos de cero.
Informar:
a. Cantidad de pares e impares.
b. El menor número ingresado.
c. De los pares el mayor número ingresado.
d. Suma de los positivos.
e. Producto de los negativos.
'''

contador = 0
contador_Pares = 0
contador_Impares = 0
bandera_Par = 0
suma_Positivos = 0


while contador < 2:
    numero = input("ingrese un numero: ")
    numero = int(numero)
    #a. Cantidad de pares e impares.
    resto = numero % 2
    resto = int(resto)
    if resto == 0:
        contador_Pares = contador_Pares + 1
        #c. De los pares el mayor número ingresado.
        if bandera_Par == 0 or numero > numero_Mayor_Par:
            numero_Mayor_Par = numero
            bandera_Par == 1
    else:
        contador_Impares = contador_Impares + 1 
    #b. El menor número ingresado.
    if contador == 0 or numero < numero_Menor:
        numero_Menor = numero
    #d. Suma de los positivos.
    if numero > -1:
        suma_Positivos = suma_Positivos + numero
    #e. Producto de los negativos.      
    contador = contador + 1 

numero_Menor = str(numero_Menor)
suma_Positivos = str(suma_Positivos)
contador_Impares = str(contador_Impares)
contador_Pares = str(contador_Pares)
numero_Mayor_Par = str(numero_Mayor_Par)

print("Cantidad Pares: " + contador_Pares)
print("Cantidad impares: " + contador_Impares)
print("El menor numero ingresado: " + numero_Menor)
print("El mayor numero par: " + numero_Mayor_Par)
print("Suma de numeros positivos: " + suma_Positivos)
