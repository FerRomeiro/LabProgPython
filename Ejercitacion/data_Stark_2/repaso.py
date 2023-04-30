from dt6.data_stark import lista_personajes

# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
def imprimir_personajes(lista):
    lista_heroes=[]
    for heroes in lista:
        lista_heroes.append(heroes["nombre"])
    
    return lista_heroes
# C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
def imprimir_altura_heroe(lista):
    alturas=[]

    for personaje in lista:
        nombre=personaje["nombre"]
        if "altura" in personaje: #SI LA CLAVE altura ES UNA CLAVE DEL DICCIONARIO personaje osea lista osea lista_personajes
            altura=personaje["altura"]
        else:
            altura="desconocida"
        alturas.append((nombre,altura)) #CREE UNA TUPLA (nombre,altura) QUE SON VARIABLES PARA AGREGAR A LA LISTA alturas=[]

    return alturas
#  D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
def heroe_mas_alto(lista):
    heroe_mas_alto=None
    mas_alto=0
    for heroe in lista:
        if "altura" in heroe: #SI LA CLAVE altura ES UNA CLAVE DEL DICCIONARIO heroe
            altura=float(heroe["altura"])
            if altura>mas_alto:
                mas_alto=altura
                heroe_mas_alto=heroe["nombre"]

    return heroe_mas_alto
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
def heroe_petiso(lista):
    heroe_mas_bajo=None
    altura_baja=float("inf") #ESTO ES CLAVE PARA DARLE UN VALOR GRANDE Y ASEGURARNOS QUE CUALQUIER ALTURA SEA MAS BAJA QUE ESTA VARIABLE
                            #REPRESENTA EL INFINITO POSITIVO
    for heroe in lista:
        if "altura" in heroe:
            altura=float(heroe["altura"])
            if altura<altura_baja:
                altura_baja=altura
                heroe_mas_bajo=heroe["nombre"]
    return heroe_mas_bajo
# F. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
def promedio_altura(lista):
    acumulador=0
    contador=0
    for heroes in lista:
        if "altura" in heroes:
            altura=float(heroes["altura"])
            acumulador=acumulador+altura
            contador=contador+1
        promedio=acumulador/contador

    return promedio

# G. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)


# H. Calcular e informar cual es el superhéroe más y menos pesado.
def mas_menos_pesado(lista):

    mas_pesado=0
    menos_pesado=float("inf")
    

    for heroes in lista:
        if "peso" in heroes:
            peso=float(heroes["peso"])
            if peso>mas_pesado:
                mas_pesado=float(heroes["peso"])
                nombre_mas_peso=heroes["nombre"]
            if peso<menos_pesado:
                menos_pesado=float(heroes["peso"])
                nombre_menos_peso=heroes["nombre"]

    mensaje=print("El mas pesado es:{0} Y el menos pesado es: {1}".format(nombre_mas_peso,nombre_menos_peso))
    return mensaje

# I. Ordenar el código implementando una función para cada uno de los valores informados.



def menu():

    print("1")
    print("2")
    print("3")
    print("4")
    print("5")
    print("6")
    print("7")
    print("8")
    print("9")
    print("10")

    opcion=input("eliga opcion: ")
    
    return opcion

continuar=True

while continuar:

    opcion_elegida=menu()

    match opcion_elegida:
        case "1":
            # print("Imprimir personajes")
            p=imprimir_personajes(lista_personajes)
            print(p)
            input("Presione tecla para continuar...")
        case "2":
            a=imprimir_altura_heroe(lista_personajes)
            print(a)
            input("Presione tecla para continuar...")
        case "3":
            # print("opcion 3")
            h=heroe_mas_alto(lista_personajes)
            print(h)
            input("Presione tecla para continuar...")
        case "4":
            # print("opcion 4")
            bajo=heroe_petiso(lista_personajes)
            print(bajo)
            input("Presione tecla para continuar...")
        case "5":
            # print("opcion 5")
            a=promedio_altura(lista_personajes)
            print(a)
            input("Presione tecla para continuar...")
        case "6":
            # print("opcion 6")
            m=mas_menos_pesado(lista_personajes)
            print(m)
            input("Presione tecla para continuar...")
        case "7":
            print("opcion 7")
            input("Presione tecla para continuar...")
        case "8":
            print("opcion 8")
            input("Presione tecla para continuar...")
        case "9":
            print("opcion 9")
            input("Presione tecla para continuar...")
        case "10":
            print("opcion 10")
            continuar=False
