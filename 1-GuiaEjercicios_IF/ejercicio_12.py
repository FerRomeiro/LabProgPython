# Fernando Romero
# Escribir un programa que le pida al usuario que ingrese dos números enteros,
# y luego imprima "El primer número es positivo" si el primer número es mayor que cero,
# "El segundo número es positivo" si el segundo número es mayor que cero,
# o "Ambos números son negativos" si los dos números son negativos.

numero_Uno = input("Ingrese el primer numero: ")
numero_Ingresado = int(numero_Uno)
numero_Dos = input("Ingrese el segundo numero: ")
numero_Ingresado_Segundo = int(numero_Dos)

if numero_Ingresado > 0:
    print("El primer numero es positivo")
elif numero_Ingresado_Segundo > 0:
    print("El segundo numero es mayor a 0")
else:
    print("Ambos numeros son negativos")