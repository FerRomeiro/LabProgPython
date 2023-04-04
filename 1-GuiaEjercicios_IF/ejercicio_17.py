# Fernando Romero
# Escribir un programa que le pida al usuario que ingrese un número entero, 
# y luego imprima "El número es negativo" si el número es menor que cero,
# "El número es cero" si el número es igual a cero, o "El número es positivo" 
# si el número es mayor que cero.

numero = input("Ingrese un numero: ")
numero_ingresado = int(numero)

if numero_ingresado > 0:
    print("el numero es mayor a 0")
elif numero_ingresado == 0:
    print("El numero es 0")
else:
    print("El numero es menor a 0")