# Fernando Romero
# Escribir un programa que le pida al usuario que ingrese un número entero,
# y luego imprima "El número ingresado es par" si el número es divisible por 2,
# o "El número ingresado es impar" si el número no es divisible por 2.

numero = input("ingrese un numero entero: ")
numero_ingresado = int(numero)

if numero_ingresado % 2 == 0:
    print("El numero ingresado es par")
else:
    print("El numero ingresado es impar")