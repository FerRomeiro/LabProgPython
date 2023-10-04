from dt6.data_stark import lista_personajes

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

def extraer_iniciales(nombre_heroe):
    
    # iniciales=[]

    # for heroe in nombre_heroe:
    #     name=heroe["nombre"]
    #     if not name.strip():
    #         return "N/A"
    #     nombre_sin_guion= name.replace("-","")
    #     palabra=nombre_sin_guion.split()

    #     if "The" in palabra:
    #         palabra.remove("The")
    #     iniciales.append(palabra[0][0].upper()+".")


    # return "".join(iniciales)

    # iniciales=[]

    # for heroe in nombre_heroe:
    #     name=heroe["nombre"]
    #     if not name.strip():
    #         return "N/A"
    #     nombre_sin_guion= name.replace("-","")
    #     palabras=nombre_sin_guion.split()

    #     if "the" in palabras:
    #         palabras.remove("the")
        
    #     # Agregar la primera letra de cada palabra
    #     for palabra in palabras:
    #         iniciales.append(palabra[0].upper()+".")

    # # Unir las iniciales con espacios
    # return "".join(iniciales)



    iniciales = []
    for heroe in nombre_heroe:
        name = heroe["nombre"]
        if name.strip()=="":
            return "N/A"
        nombre_sin_guion = name.replace("-", "")
        palabras = nombre_sin_guion.split()

        # Eliminar el artículo 'The' de la lista de palabras si está presente
        if 'the' in palabras:
            palabras.remove('the')

        # Crear la inicial del héroe
        inicial = ""
        for palabra in palabras:
            inicial += palabra[0].upper()+"."

        # Agregar resultado y un espacio
        iniciales.append(inicial + " ")

    # Unir las iniciales y devolverlas
    return "".join(iniciales)





# 1.2. Crear la función ‘definir_iniciales_nombre’ la cual recibirá como
# parámetro:
# ● heroe: un diccionario con los datos del personaje

# La función deberá agregar una nueva clave al diccionario recibido como
# parámetro. La clave se deberá llamar ‘iniciales’ y su valor será el obtenido de
# llamar a la función ‘extraer_iniciales’
# La función deberá validar:
# ● Que el dato recibido sea del tipo diccionario adsadasdsa
# ● Que el diccionario contengan la clave ‘nombre’
# En caso de encontrar algún error retornar False, caso contrario retornar True

def definir_iniciales_nombre(heroe):

    if "nombre" in heroe and type(heroe) == dict:
        nombre=heroe["nombre"]
        iniciales=extraer_iniciales(nombre)
        heroe["iniciales"]=iniciales
        return True
    else:
        return False



def listar_iniciales(heroes):
    lista_iniciales=[]

    for heroe in heroes:
        lista_iniciales.append(extraer_iniciales(heroe["nombre"]))
        cadena=". ".join(lista_iniciales)

    print(cadena)  













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

def extraer_iniciales_mia(heroe):

    if heroe:
        return "N/A"
    
    c=""
    iniciales=heroe.replace("the"," ")
    inicial_split=iniciales.split()

    for name in inicial_split:
        c=c+name[0]+"."

    return c


def definir_iniciales_nombre_mia(heroe):

    if "nombre" in heroe and type(heroe) == dict:
        heroe["iniciales"] = extraer_iniciales(heroe)

































































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
            for personajes in lista_personajes:
                d=definir_iniciales_nombre_mia(personajes)
            print("d")
        case "4":
            print("opcion1")
        case "5":
            print("opcion1")
        case "6":
            print("opcion1")
        case "7":
            print("opcion1")
        case "8":
            print("opcion1")
        case "9":
            print("chau")
            continuar=False
