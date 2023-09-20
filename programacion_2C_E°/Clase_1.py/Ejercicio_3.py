# Ejercicio 3:
# Ingresar 5 números enteros, distintos de cero.
# Informar:
# a. Cantidad de pares e impares.
# b. El menor número ingresado.
# c. De los pares el mayor número ingresado.
# d. Suma de los positivos.
# e. Producto de los negativos.

contador = 0
pares = 0
impares = 0
acumulador_positivos = 0 
producto_negativos = 1
bandera_par = 0

while contador < 4: 
    numero_ingresado = input("Ingrese un numero: ")
    numero_ingresado = int(numero_ingresado)

    resto = numero_ingresado % 2
    resto = int(resto)
    if resto == 0: 
        pares = pares + 1 
        if bandera_par == 0 or numero_ingresado > numero_mayor_par:
            numero_mayor_par = numero_ingresado
            bandera_par = 1
    else:
        impares = impares + 1

    if contador == 0 or numero_ingresado < numero_menor:
        numero_menor = numero_ingresado
    
    if numero_ingresado > -1:
        acumulador_positivos = acumulador_positivos + numero_ingresado
    else:
        producto_negativos = producto_negativos * numero_ingresado


    contador = contador + 1

print("Contador de pares: {} Contador impares: {} Menor numero ingresado: {} Mayor numero ingresado par: {} Acumulador positivos: {} Producto negativos: {}".format(pares,impares,numero_menor,numero_mayor_par,acumulador_positivos,producto_negativos))