#ESTE ES UN PROBLEMA QUE PASO UN COMPAÑERO YA HECHO NO SE VIO EN CLASE, LO PASO EN EL GRUPO DE WP EL 17/05/23

from copy import deepcopy

# """
# Se tiene la siguiente lista de diccionarios:
# lista_diccionario = [{'nombre' : 'Martillo','precio': {'sin_iva': 1500.00,'con_iva':0.00}},
# {'nombre' : 'Pinza','precio': {'sin_iva': 1250.00,'con_iva':0.00}},
# {'nombre' : 'Destornillador','precio': {'sin_iva': 1050.00,'con_iva':0.00}},
# {'nombre' : 'Pala','precio': {'sin_iva': 6250.00,'con_iva':0.00}},
# {'nombre' : 'Pico','precio': {'sin_iva': 1450.00,'con_iva':0.00}}
# ]

# Hacer una copia deep copy y trabajar con la copia, de acuerdo a lo siguiente:

# De debra mapear al precio con iva, sumando el 21% sobre el precio sin iva.
# Mostrar los datos por pantalla.
# Modificar el nombre de Destornillador por Destornillador Philips.
# Mostrar los datos por pantalla.
# Agregar una herramienta con sus respectivos datos.
# Mostrar los datos.
# Eliminar dos herramientas que no sean ni la primera ni la ultima y agregarlas a una lista de herramientas eliminadas.
# Mostrar los datos.

# Mostrar los datos de la lista original, la lista trabajada y la lista de herramientas eliminadas.

# """

lista_diccionario = [{'nombre' : 'Martillo','precio': {'sin_iva': 1500.00,'con_iva':0.00}},
{'nombre' : 'Pinza','precio': {'sin_iva': 1250.00,'con_iva':0.00}},
{'nombre' : 'Destornillador','precio': {'sin_iva': 1050.00,'con_iva':0.00}},
{'nombre' : 'Pala','precio': {'sin_iva': 6250.00,'con_iva':0.00}},
{'nombre' : 'Pico','precio': {'sin_iva': 1450.00,'con_iva':0.00}}]

copia = deepcopy(lista_diccionario)

def calcular_iva(diccionario):

    precio_con_iva = diccionario['precio']['sin_iva'] + diccionario['precio']['sin_iva'] * 21/100
    diccionario['precio']['con_iva'] = precio_con_iva
    return diccionario

copia_actualizada = list(map(calcular_iva, copia))

print(copia_actualizada)

for diccionario in copia_actualizada:
    if diccionario['nombre'] == 'Destornillador':
        diccionario.update({'nombre': 'Destornillador Philips'})
        break

print(copia_actualizada)

copia_actualizada.append({'nombre' : 'Pinza pico de loro','precio': {'sin_iva': 2000.00,'con_iva':0.00}})
copia_actualizada = list(map(calcular_iva, copia_actualizada))

herramientas_eliminadas = []

for herramienta in range(2):
    herramientas_eliminadas.append(copia_actualizada.pop(-2))

print(f'Lista original: {lista_diccionario}')
print(f'Lista modificada: {copia_actualizada}')
print(f'Lista herramientas descartadas: {herramientas_eliminadas}') 