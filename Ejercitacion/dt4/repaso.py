from data_stark import lista_personajes
import re


# 1.1. Crear la función ‘extraer_iniciales’ que recibirá como parámetro:
# ● nombre_heroe: un string con el nombre del personaje
# La función deberá devolver a partir del parámetro recibido un nuevo string con
# las iniciales del nombre del personaje seguidos por un punto (.)
# ● En el caso que el nombre del personaje contenga el artículo ‘the’ se
# deberá omitir de las iniciales
# ● Se deberá verificar si el nombre contiene un guión ‘-’ y sólo en el caso
# que lo tenga se deberá reemplazar por un espacio en blanco
# La función deberá validar:
# ● Que el string recibido no se encuentre vacío
# Devolver ‘N/A’ en caso de no cumplirse la validación
# Ejemplo de la salida de la función para Howard the Duck:
# H.D.


def listar_iniciales_mia(lista):

    heroes_iniciales=[]

    for heroe in lista:
        inicial=heroe["nombre"]
        sin_the=inicial.replace("the"," ")
        inicial_split=sin_the.split()

        inicial_cadena_vacia=""
        for palabras in inicial_split:
            inicial_cadena_vacia=inicial_cadena_vacia + palabras[:1] + "." ## [0] PRIMER CARACTER [:1] PRIMER CARACTER, ES LO MISMO
            # inicial_cadena_vacia=inicial_cadena_vacia + palabras[0] + "."
        heroes_iniciales.append(inicial_cadena_vacia + " ")
        resultado="".join(heroes_iniciales)

    return resultado

def extraer_iniciales_mia(heroe:str)->str:

    if len(heroe) == 0:
        retorno =  "N/A"
    else:
        c=""
        iniciales=heroe.replace("the"," ")
        inicial_split=iniciales.split()
        # inicial_split=re.findall("[A-Z]",heroe)
        
        for inicial in inicial_split:
            c=c+inicial[0]+"."
        retorno=c
    return retorno

# def extraer_iniciales_mia(heroe):

#     if len(heroe) == 0:
#         retorno =  "N/A"
#     else:
#         c=""

#         inicial_split=re.findall("[A-Z]",heroe)
        
#         for inicial in inicial_split:
#             c=c+inicial+"."
#         retorno=c
#     return retorno

# 1.2. Crear la función ‘definir_iniciales_nombre’ la cual recibirá como parámetro:
# ● heroe: un diccionario con los datos del personaje
# La función deberá agregar una nueva clave al diccionario recibido como
# parámetro. La clave se deberá llamar ‘iniciales’ y su valor será el obtenido de
# llamar a la función ‘extraer_iniciales’
# La función deberá validar:
# ● Que el dato recibido sea del tipo diccionario
# ● Que el diccionario contengan la clave ‘nombre’
# En caso de encontrar algún error retornar False, caso contrario retornar True


def definir_iniciales_nombre_mia(heroes:dict)->bool:

    retorno = False
    if type(heroes) == dict: #VALIDACION 
        if "nombre" in heroes.keys():  # VALIDACION
            # print("esta dentro")
            heroes["iniciales"] = extraer_iniciales_mia(heroes["nombre"]) # 
            retorno=True
    # for i, heroe in enumerate(heroes):
    #     heroes[i] = {"nombre": heroe, "iniciales": extraer_iniciales_mia(heroe["nombre"])}

    return retorno

# 1.3. Crear la función ‘agregar_iniciales_nombre’ la cual recibirá como
# parámetro:
# ● lista_heroes: lista de personajes
# Se deberá validar:
# ● Que lista_heroes sea del tipo lista
# ● Que la lista contenga al menos un elemento
# La función deberá iterar la lista_heroes pasándole cada héroe a la función
# definir_iniciales_nombre.
# En caso que la función definir_iniciales_nombre() retorne False entonces se
# deberá detener la iteración e informar por pantalla el siguiente mensaje:
# ‘El origen de datos no contiene el formato correcto’
# La función deberá devolver True en caso de haber finalizado con éxito o False
# en caso de que haya ocurrido un error


