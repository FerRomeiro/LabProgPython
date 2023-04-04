# Fernando Romero
# Escribir un programa que le pida al usuario que ingrese un número entero,
# y luego imprima "El número es divisible por 3 y por 5" si el número es divisible por 3 
# y por 5, 
# o "El número no es divisible por 3 y por 5" si el número no es divisible por 3 y por 5.

numero = input("Ingrese un numero: ")
numero_Ingresado = int(numero)

if numero_Ingresado%3 == 0 and numero_Ingresado%5 == 0:
    print("El numero es divisible por 3 y por 5")
else:
    print("No es divisible por 3 ni por 5")