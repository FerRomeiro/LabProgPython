from dt6.data_stark import lista_personajes
import re

def menu():
    print("opcion1")
    print("opcion2")
    print("opcion3")
    print("opcion4")
    print("opcion5")
    print("opcion6")
    print("opcion7")
    print("opcion8")
    print("opcion9")
    print("opcion10")
    opcion=input("ingrese opcion: ")
    return opcion

# 5.1. Crear la función ‘convertir_cm_a_mtrs’ la cual recibirá como parámetro:
# ● valor_cm: Un número que representa una medida en centímetros
# La función deberá retornar el número recibido, pero convertido a la unidad
# metros. La función deberá validar que el número recibido sea un número
# flotante positivo, en caso de no serlo retornar -1

def convertir_cm_a_mtrs(valor_cm:int)->float:
    

    if float(valor_cm)>0: 
        numero=valor_cm
        metro=100.00
        retorno=float(numero)/metro
    else:
        retorno="-1"

    return retorno 

# 5.2. Crear la función ‘generar_separador’ la cual recibirá como parámetro
# ● patron: un carácter que se utilizará como patrón para generar el
# separador
# ● largo: un número que representa la cantidad de caracteres que va
# ocupar el separador.
# ● imprimir: un parámetro opcional del tipo booleano (por default definir
# en True)
# La función deberá generar un string que contenga el patrón especificado
# repitiendo tantas veces como la cantidad recibida como parámetro (uno junto
# al otro, sin salto de línea)
# Si el parámetro booleano recibido se encuentra en False se deberá solo
# retornar el separador generado. Si se encuentra en True antes de retornarlo,
# imprimirlo por pantalla
# La función deberá validar:
# ● Que el parámetro patrón tenga al menos un carácter y como máximo
# dos
# ● Que el parámetro largo sea un entero entre 1 y 235 inclusive
# En caso de no verificarse las validaciones devolver ‘N/A’
# Ejemplo de llamada:
# generar_separador(‘*’, 10)
# Ejemplo de salida:
# **********

def generar_separado(patron:str,largo:int,imprimir:bool=True):

    if len(patron)>0 and len(patron)<3:
        if largo>0 and largo<235 and imprimir==True:
            retorno=patron*largo
            print(retorno)
        else:
            retorno=patron
    else:
        retorno="N/A"

    return retorno

# 5.3. Crear la función ‘generar_encabezado’ la cual recibirá como parámetro

# ● titulo: un string que representa el título de una sección de la ficha
# La función deberá devolver un string que contenga el título envuelto entre dos
# separadores (estimar el largo requerido para tu pantalla).
# Ejemplo de salida:
# ********************************************************************************
# PRINCIPAL
# ********************************************************************************
# La función deberá convertir el titulo recibido en todas letras mayúsculas

def generar_encabezado(titulo:str)->str:

    retorno = titulo.upper()
    generar_separado("*",100)
    print(retorno)
    generar_separado("*",100)

# 5.4. Crear la función ‘imprimir_ficha_heroe’ la cual recibirá como parámetro:
# ● heroe: un diccionario con los datos del héroe
# La función deberá a partir los datos del héroe generar un string con el
# siguiente formato e imprimirlo por pantalla::
# ***************************************************************************************
# PRINCIPAL
# ***************************************************************************************
# NOMBRE DEL HÉROE: Spider-Man (S.M.)
# IDENTIDAD SECRETA: Peter Parker
# CONSULTORA: Marvel Comics
# CÓDIGO DE HÉROE : M-00000001
# ***************************************************************************************
# FISICO
# ***************************************************************************************

# ALTURA: 1,78 Mtrs.
# PESO: 74,25 Kg.
# FUERZA: 55 N
# ***************************************************************************************
# SEÑAS PARTICULARES
# ***************************************************************************************
# COLOR DE OJOS: Hazel
# COLOR DE PELO: Brown
def imprimir_ficha_heroe(heroe:dict):

    nombre=heroe["nombre"]
    identidad=heroe["identidad"]
    altura=heroe["altura"]
    peso=heroe["peso"]
    fuerza=heroe["fuerza"]
    color_ojos=heroe["color_ojos"]
    color_pelo=heroe["color_pelo"]

    generar_encabezado("principal")
    print((f"Nombre del heroe:{nombre}"))
    print((f"Identidad:{identidad}"))
    generar_encabezado("fisico")
    print(f"Fuerza:{fuerza}")
    print(f"Altura:{altura}")
    print(f"Peso:{peso}")
    generar_encabezado("señas particulares")
    print(f"Color de ojos:{color_ojos}")
    print(f"Color de pelo:{color_pelo}")

# 5.5. Crear la función 'stark_navegar_fichas’ la cual recibirá como parámetros:
# ● lista_heroes: la listas personajes
# La función deberá comenzar imprimiendo la ficha del primer personaje de la
# lista y luego solicitar al usuario que ingrese alguna de las siguientes opciones:
# [ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir
# ● Si el usuario ingresa ‘1’: se debe mostrar el héroe que se encuentra en
# la posición anterior en la lista (en caso de estar en el primero, ir al
# último)

# ● Si el usuario ingresa ‘2’: se debe mostrar el héroe que se encuentra en
# la posición siguiente en la lista (en caso de estar en el último, ir al
# primero)

# ● Si ingresa ‘S’: volver al menú principal

# ● Si ingresa cualquier otro valor, volver a mostrar las opciones hasta que
# ingrese un valor válido


def stark_navegar_fichas(lista_heroes:list):
    
    imprimir_ficha_heroe(lista_personajes[0])

    opcion=input("ingrese opcion 1 para ir a la izq. o opcion 2 para ir a las derecha o opcion S para salir")

    if opcion=="1":
        imprimir_ficha_heroe(lista_personajes[-1])
    elif opcion=="2":
        imprimir_ficha_heroe(lista_personajes[1])
    elif opcion.tolower()=="s":
        imprimir_ficha_heroe(lista_personajes[0])
    else:
        print("ingrese un valor valido")




continuar=True

while continuar:
    opcion=menu()
    match opcion:
        case "1":
            m=convertir_cm_a_mtrs("1232")
            print(f"{m} metros")
        case "2":
            c=generar_separado("aa",91)
            print(c)
        case "3":
            generar_encabezado("jeejeje")
            # print("1")
        case "4":
            imprimir_ficha_heroe(lista_personajes[0])
            # print("1")
        case "5":
            stark_navegar_fichas(lista_personajes)
            # print("1")
        case "6":
            print("1")
        case "7":
            print("1")
        case "8":
            print("1")
        case "9":
            print("1")
        case "10":
            print("1")
