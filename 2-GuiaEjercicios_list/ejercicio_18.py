# Fernando Romero
# Solicitar al
# usuario números enteros hasta que ingrese el 0. Almacenar los números en una lista 
# y luego imprimir el mayor (sin utilizar la función max())

lista=[]
bandera=False

while bandera==False:
    numero = int(input("Ingrese un numero: "))
    if numero==0:
        break

    lista.append(numero)

mayor_numero=None

for mayor in range(len(lista)):

    if bandera == False or lista[mayor] > mayor_numero:
        mayor_numero = lista[mayor] 
        bandera=True

print(lista)
print(mayor_numero)




