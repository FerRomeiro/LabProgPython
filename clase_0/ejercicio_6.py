'''
Pedir números hasta que el USUARIO QUIERA e informar la suma acumulada y el promedio.
'''

respuesta = "y"
contador_numero = 0
numeros_totales = 0

while (respuesta == "y"):
    numero = input("ingrese un numero: ")
    numero = int(numero);
    
    numeros_totales = numero + numeros_totales
    contador_numero += 1

    respuesta = input("Desea continuar?? y/n: ")

promedio = numeros_totales / contador_numero
promedio=str(promedio)
numeros_totales=str(numeros_totales)

print("El promedio es: " + promedio)
print("La suma acumulada es: " + numeros_totales)


#ESTA FORMA ESTA PIOLA 

flag_numero = True
contador = 0
suma = 0

while flag_numero:
    numero = input("Ingrese un numero: ")
    if  numero != "":
        numero = int(numero)
        suma += numero
        contador+=1
    else:
        flag_numero = False

promedio = suma / contador
mensaje = "La suma es: {0}, y el promedio es de: {1}". format (suma, promedio)
print(mensaje)