def agregar_iniciales_nombre(lista_heroes:list)->bool:

    retorno = False

    if type(lista_heroes) == list:
        if len(lista_heroes) > 0:
            retorno=True
            for heroe in lista_heroes:
                resultado =  definir_iniciales_nombre_mia(heroe)
                if resultado == False:
                    print("El origen de datos no contiene el formato correcto")
                    retorno=False
                    break
    return retorno

# 1.3. Crear la función ‘stark_imprimir_nombres_con_iniciales’ la cual recibirá
# como parámetro:
# ● lista_heroes: la lista de personajes
# La función deberá utilizar la función agregar_iniciales_nombre’ para añadirle
# las iniciales a los diccionarios contenidos en la lista_heroes
# Luego deberá imprimir la lista completa de los nombres de los personajes
# seguido de las iniciales encerradas entre paréntesis ()
# Se deberá validar:
# ● Que lista_heroes sea del tipo lista
# ● Que la lista contenga al menos un elemento
# Delante de cada nombre se deberá agregar un asterisco ‘*’ (de forma de
# viñeta) seguido de un espacio.
# Ejemplo de salida:
# * Howard the Duck (H.D.)
# * Rocket Raccoon (R.R.)
# ...
# La función no retorna nada
    # for heroes in lista_heroes:
    #     definir_iniciales_nombre_mia(heroes)
    #     return True
def stark_imprimir_nombres_con_iniciales(lista_heroes:list):
    
    if type(lista_heroes) == list and len(lista_heroes) > 0:

        agregar_iniciales_nombre(lista_heroes)

        for heroe in lista_heroes:
            # print(heroe["nombre"] + heroe["iniciales"])
            print(f"{heroe['nombre']} ({heroe['iniciales']})")

# 2.1. Crear la función ‘generar_codigo_heroe’ la cual recibirá como
# parámetros:
# ● id_heroe: un entero que representa el identificador del héroe.
# ○ NOTA: el valor de id_heroe lo vamos a generar recién el punto
# 2.3. Para probar la función podes pasarle cualquier entero
# ● genero_heroe: un string que representa el género del héroe ( puede
# tomar los valores ‘M’, ‘F’ o ‘NB’)
# La función deberá generar un string con el siguiente formato:

# GENERO-000…000ID
# Es decir, el género recibido por parámetro seguido de un ‘-’ (guión) y por
# último el identificador recibido. Todos los códigos generados deben tener
# como máximo 10 caracteres (contando todos los caracteres, inclusive el
# guión). Se deberá completar con ceros para que todos queden del mismo
# largo
# Algunos ejemplos:
# F-00000001
# M-00000002
# NB-0000010
# La función deberá validar:
# ● El identificador del héroe sea numérico.
# ● El género no se encuentre vacío y este dentro de los valores esperados
# (‘M’, ‘F’ o ‘NB’)
# En caso de no pasar las validaciones retornar ‘N/A’. En caso de verificarse
# correctamente retornar el código generado


def generar_codigo_heroe(id_heroe:int,genero_heroe:str)->str:

    retorno = False

    if genero_heroe == "M" or genero_heroe == "F" or genero_heroe=="NB" or len(genero_heroe) == 0 and id_heroe.isalnum():
        if genero_heroe == "NB":
            print(f"{genero_heroe}-{str(id_heroe).zfill(7)}") #zfill solo funca con str y no con int, pasarlo siempre a str 
        if genero_heroe == "M" or "F":
            print(f"{genero_heroe}-{str(id_heroe).zfill(8)}") #zfill solo funca con str y no con int, pasarlo siempre a str 
        # id=id_heroe
        # id_con_ceros=str(id).zfill(10)
        retorno=True
    else:

        retorno="N/A"

    return retorno

