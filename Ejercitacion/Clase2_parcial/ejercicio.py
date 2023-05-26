import re

from copy import deepcopy 

#Se tiene la siguiente lista de diccionario:
#lista_diccionario = [{"nombre":"Martillo","precio":{"sin iva":1500.00,"con_iva":0.00}},
#{"nombre":"Pinza","precio":{"sin_iva":1250.00,"con_iva":0.00}},
#{"nombre":"Destornillador","precio":{"sin_iva":1050.00,"con_iva":0.00}},
#{"nombre":"Pala","precio":{"sin_iva":6250.00,"con_iva":0.00}},
#{"nombre":"Pico","precio":{"sin_iva":1450.00,"con_iva":0.00}}
#]

#Hacer una copia deep copy y trabajar con la copia, de acuerdo a lo siguiente:

#Debera mapear al precio con iva sumando al 21% sobre el precio sin iva
#Mostrar los datos por pantalla
#Modificar el nombre Destornillador por Destonillar Philips
#Mostrar datos por pantalla
#Agregar una herramiento con sus respectivos datos
#Mostrar datos
#Eliminar dos herramientas que no sean las primeras ni la ultimas y agregarlas a una lista de herramientas eliminadas
#Mostrar los datos

#Mostrar los datos de la lista original, la lista trabajada y la lista de herramientas eliminadas

lista_diccionario = [{"nombre":"Martillo","precio":{"sin_iva":1500.00,"con_iva":0.00}},
{"nombre":"Pinza","precio":{"sin_iva":1250.00,"con_iva":0.00}},
{"nombre":"Destornillador","precio":{"sin_iva":1050.00,"con_iva":0.00}},
{"nombre":"Pala","precio":{"sin_iva":6250.00,"con_iva":0.00}},
{"nombre":"Pico","precio":{"sin_iva":1450.00,"con_iva":0.00}}
]

copia=deepcopy(lista_diccionario)

def calcular_iva(diccionario):

    precio_con_iva=diccionario["precio"]["sin_iva"]+diccionario["precio"]["sin_iva"]*21/100
    diccionario["precio"]["con_iva"]=precio_con_iva
    return diccionario

copia_actualizada=list(map(calcular_iva,copia))

print(copia_actualizada)

for diccionario in copia_actualizada:
    if diccionario["nombre"]=="Destornillador":
        diccionario.update({"nombre":"Destornillador Philips"})
    break

print(copia_actualizada)

copia_actualizada.append({"nombre":"Pinza pico de loro","precio":{"sin_iva":2000.00,"con_iva":0.00}})
copia_actualizada=list(map(calcular_iva,copia_actualizada))

herramientas_eliminadas=[]

for herramienta in range(2):
    herramientas_eliminadas.append(copia_actualizada.pop(-2)) #LE PASAMOS -2 PORQUE NO HAY QUE BORRAR NI EL PRIMERO NI EL ULTIMO ESTE SERIA EL ANTEULTIMO
                                                                #PODRIA SER TRANQUILAMENTE -3-4 3 4 5 MENOS -1 O 1 PORQUE NO TIENEN Q SER PRIMERO NI ULTIMO
print(f"lista original:{lista_diccionario}")
print(f"lista modificada:{copia_actualizada}")
print(f"lista Herramientas descartadas:{herramientas_eliminadas}")
