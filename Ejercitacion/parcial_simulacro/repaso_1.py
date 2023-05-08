import json
import re

#creo una funcion para acceder al json
def parseo_json(stark:str)->list:

    archivo=open(stark,"r")
    diccionario=json.load(archivo)["heroes"]
    archivo.close()

    return diccionario

lista_heroes=parseo_json("repaso\stark.json")

lista_aux=lista_heroes.copy()


def cantidad_heroes(mensaje:str)->int:

    
    valor=input(mensaje)
    # patron=r"[A-Za-z]"
    patron=r"[0-9]"
    resultado=re.search(patron,valor)
    print(resultado)

    while resultado == None:

        print("Dato invalido")
        valor=input(mensaje)
        resultado=re.search(patron,valor)
        
    
    return valor

def listar(lista:list)->list:

    numero=int(cantidad_heroes("ingrese la cantidad de heroes que quiere listar: "))
    # numero=int(input("ingrese la cantidad de heroes que quiere listar: "))

    if numero < len(lista):
        lista_hero=[]
        # print()
        for i in range(numero):
            if numero < len(lista):
                lista_hero.append(lista[i])
                
    
    elif numero>len(lista):
        lista_hero=("NO HAY TANTOS HEROES")

    return lista_hero


def guardar_csv_stark(nombre_archivo,lista:list):
    #para trabajar con archivos primero debo abrirlo 
    archivo=open(nombre_archivo,"w") # En este caso quiero empezar a escribir en un archivo asi que uso W y no R
    #quiero escribir los datos de cada uno de los heroes 
    for heroe in lista:
        # print(heroe)
        linea = heroe["nombre"] + "," + heroe["identidad"] + "," +heroe["empresa"] + ","+str(heroe["altura"]) + ","+str(heroe["peso"]) + ","+heroe["genero"] + ","+heroe["color_ojos"] + ","+heroe["color_pelo"] + ","+str(heroe["fuerza"]) + ","+str(heroe["inteligencia"])+"\n"
        #ahora quiero escribir la linea
        # print(linea)
        archivo.write(linea)
        #ahora cierro el archivo
    archivo.close()

def menu():

    print("1. Listar los primeros N héroes.")
    print("2.Ordenar")
    print("3. Exportar a CSV la lista de héroes ordenada según opción elegida anteriormente")
    opcion=input("Eliga una opcion: ")

    return opcion


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

continuar=True

while continuar:

    opcion=menu()

    match opcion:
        case "1":
            # print("Listar los primeros N héroes.")
            lista_heroes_reducida=listar(lista_aux)         
            print(lista_heroes_reducida)
            input("Presione una tecla para continuar...")
        case "2":
            # print("Ordenar y Listar héroes por altura.")
            normalizar_flotantes(lista_aux,"altura")
            lista_heroes_ordenada=ordenar_altura(lista_aux,"altura")
            print(lista_heroes_ordenada)
            input("Presione una tecla para continuar...")
            # print(ordenar_altura(lista_aux,"altura"))
        case "3":
            guardar_csv_stark("parcial_simulacro\data_stark.csv",lista_heroes_reducida)            
            guardar_csv_stark("parcial_simulacro\data_stark_ordenada.csv",lista_heroes_ordenada)