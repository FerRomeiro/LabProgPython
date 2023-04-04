# Fernando Romero
# Escribir un programa que le pida al usuario que ingrese su nombre y su edad,
# y luego imprima "Puedes votar" si la edad es mayor o igual a 18 y menor o igual a 65, 
# o "No puedes votar" si la edad es menor a 18 o mayor a 65.

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
edad_ingresada = int(edad)

if edad_ingresada >= 18 and edad_ingresada <= 65:
    print("Puedes votar")
else:
    print("No puedes votar")