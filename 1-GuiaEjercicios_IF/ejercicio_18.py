# Fernando Romero 
# Escribir un programa que le pida al usuario que ingrese un número entero,
# y luego imprima "El número es par y es múltiplo de 3" si el número es par y
# es múltiplo de 3, o "El número no cumple ninguna de las dos condiciones" 
# si el número no cumple ninguna de las dos condiciones.

numero = input("ingrese un numero entero: ")
numero_ingresado = int(numero)

if numero_ingresado % 2 == 0 and numero_ingresado % 3 == 0:
    print("El numero es par y multiplo de 3")
elif numero_ingresado % 2 != 0 and numero_ingresado % 3 != 0:
    print("El numero no es par ni multiplo de 3")