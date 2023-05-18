import json
import re 

def menu():

    print("1) Listar por pantalla los juegos cuyo género no contenga la palabra “pelea”")
    print("2) Calcular y mostrar la cantidad de juegos de una década determinada")
    print("3) Listar los juegos ordenados por Empresa")
    print("4) Buscar juegos por modo [multijugador, cooperativo]")
    print("5) Exportar a CSV la lista de juegos según opción 1 o 3")
    print("6) Exit")

    opcion=input("ingrese una opcion: ")

    return opcion

def main():


    juegos=parse_json("parcial_programacion\data_pp.json")

    continuar=True

    while continuar:

        opcion=menu()

        match opcion:
            case "1":
                opcion_juegos=lista_pelea(juegos)
                print(len(opcion_juegos))
                # print(opcion)
            case "2":
                print(juegos_decada(juegos))
            case "3":
                opcion_juegos=juegos_ordenados_empresas(juegos,"empresa")
                # print(opcion)
            case "4":
                print(juegos_modo(juegos))
            case "5":
                guardar_csv("parcial_programacion\juegos.csv",opcion_juegos)    
            case "6":
                continuar=False
                print("CHAU")


def parse_json(nombre_archivo:str)->list:

    archivo=open(nombre_archivo,"r")
    lista=json.load(archivo)["juegos"]
    archivo.close()

    return lista

# 1) Listar por pantalla los juegos cuyo género no contenga la palabra “pelea”.
def lista_pelea(lista_juegos:list)->list:
    lista=[]

    if len(lista_juegos) > 0 and type(lista_juegos) == list:
        
        for juegos in range(len(lista_juegos)):
            patron=r"pelea".capitalize()
            genero=lista_juegos[juegos]["genero"]
            resultado=re.search(patron,genero)

            if resultado == None:
                lista.append(lista_juegos[juegos])



    #ESTA OPCION ME LISTA LOS JUEGOS PERO SOLO POR NOMBRE
        # for juegos in lista_juegos:
        #     patron=r"pelea".capitalize()
        #     genero=juegos["genero"]
        #     resultado=re.search(patron,genero)

        #     if resultado == None:
        #         lista.append(juegos["nombre"])


    # print(len(lista))
    # print(lista) 
    return lista

# 2) Calcular y mostrar la cantidad de juegos de una década determinada, la misma será
# ingresada por el usuario por pantalla.

def decada_ingresada()->str:

    decada=input("Ingrese una decada 80/90/00/10/20: ")

    return decada

def juegos_decada(lista_juegos:list)->int:

    decada=decada_ingresada()
    decada=decada[0]
    cantidad_juegos=0

    for juegos in range(len(lista_juegos)):
        # print(lista_juegos[juegos]["anio"][0])

        if int(lista_juegos[juegos]["anio"][2]) == int(decada):
            cantidad_juegos=cantidad_juegos+1

    # print(type(cantidad_juegos))

    return cantidad_juegos


# 3) Listar los juegos ordenados por Empresa. Preguntar al usuario si lo quiere ordenar de
# manera ascendente (‘asc’) o descendente („desc‟).

def manera_asc_desc()->str:

    pregunta=input("De que manera queres ordenarlo asc/desc: ").lower()
    while pregunta != "desc" and pregunta != "asc":
            print("VALOR INCORRECTO")
            pregunta=input("De que manera queres ordenarlo asc/desc: ").lower()

    return pregunta


def juegos_ordenados_empresas(lista_aux:list,clave:str)->list:

    valor=manera_asc_desc()
    bandera_swap=True
    
    while bandera_swap:

        bandera_swap=False

        for i in range(len(lista_aux)-1):
            if valor=="asc":
                if lista_aux[i][clave]>lista_aux[i+1][clave]:
                    aux=lista_aux[i]
                    lista_aux[i]=lista_aux[i+1]
                    lista_aux[i+1]=aux
                    bandera_swap=True
            elif valor=="desc":
                if lista_aux[i][clave]<lista_aux[i+1][clave]:
                    aux=lista_aux[i]
                    lista_aux[i]=lista_aux[i+1]
                    lista_aux[i+1]=aux
                    bandera_swap=True
        
    return lista_aux

# 4) Buscar juegos por modo [multijugador, cooperativo] y listar en consola los que cumplan
# dicha búsqueda. (Usando RegEx).

def juegos_modo(lista_juegos:list)->list:

    lista=[]

    for juegos in range(len(lista_juegos)):
        patron_uno="multijugador"
        patron_dos="cooperativo"
        modo=lista_juegos[juegos]["modo"]
        resultado_uno=re.search(patron_uno,modo)
        resultado_dos=re.search(patron_dos,modo)

        if resultado_uno:
            lista.append(lista_juegos[juegos]["nombre"])
        if resultado_dos:
            lista.append(lista_juegos[juegos]["nombre"])

    return lista
        
# 5) Exportar a CSV la lista de juegos según opción 1 o 3.

def guardar_csv(nombre_archivo:str,lista:list):
        
    archivo=open(nombre_archivo,"w") 

    for juegos in lista:

        linea = str(juegos["id"]) + "," + juegos["nombre"] + "," +juegos["plataforma"] + ","+juegos["modo"] + ","+juegos["empresa"] + ","+str(juegos["anio"]) + ","+juegos["pais"] + ","+juegos["genero"]+"\n"

        archivo.write(linea)

    archivo.close()



main()
