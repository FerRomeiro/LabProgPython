'''
Fernando Romero

Ejercicio 4:

Pedir una edad y un estado civil, si la edad es menor a 18 años y el estado civil
distinto a "Soltero", mostrar el siguiente mensaje: 'Es muy pequeño para NO
ser soltero.'
'''

edad = input("ingresar edad: ")
edad_ingresada = int(edad)
estado_Civil = input("ingrese estado civil: ")

if estado_Civil != "Soltero" and edad_ingresada < 18:
    print("Es muy pequeño para no ser soltero")
