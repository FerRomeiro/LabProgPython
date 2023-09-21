from data_stark import lista_personajes
#1.1
def extraer_iniciales (nombre_heroe):
    iniciales = ""
    nombre_heroe = nombre_heroe.replace("the ", " ")
    nombre_heroe = nombre_heroe.replace("-", " ")
    nombre_heroe = nombre_heroe.split(" ")

    for heroe in nombre_heroe:
        if heroe == " ":
            iniciales = "N/A" 
        else: 
            iniciales += heroe[:1]
            iniciales = ".".join(iniciales)

    # print(iniciales)
    return iniciales

def listar_iniciales(heroes):
    lista_iniciales=[]

    for heroe in heroes:
        lista_iniciales.append(extraer_iniciales(heroe["nombre"]))
        cadena=". ".join(lista_iniciales)

    print(cadena)    
#1.2

# Crear la función ‘definir_iniciales_nombre’ la cual recibirá como
# parámetro:
# heroe: un diccionario con los datos del personaje
# La función deberá agregar una nueva clave al diccionario recibido como
# parámetro. La clave se deberá llamar ‘iniciales’ y su valor será el obtenido de
# llamar a la función ‘extraer_iniciales’
# La función deberá validar:
# Que el dato recibido sea del tipo diccionario
# Que el diccionario contengan la clave ‘nombre’
# En caso de encontrar algún error retornar False, caso contrario retornar True

def definir_inciales_nombre(heroe):
    
    if type(heroe) is not dict:
        return False
    if "nombre" not in heroe:
        return False
    
    heroe["iniciales"] = extraer_iniciales(heroe["nombre"])

    return True

# 1.3. Crear la función ‘agregar_iniciales_nombre’ la cual recibirá como
# parámetro:
# lista_heroes: lista de personajes
# Se deberá validar:
# Que lista_heroes sea del tipo lista
# Que la lista contenga al menos un elemento
# La función deberá iterar la lista_heroes pasándole cada héroe a la función
# definir_iniciales_nombre.
# En caso que la función definir_iniciales_nombre() retorne False entonces se
# deberá detener la iteración e informar por pantalla el siguiente mensaje:
#  ‘El origen de datos no contiene el formato correcto’
# La función deberá devolver True en caso de haber finalizado con éxito o False
# en caso de que haya ocurrido un error

def agregar_inciales_nombre(lista_heroes):

    if type(lista_heroes) is not list:
        return False
    elif len(lista_heroes) == 0:
        return False
    else: 
        for heroes in lista_heroes:
            if not definir_inciales_nombre(heroes):
                print("El origen de datos no contiene el formato correcto")
                return False
        return True

# 1.4 Crear la función ‘stark_imprimir_nombres_con_iniciales’ la cual recibirá
# como parámetro:
# lista_heroes: la lista de personajes
# La función deberá utilizar la función agregar_iniciales_nombre’ para añadirle
# las iniciales a los diccionarios contenidos en la lista_heroes
# Luego deberá imprimir la lista completa de los nombres de los personajes
# seguido de las iniciales encerradas entre paréntesis ()
# Se deberá validar:
# Que lista_heroes sea del tipo lista
# Que la lista contenga al menos un elemento
# Delante de cada nombre se deberá agregar un asterisco ‘*’ (de forma de
# viñeta) seguido de un espacio.
# Ejemplo de salida:
# * Howard the Duck (H.D.)
# * Rocket Raccoon (R.R.) …
# La función no retorna nada
def stark_imprimir_nombres_con_iniciales(lista_heroes):

    if type(lista_heroes) != list:
        return
    elif len(lista_heroes) == 0:
        return
    else:
        if agregar_inciales_nombre(lista_heroes):
            for heroes in lista_heroes:
                nombre = heroes["nombre"]
                iniciales = heroes["iniciales"]
                print("*{}{}".format(nombre,iniciales))

# 2.1. Crear la función ‘generar_codigo_heroe’ la cual recibirá como
# parámetros:
# id_heroe: un entero que representa el identificador del héroe.
# NOTA: el valor de id_heroe lo vamos a generar recién el punto
# 2.3. Para probar la función podes pasarle cualquier enterogenero_heroe: un string que representa el género del héroe ( puede
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
# El identificador del héroe sea numérico.
# El género no se encuentre vacío y este dentro de los valores esperados
# (‘M’, ‘F’ o ‘NB’)
# En caso de no pasar las validaciones retornar ‘N/A’. En caso de verificarse
# correctamente retornar el código generado 

def generar_codigo_heroe(id_heroe, enterogenero_heroe):

    if type(id_heroe) != int or (enterogenero_heroe != "M" or enterogenero_heroe != "F" or enterogenero_heroe != "NB"):
        return "N/A"
    
    codigo = f"{enterogenero_heroe}-{str(id_heroe).zfill(8)}" #USAMOS STR PARA PASAR EL ID_HEROE A STRING O CADENA YA Q ZFILL SOLO FUNCA CON CADENAS
                                                            #zfill le manda 8 ceros a la izq de la cadena id_heroe
    if len(codigo)>10:
        return "N/A"
    
    return codigo

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

def agregar_codigo_heroe(heroe,id_heroe):
    if type(heroe) != dict or not heroe: # not heroe verifica que heroe del tipo dict no este vacio tmb puedo usar el bool(heroe)
        return False
    if type(id_heroe) != int:
        return False
    
    heroe["codigo_heroe"] = generar_codigo_heroe(id_heroe)

    if len(heroe["codigo_heroe"])!=10:
        return False
    
    return True

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

def stark_generar_codigos_heroes(lista_heroes):

    for personajes in range(1,len(lista_heroes)):
        



def menu():

    print("1. opcion 1 ")
    print("2. opcion 2")
    print("3. opcion 3")
    print("4. opcion 4")
    print("5. salir")

    opcion = input("Eliga una opcion: ")

    return opcion

continuar = True

while continuar:

    opciones = menu()

    match opciones:
        case "1":

            # extraer_iniciales(lista_personajes)
            listar_iniciales(lista_personajes)
            #print("Eligio opcion 1")
            input("Presione una tecla para continuar")
        case "2":
            #print("Eligio opcion 2")
            input("Presione una tecla para continuar")
        case "3":
            #print("Eligio opcion 3")
            input("Presione una tecla para continuar")
        case "4":
            #print("Eligio opcion 4")
            input("Presione una tecla para continuar")
        case "5":
            #print("chau")
            continuar = False

