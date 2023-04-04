# Fernando Romero
# Escribir un programa que le pida al usuario que ingrese dos números enteros,
# y luego imprima "El primer número es mayor" si el primer número es mayor que el segundo,
# "El segundo número es mayor" si el segundo número es mayor que el primero,
# o "Los dos números son iguales" si los dos números son iguales.

numero_Uno = input("Ingrese el primer numero: ")
primer_Numero = int(numero_Uno)

numero_Dos = input("Ingrese el segundo numero: ")
segundo_Numero = int(numero_Dos)

if primer_Numero == segundo_Numero:
    print("Numeros iguales")
elif primer_Numero > segundo_Numero:
    print("El primer numero es el mayor")
else:
    print("El segundo numero es el mayor")