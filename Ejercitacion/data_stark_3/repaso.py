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

        # Agregar la inicial al resultado y un espacio
        iniciales.append(inicial + " ")

    # Unir las iniciales y devolverlas
    return "".join(iniciales)




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
            e=extraer_iniciales(lista_personajes)
            print(e)
        case "2":
            print("opcion1")
        case "3":
            print("opcion1")
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
