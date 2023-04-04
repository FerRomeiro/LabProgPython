'''
Fernando Romero

Ejercicio 2:
Pedir una edad. Informar si la persona 
es mayor de edad (más de 18 años),
adolescente (entre 13 y 17 años) o niño (menor a 13 años).
'''

edad = input("ingrese edad: ")
edad = int(edad)

#PREGUNTAR AL PROFE PARA VALIDAR QUE SOLO NUMEROS O SOLO LETRA
# #edad_ingresada = int(edad)
# while(edad.isalpha()):
#     edad = input("Error, reingrese edad: ")
#     #edad_ingresada = int(edad)


if edad>18:
    print("es mayor de edad")
elif edad>12 and edad<18:
    print("es adolescente")
else:
    print("es un niño")