# 2.2. Crear la función ‘agregar_codigo_heroe’ la cual recibirá como
# parámetro:
# ● heroe: un diccionario con los datos del personaje
# ● id_heroe: un entero que representa el identificador del héroe.
# ○ NOTA: el valor de id_heroe lo vamos a generar recién el punto
# 2.3. Para probar la función podes pasarle cualquier entero
# La función deberá agregar una nueva clave llamada ‘codigo_heroe’ al
# diccionario ‘heroe’ recibido como parámetro y asignarle como valor un código
# utilizando la función ‘generar_codigo_heroe’

# La función deberá validar:
# ● Que el diccionario recibido como parámetro no se encuentre vacío.
# ● Que el código recibido mediante generar_codigo_heroe tenga
# exactamente 10 caracteres
# En caso de pasar las validaciones correctamente la función deberá retornar
# True, en caso de encontrarse un error retornar False

def agregar_codigo_heroe(heroe:dict,id_heroe:int)->bool:

    retorno=False

    if len(heroe) > 0 :
        heroe["codigo heroe"] = generar_codigo_heroe(id_heroe,heroe["genero"])
        # if len(resultado) == 10:
        retorno=True 

    return retorno

# 2.3. Crear la función ‘stark_generar_codigos_heroes’ la cual recibirá como
# parámetro:
# ● lista_heroes: la lista de personajes
# La función deberá iterar la lista de personajes y agregarle el código a cada
# uno de los personajes.
# El código del héroe (id_heore) surge de la posición del mismo dentro de la
# lista_heroes (comenzando por el 1).
# Reutilizar la función agregar_codigo_heroe pasándole como argumentos el
# héroe que se está iterando y el id_heroe
# Una vez finalizado imprimir por pantalla un mensaje como el siguiente:
# (## representa la cantidad de códigos generados):
# Se asignaron ## códigos
# * El código del primer héroe es: M-00000001
# * El código del del último héroe es: M-00001224
# La función deberá validar::
# ● La lista contenga al menos un elemento
# ● Todos los elementos de la lista sean del tipo diccionario

# ● Todos los elementos contengan la clave ‘genero’
# En caso de encontrar algún error, informar por pantalla: ‘El origen de datos no
# contiene el formato correcto’
# La función no retorna ningún valor.

def stark_generar_codigos_heroes(lista_heroes:list):
    
    for heroe in lista_personajes:
        agregar_codigo_heroe(heroe["nombre"],enumerate(lista_heroes))
        resultado = len(lista_personajes)
        print(f"Se asignaron {resultado} codigos:")

def menu():

    print("opcion 1")
    print("opcion 2")
    print("opcion 3")
    print("opcion 4")
    print("opcion 5")
    print("opcion 6")
    print("opcion 7")
    print("opcion 8")
    print("opcion 9")

    opcion=input("eliga una opcion: ")

    return opcion


continuar=True

while continuar:

    opcion=menu()
    
    match opcion:
 
        case "1":
            # print("opcion1")
            # e=extraer_iniciales(lista_personajes)
            # print(e)
            e=listar_iniciales_mia(lista_personajes)
            print(e)
        case "2":
            e=extraer_iniciales_mia("Howard the Duck")
            print(e)
            # for personaje in lista_personajes:
            #     p=definir_iniciales_nombre(personaje)
            # print(p)
        case "3":
            # l=listar_iniciales(lista_personajes)
                resultado=definir_iniciales_nombre_mia(lista_personajes[0])
                print(lista_personajes[0])
                print(resultado)
        case "4":
            a=agregar_iniciales_nombre(lista_personajes)
            print(a)
            print(lista_personajes)
        case "5":
            stark_imprimir_nombres_con_iniciales(lista_personajes)
            print("opcion1")
        case "6":
            # c=generar_codigo_heroe("12","M")
            # if len(c) == 10:
            #     print(c)
            print("opcion1")
        case "7":
            # a=agregar_codigo_heroe(lista_personajes[0],"54")
            print("asd")
        case "8":
            stark_generar_codigos_heroes(lista_personajes)
            # print("opcion1")
        case "9":
            print("chau")
            continuar=False
