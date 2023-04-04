# Fernando Romero
# Escribir un programa que le pida al usuario que ingrese su edad, 
# y luego imprima "Eres mayor de edad" 
# si la edad es mayor o igual a 18, o "Eres menor de edad" si la edad es menor a 18.

numero = input("Ingrese su edad: ")
numero_ingresado = int(numero)

if numero_ingresado >= 18:
    print("Eres mayor edad")
else:
    print("Eres menor de edad")