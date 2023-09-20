    # CLASE 1
# Ejercicio 1:
# Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su
# sueldo para esa persona.

nombre = input("Ingrese el nombre: ")
sueldo = input("Ingrese el sueldo: ")

sueldo_ingresado = float(sueldo)

if sueldo_ingresado > 0:

    sueldo_aumentado = sueldo_ingresado + sueldo_ingresado*10/100
    sueldo_aumentado = str(sueldo_aumentado)
    sueldo_ingresado = str(sueldo_ingresado)

    print("El sueldo de la persona " + nombre + " es de $" + sueldo_ingresado + " con 10% de aumento es $" + sueldo_aumentado)

else: 
    print("El sueldo es invalido")





