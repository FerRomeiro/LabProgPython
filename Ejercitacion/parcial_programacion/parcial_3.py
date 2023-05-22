import re
import json
import csv



def json_heroes(nombre_archivo:str)->list:
    
    archivo=open(nombre_archivo,"r")
    lista=json.load(archivo)["heroes"]
    archivo.close()

    return lista

def mostar_menu(lista:list):

    for opciones in lista:
        print(opciones)

def opciones(min:int,max:int): #ES DE DOBLE FILO PORQUE SI INGRESO COMO MAX UN NUMERO DE MAS DE 1 DIGITO NO ME SIRVE, PARA CHEQUEAR Y PROBAR
                                #PROBARRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
    
    patron=r"^[{}-{}$]".format(min,max)

    while True:
        opcion_elegida=input("Ingrese una opcion ({0}-{1}) :".format(min,max))
        if re.match(patron,opcion_elegida):
            return int(opcion_elegida)
        else:
            print("Opcion incorrecta, reingrese una opcion valida entre {}-{}".format(min,max))

def cantidad_heroes()->int:
    patron=r"^([1-9]|1[0-9]|2[0-9])$"

    while True:
        numero_heroes=str(input("ingrese la cantidad de heroes que desea listar entre 1-24: "))
        if re.match(patron,numero_heroes) and numero_heroes<="24":
            return int(numero_heroes)
        else:
            print("NUMERO INVALIDO, REINGRESE UN NUMERO ENTRE 1-24")


def heroes_ingresados(lista:list)->list:

    heroes=cantidad_heroes()
    # print(heroes)
    lista_heroes=[]

    for i in range(heroes):    
        lista_heroes.append(lista[i]["nombre"])

    return lista_heroes


def manera_asc_desc()->str:

    pregunta=input("De que manera queres ordenarlo asc/desc: ").lower()
    while pregunta != "desc" and pregunta != "asc":
            print("VALOR INCORRECTO")
            pregunta=input("De que manera queres ordenarlo asc/desc: ").lower()

    return pregunta

def heroes_altura(lista_aux:list,clave:str)->list:

    valor=manera_asc_desc()
    bandera_swap=True
    
    while bandera_swap:

        bandera_swap=False

        for i in range(len(lista_aux)-1):
            if valor=="asc":
                if lista_aux[i][clave]>lista_aux[i+1][clave]:
                    aux=lista_aux[i]
                    lista_aux[i]=lista_aux[i+1]
                    lista_aux[i+1]=aux
                    bandera_swap=True
            elif valor=="desc":
                if lista_aux[i][clave]<lista_aux[i+1][clave]:
                    aux=lista_aux[i]
                    lista_aux[i]=lista_aux[i+1]
                    lista_aux[i+1]=aux
                    bandera_swap=True

    return lista_aux

# def heroes_altura(lista:list, clave:str, tipo:int):
#     bandera_swap = True
#     while bandera_swap == True: 
#         bandera_swap = False 
#         for i in range(len(lista)-1):
#             if (tipo == 1 and lista[i][clave] > lista[i+1][clave]) or (tipo == 2 and lista[i][clave] < lista[i+1][clave]):
#                     aux = lista[i]
#                     lista[i] = lista[i+1]
#                     lista[i+1] = aux
#                     bandera_swap = True

    # return lista

    #     lista=[]
    #     for i in range(len(lista_aux)):
    #         lista.append(lista_aux[i]["altura"])



    # return lista


def heroes_fuerza(lista:list,clave:str)->list:

    valor=manera_asc_desc()
    bandera_swap=True

    while bandera_swap:
        bandera_swap=False
        for i in range(len(lista)-1):
            if valor == "asc":
                if lista[i][clave]>lista[i+1][clave]:
                    aux=lista[i]
                    lista[i]=lista[i+1]
                    lista[i+1]=aux
                    bandera_swap=True
            elif valor=="desc":
                if lista[i][clave]<lista[i+1][clave]:
                    aux=lista[i]
                    lista[i]=lista[i+1]
                    lista[i+1]=aux
                    bandera_swap=True                

    return lista


def promedio_heroes(lista:list,key:str):

    # key=input("Escriba una key numerica: ")
    valor=input("Desea calcular los heroes que sean menor o mayor al promedio: ")
    acumulador_key=0
    contador=0
    for i in lista:
        acumulador_key+=int(i[key])
        contador+=1

    promedio=acumulador_key/contador
    print(promedio)
    lista_heroes=[]
        
    for j in lista:
        if float(j[key]) > promedio and valor == "mayor":
            lista_heroes.append(j["nombre"])
        if float(j[key]) < promedio and valor == "menor":
            lista_heroes.append(j["nombre"])
        
    
    return lista_heroes


def heroes_inteligencia(lista:list):

    inteligencia=(set(x["inteligencia"] for x in lista))
    diccionario_inteligencia={}
    for k in inteligencia:
        diccionario_inteligencia[k] = []

    for i in inteligencia:
        for j in lista:
            if i == j["inteligencia"]:
                diccionario_inteligencia["{0}".format(i)]+=j["nombre"]
    


    print(diccionario_inteligencia)





def menu():

    lista_opciones=["1)Listar los primeros N héroes. El valor de N será ingresado por el usuario(Validar que no supere max. de lista)",
                    "2)Ordenar y Listar héroes por altura. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)",
                    "3)Ordenar y Listar héroes por fuerza. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente (‘desc’)",
                    "4)Calcular promedio de cualquier key numérica, filtrar los que cumplan con la condición de superar o no el promedio (preguntar al usuario la condición:  ‘menor’ o ‘mayor’) se deberá listar en consola aquellos que cumplan con ser mayores o menores según corresponda.",
                    "5) Buscar héroes por inteligencia [good, average, high] y listar en consola los que cumplan dicha búsqueda. (Usando RegEx)",
                    "6)Exit"]
    opcion=0
    lista_heroes=json_heroes("parcial_programacion\data_stark.json")
    copia_lista_heroes=lista_heroes.copy()

    while opcion!=6:
        mostar_menu(lista_opciones)
        opcion=opciones(1,6)

        match opcion:
            case 1:
                lista_heroes_ingresados=heroes_ingresados(copia_lista_heroes)
                print(lista_heroes_ingresados)
            case 2:
                # lista_heroes_altura=heroes_altura(copia_lista_heroes,"altura",1)
                lista_heroes_altura=heroes_altura(copia_lista_heroes,"altura")
                print(lista_heroes_altura)
            case 3:
                lista_heroes_fuerza=heroes_fuerza(copia_lista_heroes,"fuerza")
                print(lista_heroes_fuerza)
            case 4:
                print(promedio_heroes(copia_lista_heroes,"fuerza"))
            case 5:
                print(heroes_inteligencia(copia_lista_heroes))

menu()
