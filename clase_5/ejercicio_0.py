from data_stark import lista_personajes

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

# 1.2. Crear la función ‘definir_iniciales_nombre’ la cual recibirá como parámetro:
# ● heroe: un diccionario con los datos del personaje

# La función deberá agregar una nueva clave al diccionario recibido como
# parámetro. La clave se deberá llamar ‘iniciales’ y su valor será el obtenido de
# llamar a la función ‘extraer_iniciales’
# La función deberá validar:
# ● Que el dato recibido sea del tipo diccionario
# ● Que el diccionario contengan la clave ‘nombre’
# En caso de encontrar algún error retornar False, caso contrario retornar True

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

    #print(iniciales)
    return iniciales

def listar_iniciales(heroes):
    lista_iniciales=[]

    for heroe in heroes:

        lista_iniciales.append(extraer_iniciales(heroe["nombre"]))
    print(lista_iniciales)    


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

