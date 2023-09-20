# Ejercicio 2:
# Pedir una edad. Informar si la persona es mayor de edad (más de 18 años),
# adolescente (entre 13 y 17 años) o niño (menor a 13 años).

edad = input("Ingrese edad: ")
edad = int(edad)

if edad > 0:

    if edad > 18:
        print("Es mayor de edad")
    elif edad >= 13:
        print("Es adolescente")
    elif edad < 13:
        print("Es un niño")
else: 
    print("Edad invalida")