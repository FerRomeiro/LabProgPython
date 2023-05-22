import json
import re 
import csv


def parse_json(nombre_archivo:str)->list:

    archivo=open(nombre_archivo,"r")
    lista=json.load(archivo)["juegos"]
    archivo.close()

    return lista

def mostrar_menu(lista:list):

    for elemento in lista:
        print(elemento)

def elegir_opcion(rango_min:int, rango_max:int)->int:

    patron = r'^[{}-{}]$'.format(rango_min, rango_max)

    while True:
        numero = input("Elija una opcion ({}-{}): ".format(rango_min, rango_max))

        if re.match(patron, numero):
            return int(numero)

        print("Número inválido. Ingresa nuevamente.")

def main():


    juegos=parse_json("parcial_programacion\data_pp.json")
    lista_opciones_menu=["----------------------------------------------------------------------------------------",
                    "1. Listar por pantalla los juegos cuyo género no contenga la palabra “pelea”",
                    "2. Calcular y mostrar la cantidad de juegos de una década determinada, la misma será ingresada por el usuario por pantalla.",
                    "3. Listar los juegos ordenados por Empresa. Preguntar al usuario si lo quiere ordenar de manera ascendente (‘asc’) o descendente („desc‟).",
                    "4. Buscar juegos por modo [multijugador, cooperativo] y listar en consola los que cumplan dicha búsqueda.",
                    "5. Exportar a CSV la lista de juegos según opción 1 o 3.",
                    "6. Salir",
                    "----------------------------------------------------------------------------------------"]


    opcion=0

    while opcion!=6:

        mostrar_menu(lista_opciones_menu)
        opcion=elegir_opcion(1,6)
        match opcion:
            case 1:
                opcion_juegos_pelea=lista_pelea(juegos)
                print(len(opcion_juegos_pelea))
                # print(opcion)
            case 2:
                print(juegos_decada(juegos))
            case 3:
                opcion_juegos_empresas=juegos_ordenados_empresas(juegos,"empresa")
                # print(opcion)
            case 4:
                print(juegos_modo(juegos))
            case 5:
                while True:
                    exportar=input("Eliga la opcion que quiere exportar a csv (1 o 3): ")
                    
                    if re.match("^(1|3)$",exportar):
                        exportar=int(exportar)
                        match exportar:
                            case 1:
                                exportar_a_csv(opcion_juegos_pelea,"parcial_programacion\juegos.csv")
                            case 3:
                                exportar_a_csv(opcion_juegos_empresas,"parcial_programacion\juegos.csv")
                    else:
                        print("ingrese opcion valida")
            case 6:
                print("CHAU")



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
    # print(type(decada))
    patron=r"^[34567]"
    resultado=re.search(patron,decada)
    # print(resultado)

    while decada.isalpha()==True or resultado != None:
        print("VALOR INCORRECTO")
        decada=input("Ingrese una decada 80/90/00/10/20: ")
        patron=r"^[34567]"
        resultado=re.search(patron,decada)

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

def exportar_a_csv(lista, nombre_archivo):

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

# def guardar_csv(nombre_archivo:str,lista:list):
        
#     archivo=open(nombre_archivo,"w") 

#     for juegos in lista:

#         linea = str(juegos["id"]) + "," + juegos["nombre"] + "," +juegos["plataforma"] + ","+juegos["modo"] + ","+juegos["empresa"] + ","+str(juegos["anio"]) + ","+juegos["pais"] + ","+juegos["genero"]+"\n"

#         archivo.write(linea)

#     archivo.close()



main()
