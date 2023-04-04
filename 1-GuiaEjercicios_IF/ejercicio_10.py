# Fernando Romero
# Escribir un programa que le pida al usuario que ingrese un número entero,
# y luego imprima "El número es positivo y par" si el número es positivo y divisible por 2,
# o "El número no cumple ninguna condición" si el número no cumple ninguna de las 
# dos condiciones anteriores.

numero = input("Ingrese un numero:")
numero_ingresado = int(numero)

if numero_ingresado % 2 == 0 and numero_ingresado > 0:
    print("El numero es positivo y par")
elif numero_ingresado % 2 != 0 and numero_ingresado < 0:
    print("El numero no es positivo ni par")