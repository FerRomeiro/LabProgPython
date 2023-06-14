import re
import json
import csv
# Desarrollar en Python:
# Leer el archivo data_pp.json y generar una lista de diccionarios, y de acuerdo a un menú de
# opciones realizar lo siguiente:
# 1) Listar por pantalla los juegos cuyo género no contenga la palabra “pelea”.
# 2) Calcular y mostrar la cantidad de juegos de una década determinada, la misma será
# ingresada por el usuario por pantalla.
# 3) Listar los juegos ordenados por Empresa. Preguntar al usuario si lo quiere ordenar de
# manera ascendente (‘asc’) o descendente („desc‟).
# 4) Buscar juegos por modo [multijugador, cooperativo] y listar en consola los que cumplan
# dicha búsqueda. (Usando RegEx).
# 5) Exportar a CSV la lista de juegos según opción 1 o 3.
# 6) Salir.

def json_heroes(nombre_archivo:str)->list:

    archivo=open(nombre_archivo,"r")
    lista=json.load(archivo)["juegos"]
    archivo.close()

    return lista

def mostrar_opciones(lista_opciones:list)->list:
    
    for opciones in lista_opciones:
        print(opciones)

def opciones(min:int,max:int):

    patron=r"^[{}-{}]$".format(min,max)

    while True:
        opcion_elegida=input("Eliga una opcion {}-{}: ".format(min,max))
        if re.match(patron,opcion_elegida):
            return int(opcion_elegida)
        else:
            print("Opcion incorrecta, eliga una opcion valida entre {}-{}".format(min,max))

def menu():
    
    lista_opciones=["1) Listar por pantalla los juegos cuyo género no contenga la palabra “pelea”.",
                "2) Calcular y mostrar la cantidad de juegos de una década determinada, la misma será ingresada por el usuario por pantalla.",
                "3) Listar los juegos ordenados por Empresa. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente („desc‟).",
                "4) Buscar juegos por modo [multijugador, cooperativo] y listar en consola los que cumplan dicha búsqueda. (Usando RegEx).",
                "5) Exportar a CSV la lista de juegos según opción 1 o 3.",
                "6)Exit"]
    continuar=True
    lista_juegos=json_heroes("parcial_recuperatorio\data_pp.json")
    copia_lista_juegos=lista_juegos.copy()

    while continuar:
        mostrar_opciones(lista_opciones)
        opcion=opciones(1,6)

        match opcion:
            case 1:
                juegos_pelea=pelea(copia_lista_juegos)
                print(juegos_pelea)
                print(len(juegos_pelea))
            case 2:
                juegos_decada=decada(copia_lista_juegos)
                print(juegos_decada)
            case 3:
                juegos_empresas=juegos_ordenados_empresas(copia_lista_juegos,"empresa")
                print(juegos_empresas)
            case 4:
                juegos=juegos_modo(lista_juegos)
                print(juegos)
            case 5:
                opcion_exportar=input("Que lista desea exportar 1 o 3?: ")
                if re.match("^1|3$",opcion_exportar):
                    opcion_exportar=int(opcion_exportar)
                    match opcion_exportar:
                        case 1:
                            guardar_csv("parcial_recuperatorio\no_pelea.csv",juegos_pelea)
                        case 3:
                            guardar_csv("parcial_recuperatorio\empresas.csv",juegos_empresas)
                else:
                    print("OPCION INVALIDA")
            case 6:
                continuar=False
                print("chau")



# 1) Listar por pantalla los juegos cuyo género no contenga la palabra “pelea”.
def pelea(lista_juegos:list)->list:
    
    lista=[]
    for juegos in lista_juegos:
        patron=r"pelea".capitalize()
        genero=juegos["genero"]

        if re.match(patron,genero)==None:
            lista.append(juegos)
    
    return lista

# 2) Calcular y mostrar la cantidad de juegos de una década determinada, la misma será
# ingresada por el usuario por pantalla.

def numero_decada()->str:
    decada=input("Ingresa una decada 80/90/00/10/20: " )
    patron = r"^(80|90|00|10|20)$"
    
    while re.match(patron,decada)==None:
        print("ingrese una decada valida")
        decada=input("Ingresa una decada 80/90/00/10/20: " )
        patron = r"^(80|90|00|10|20)$"
    
    return decada
    

def decada(lista_juegos)->list:

    decada=int(numero_decada())
    decada_final=decada + 10
    lista=[]

    for juego in lista_juegos:
        anio=int(juego["anio"])%100

        if anio in range(decada,decada_final):
            lista.append(juego["nombre"])
    
    return lista

# 3) Listar los juegos ordenados por Empresa. Preguntar al usuario si lo quiere ordenar de
# manera ascendente (‘asc’) o descendente („desc‟).

def manera_asc_desc()->str:

    pregunta=input("De que manera queres ordenarlo asc/desc: ").lower()
    while pregunta != "desc" and pregunta != "asc":
            print("VALOR INCORRECTO")
            pregunta=input("De que manera queres ordenarlo asc/desc: ").lower()

    return pregunta


def juegos_ordenados_empresas(lista_juegos:list,clave:str)->list:

    valor=manera_asc_desc()
    bandera_swap=True
    
    while bandera_swap:

        bandera_swap=False

        for i in range(len(lista_juegos)-1):
            if valor=="asc":
                if lista_juegos[i][clave]>lista_juegos[i+1][clave]:
                    aux=lista_juegos[i]
                    lista_juegos[i]=lista_juegos[i+1]
                    lista_juegos[i+1]=aux
                    bandera_swap=True
            elif valor=="desc":
                if lista_juegos[i][clave]<lista_juegos[i+1][clave]:
                    aux=lista_juegos[i]
                    lista_juegos[i]=lista_juegos[i+1]
                    lista_juegos[i+1]=aux
                    bandera_swap=True
    
            # lista_empresas=[]
            # for i in lista_juegos:
            #     lista_empresas.append(i["empresa"])

    return lista_juegos

# 4) Buscar juegos por modo [multijugador, cooperativo] y listar en consola los que cumplan
# dicha búsqueda. (Usando RegEx).

def juegos_modo(lista_juegos:list)->list:
    lista=[]

    for juegos in lista_juegos:
        patron=r"\bmultijugador\b|\bcooperativo\b"
        modo=juegos["modo"].lower()
        if re.search(patron,modo):
            lista.append(juegos["nombre"])

    return lista

# 5) Exportar a CSV la lista de juegos según opción 1 o 3.
# def guardar_csv(nombre_archivo:str,lista_juegos:list):
        
#     archivo=open(nombre_archivo,"w") 

#     for juegos in lista_juegos:

#         linea = str(juegos["id"]) + "," + juegos["nombre"] + "," +juegos["plataforma"] + ","+juegos["modo"] + ","+juegos["empresa"] + ","+str(juegos["anio"]) + ","+juegos["pais"] + ","+juegos["genero"]+"\n"

#         archivo.write(linea)

#     archivo.close()

def guardar_csv(nombre_archivo:str,lista:list):
    if len(lista) == 0:
        print("La lista de datos está vacía.")
        return -1
    nombres_columnas = list(lista[0].keys())

    with open(nombre_archivo, "w", newline="") as archivo_csv:
        escritor_csv = csv.DictWriter(archivo_csv, fieldnames=nombres_columnas)
        escritor_csv.writeheader()

        for datos in lista:
            escritor_csv.writerow(datos)

    print(f"Los datos se han exportado exitosamente al archivo {nombre_archivo}.csv.")

menu()