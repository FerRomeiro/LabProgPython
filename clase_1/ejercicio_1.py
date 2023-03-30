'''
Ejercicio 1:
Pedir el nombre y el sueldo, 
incrementarle un 10% e informar el aumento de su
sueldo para esa persona.
'''
nombre = input("ingrese un nombre: ")

sueldo = input("ingrese el sueldo: ") 
sueldo = int(sueldo)

incremento = (sueldo * 10) /100

sueldo_Final = sueldo + incremento
sueldo_Final = str(sueldo_Final)
print("Nombre es:" + nombre + " y su sueldo: " + sueldo_Final)