import json
import re

# 1.4. Crear la función 'leer_archivo' la cual recibirá por parámetro un string
# que indicará el nombre y extensión del archivo a leer (Ejemplo:
# archivo.json). Dicho archivo se abrirá en modo lectura únicamente y
# retornará la lista de héroes como una lista de diccionarios.

def parse_json_stark(nombre_archivo:str)->list:
    dic_json={}
    #para trabajar con archivos debo abrirlo, hay dos formas:
    # with open(nombre_archivo,"r") as archivo: #r porque es modo lectura
    archivo=open(nombre_archivo,"r") # otra manera de abrir el archivo es asignarle a una variable
    dic_json=json.load(archivo) #nos devuelve lo que hay adentro del json que es este caso es un diccionario 
                                # archivo es una variable del tipo file 
    archivo.close() #cierro el archivo
    return dic_json["heroes"] #le pasamos la clave y nos devuelve ese diccionario 

lista_heroes=parse_json_stark("archivos/data_stark.json") #nos traemos la lista que es lo que nos devuelve la funcion y printeo 
print(lista_heroes) #nos devuelve una lista 

# Crear la función 'guardar_archivo' la cual recibirá por parámetro un
# string que indicará el nombre con el cual se guardará el archivo junto
# con su extensión (ejemplo: 'archivo.csv') y como segundo parámetro
# tendrá un string el cual será el contenido a guardar en dicho archivo.
# Debe abrirse el archivo en modo escritura+, ya que en caso de no
# existir, lo creara y en caso de existir, lo va a sobreescribir La función
# debera retornar True si no hubo errores, caso contrario False, además
# en caso de éxito, deberá imprimir un mensaje respetando el formato:
# .Se creó el archivo: nombre_archivo.csv
# En caso de retornar False, el mensaje deberá decir: ‘Error al crear el
# archivo: nombre_archivo’

def guardar_csv_stark(nombre_archivo,lista:list):
    #para trabajar con archivos primero debo abrirlo 
    archivo=open(nombre_archivo,"w") # En este caso quiero empezar a escribir en un archivo asi que uso W y no R
    #quiero escribir los datos de cada uno de los heroes 
    for heroe in lista:
        linea = heroe["nombre"] + "," + heroe["identidad"] + "," +heroe["empresa"] + ","+str(heroe["altura"]) + ","+str(heroe["peso"]) + ","+heroe["genero"] + ","+heroe["color_ojos"] + ","+heroe["color_pelo"] + ","+str(heroe["fuerza"]) + ","+heroe["inteligencia"]+"\n"
        #ahora quiero escribir la linea
        archivo.write(linea)
        #ahora cierro el archivo
    archivo.close()

guardar_csv_stark("archivos/data_stark.csv",lista_heroes) ## CREAMOS ASI data_stark.csv

##ahora vamos a suponer en caso que yo no tenga la lista y yo quiera sacarla de un csv
#CREO UNA FUNCION QUE LEA EL ARCHIVO csv Y ME DEVUELVA LA lista de heroes
def parse_csv_stark(nombre_archivo:str)->list:
    lista_heroes=[] #creamos una lista de heroes vacia para appendear un diccionario que en este caso serian cada uno de los heroes
    archivo=open(nombre_archivo,"r")
    #itero sobre el archivo para acceder a cada una de las lineas
    for linea in archivo:#recorro cada linea del archivo
        #los datos del csv estan separados por comas, uso el split() para que me devuelva una lista de palabras
        heroe={} #creo un diccionario vacio
        lista=linea.split(",") #separamos con una coma cada uno de los valores para q se transforme en una lista cada uno de los valores
    #asigno cada una de las claves a sus respectivos valores, a los elementos de la lista de csv accedo a traves del indice, el primero es el nombre osea [0]
        heroe["nombre"]=lista[0]
        heroe["identidad"]=lista[1]
        heroe["empresa"]=lista[2]
        heroe["altura"]=float(lista[3])
        heroe["peso"]=float(lista[4])
        heroe["genero"]=lista[5]
        heroe["color_ojos"]=lista[6]
        heroe["color_pelo"]=lista[7]
        heroe["fuerza"]=int(lista[8])
        heroe["inteligencia"]=re.sub("\n","",lista[9]) #ELIMINAMOS EL \n EL RESUB ES EL REPLACE DE EXPRESIONES REGULARES Y EL REPLACE ES EL DE STRING
        lista_heroes.append(heroe)
    archivo.close()#cerramos el archivo
    return lista_heroes


lista_heroes_stark=parse_csv_stark("archivos/data_stark.csv")
print(lista_heroes_stark)

