import json
import re

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
    # patron=r"[a-Za-z]"
    # resultado=re.search(patron,valor)

    # if resultado:
    #     print("Dato invalido")
        # valor=input("ingrese la cantidad de heroes que quiere listar: ")

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




def clave_heroes()->str:
    
    clave=input("Ingrese el promedio que quiere sacar: ")

    return clave


def calcular_promedio(lista:list)->float:

    # clave=input("Ingrese el promedio que quiere sacar: ")
    clave=clave_heroes()
    acumulador=0
    contador=0

    for i in range(len(lista)):
        
        acumulador=acumulador+float(lista[i][clave])
        contador=contador+1
    
    promedio=acumulador/contador

    return promedio

def mayor_menor_promedio(lista:list,clave:str)->list:

    promedio=calcular_promedio(lista_aux)
    valor=input("Calculas el menor/mayor??: ")
    lista_heroes=[]

    for i in  range(len(lista_aux)):
        heroe_clave=float(lista_aux[i][clave])

        if valor=="menor":
            if heroe_clave < promedio:
                lista_heroes.append(lista[i]["nombre"])
        elif valor=="mayor":
            if heroe_clave > promedio:
                lista_heroes.append(lista[i]["nombre"]) 
    
    print(lista_heroes)

# 5. Buscar héroes por inteligencia [good, average, high] y listar en consola los
# que cumplan dicha búsqueda. (Usando RegEx)

def patron_heroes()->str:
    
    patron=input("Escriba tipo de inteligencia que desea buscar[good, average, high]: ")

    return patron


def heroes_inteligencia(lista:list):
    
    lista_heroes=[]
    patron=patron_heroes()

    for i in range(len(lista)):
        # patron="good"

        cadena=lista[i]["inteligencia"]
        resultado=re.match(patron,cadena)
        # print(resultado)
        if resultado:
            lista_heroes.append(lista[i]["nombre"])
            
    
    print(lista_heroes)


# Exportar a CSV la lista de héroes ordenada según opción elegida
# anteriormente [1-4]


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



def menu():

    print("1. Listar los primeros N héroes.")
    print("2. Ordenar y Listar héroes por altura.")
    print("3. Ordenar y Listar héroes por fuerza.")
    print("4. Calcular promedio de cualquier key numérica.")
    print("5. Buscar héroes por inteligencia [good, average, high].")
    print("6. Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente [1-4]")
    print("7. Exit")
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
            # print("opcion1")
            # calcular_promedio(lista_heroes)
            mayor_menor_promedio(lista_aux,"fuerza")
            input("Presione una tecla para continuar...")
        case "5":
            heroes_inteligencia(lista_aux)
        case "6":
            guardar_csv_stark("repaso/data_stark.csv",lista_aux)
        case "7":
            print("Chau")
            continuar=False
    