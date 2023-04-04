# Fernando Romero
# Escribir un programa que le pida al usuario que ingrese su edad,
# y luego imprima "Eres un niño" si la edad es menor a 12, "Eres un adolescente"
# si la edad está entre 12 y 17 inclusive, 
# "Eres un adulto" si la edad está entre 18 y 64

edad = input("Ingrese su edad: ")
edad_ingresada = int(edad)

if edad_ingresada < 12:
    print("Eres un niño")
elif edad_ingresada > 11 and edad_ingresada <= 17:
    print("Eres un adolescente")
else:
    print("Eres un adulto")