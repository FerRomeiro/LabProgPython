# Fernando Romero
# Escribir un programa que le pida al usuario que ingrese dos números enteros,
# y luego imprima "Los dos números son iguales" si los dos números son iguales, 
# "El primer número es mayor" si el primer número es mayor que el segundo,
# o "El segundo número es mayor" si el segundo número es mayor que el primero.

numero_uno = input("ingrese el primero numero: ")
numero_Ingresado_Uno = int(numero_uno)
numero_Dos = input("Ingrese el segundo numero: ")
numero_Ingresado_Dos = int(numero_Dos)

if numero_Ingresado_Uno == numero_Ingresado_Dos:
    print("Los numeros son iguales")
elif numero_Ingresado_Uno > numero_Ingresado_Dos:
    print("El primer numero es el mayor")
else:
    print("El segundo numero es el mayor")