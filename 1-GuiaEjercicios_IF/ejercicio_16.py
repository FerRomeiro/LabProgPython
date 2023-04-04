# Fernando Romero
# Escribir un programa que le pida al usuario que ingrese su nombre y su edad,
# y luego imprima "Eres adolescente" si la edad está entre 13 y 17 inclusive, 
# "Eres adulto" si la edad está entre 18 y 64 inclusive,
# o "Eres adulto mayor" si la edad es mayor o igual a 65.

nombre = input("Ingrese el nombre: ")
edad = input("Ingrese edad: ")
edad_ingresada = int(edad)

if edad_ingresada >= 13 and edad_ingresada <=17:
    print("Eres adolescente")
elif edad_ingresada >= 18 and edad_ingresada <= 64:
    print("Eres adulto")
else:
    print("Eres adulto mayor")