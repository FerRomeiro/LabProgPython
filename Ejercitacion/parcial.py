import json


#creo una funcion para acceder al json
def parseo_json(stark:str)->list:

    archivo=open(stark,"r")
    diccionario=json.load(archivo)["heroes"]
    archivo.close()

    return diccionario

lista_heroes=parseo_json("repaso\stark.json")

lista_aux=lista_heroes


# print(lista_heroes)
# print(lista_heroes[0])s

# 1. Listar los primeros N héroes. El valor de N será ingresado por el usuario
# (Validar que no supere max. de lista)

def cantidad_heroes()->int:

    valor=input("ingrese la cantidad de heroes que quiere listar: ")

    return valor


def listar(lista:list):

    numero=int(cantidad_heroes())
    # numero=int(input("ingrese la cantidad de heroes que quiere listar: "))

    if numero < len(lista):
        lista_hero=[]
        # print()
        for i in range(numero):
            if numero < len(lista):
                heroe=lista[i]["nombre"]
                lista_hero.append(heroe)
    
    elif numero>len(lista):
        lista_hero=("NO HAY TANTOS HEROES")


    return lista_hero

# heroes=listar(lista_heroes)
# print(heroes)


# 2. Ordenar y Listar héroes por altura. Preguntar al usuario si lo quiere ordenar de
# manera ascendente (‘asc’) o descendente (‘desc’)

def manera_asc_desc()->str:

    pregunta=input("De que manera queres ordenarlo asc/desc: ").lower()
    while pregunta != "desc" and pregunta != "asc":
            print("VALOR INCORRECTO")
            pregunta=input("De que manera queres ordenarlo asc/desc: ").lower()

    return pregunta


def ordenar_altura(lista:list,clave:str):

    valor=manera_asc_desc()
    

    bandera_swap=True

    while bandera_swap:
        bandera_swap=False
        for i in range(len(lista)-1): 
            if valor=="asc":
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

    return lista_aux

def normalizar_flotantes(lista:list,clave:str):

    for i in lista:
        i[clave]=float(i[clave])





# normalizar_flotantes(lista_aux,"altura")
# print(ordenar_altura(lista_aux,"altura"))

# 3. Ordenar y Listar héroes por fuerza. Preguntar al usuario si lo quiere ordenar
# de manera ascendente (‘asc’) o descendente (‘desc’)

def normalizar_int(lista:list,clave:str):

    for i in lista:
        i[clave]=int(i[clave])

def ordenar_fuerza(lista:list,clave:str)->list:

    orden=manera_asc_desc()

    bandera_swap=True

    while bandera_swap:
        bandera_swap=False
        for i in range(len(lista)-1): 
            if orden=="asc":
                if lista[i][clave]>lista[i+1][clave]:
                    aux=lista[i]
                    lista[i]=lista[i+1]
                    lista[i+1]=aux
                    bandera_swap=True
            elif orden=="desc":
                if lista[i][clave]<lista[i+1][clave]:
                    aux=lista[i]
                    lista[i]=lista[i+1]
                    lista[i+1]=aux
                    bandera_swap=True

    return lista_aux





def menu():

    print("1. Listar los primeros N héroes.")
    print("2. Ordenar y Listar héroes por altura.")
    print("3. Ordenar y Listar héroes por fuerza.")
    print("4")
    print("5")

    opcion=input("Eliga una opcion: ")

    return opcion


continuar=True

while continuar:

    opcion=menu()

    match opcion:
        case "1":
            # print("Listar los primeros N héroes.")
            heroes=listar(lista_aux)
            print(heroes)
            input("Presione una tecla para continuar...")
        case "2":
            # print("Ordenar y Listar héroes por altura.")
            normalizar_flotantes(lista_aux,"altura")
            print(ordenar_altura(lista_aux,"altura"))
            input("Presione una tecla para continuar...")
        case "3":
            normalizar_int(lista_aux,"fuerza")
            orden=ordenar_fuerza(lista_aux,"fuerza")
            print(orden)
            input("Presione una tecla para continuar...")
        case "4":
            print("opcion1")
            input("Presione una tecla para continuar...")
        case "5":
            print("Chau")
            continuar=False
    