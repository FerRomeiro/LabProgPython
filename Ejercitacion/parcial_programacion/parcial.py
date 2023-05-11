import json
import re 

def menu():
    print("opcion1")
    print("opcion2")
    print("opcion3")
    print("opcion4")
    print("opcion5")
    print("opcion6")

    opcion=input("ingrese opcion: ")

    return opcion


def parseo_json(nombre_archivo:str)->list:

    archivo=open(nombre_archivo,"r")
    diccionario=json.load(archivo)["juegos"]
    archivo.close()

    return diccionario

# print(type(lista_aux))
# print(lista_aux)

# 1) Listar por pantalla los juegos cuyo género no contenga la palabra “pelea”.

# def lista_no_pelea(lista_juegos:list)->list:
#     lista=[]
#     if len(lista_juegos)>0:

#         for juegos in lista_juegos:
#             genero=juegos["genero"]
#             # nombre=juegos["nombre"]
#             # print(nombre)

#             patron="Pelea"

#             if re.search(patron,genero)==None:
#                 # lista.append(str(juegos["id"]) + "," + juegos["nombre"] + "," +juegos["plataforma"] + ","+juegos["modo"] + ","+juegos["empresa"] + ","+str(juegos["anio"]) + ","+juegos["pais"] + ","+juegos["genero"]+"\n")
#                 lista.append()
#         # print(lista)
#         print(len(lista))
#         print(type(lista))
#     return lista


def lista_no_pelea(lista_juegos:list)->list:
    lista=[]
    if len(lista_juegos)>0:

        for juegos in range(len(lista_juegos)):
            # print(lista_juegos)
            genero=lista_juegos[juegos]["genero"]
            # print(genero)
            patron="Pelea"
            if re.search(patron,genero)==None:
                lista.append(lista_juegos[juegos])
    print(len(lista))
    return lista


# 2) Calcular y mostrar la cantidad de juegos de una década determinada, la misma será
# ingresada por el usuario por pantalla.

def decada(mensaje:str):
    valor=input(mensaje)
    patron=r"[1,0,8,9]"
    resultado=re.search(patron,valor[0])
    # patron_dos=r"[1-9]"
    # resultado_dos=re.search(patron_dos,valor[1])
    # print(resultado_dos)
    
    if valor[2] != "0":

        while resultado == None or len(valor)>2:

            print("Dato invalido")
            valor=input(mensaje)
            resultado=re.search(patron,valor)
        
    
    return valor


def decada_juegos(lista_aux:list):
    
    numero=str(decada("Ingrese una decada valida (80/90/00/10): "))
    # numero=[]
    # numero.append(numero_decada)
    # print(type(numero))

    numero=list(numero)
    # print(type(numero))
    # print(numero[2])
    numero=numero[2]
    print(numero)
    lista_valor=[]
    contador=0

    for ano in range(len(lista_aux)):
        deca=lista_aux[ano]["anio"]
        print(numero)
        # print(deca)
        deca=deca[2]
        print(deca)
        # valor=deca+"0"
        # print(valor)
        if deca == numero :
            contador=contador+1

    lista_valor.append("Los juegos de la decada "+str(numero)+"0 son: "+str(contador))

    print(lista_valor)
            
        







    # for decada in lista_aux:
    #     anio=decada["anio"]




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

def buscar_juego_multijugador_coopetativo(lista_auxiliar:list):

    lista=[]
    # patron="[multijugador","cooperativo]"

    for juegos in range(len(lista_auxiliar)):
        # nombre=juegos["nombre"]
        modo=lista_auxiliar[juegos]["modo"]
        patron="multijugador"
        patron_dos="cooperativo"

        if re.search(patron,modo):
                # lista.append(str(juegos["id"]) + "," + juegos["nombre"] + "," +juegos["plataforma"] + ","+juegos["modo"] + ","+juegos["empresa"] + ","+str(juegos["anio"]) + ","+juegos["pais"] + ","+juegos["genero"]+"\n")
                #                 # lista.append(str(juegos["id"]) + "," + juegos["nombre"] + "," +juegos["plataforma"] + ","+juegos["modo"] + ","+juegos["empresa"] + ","+str(juegos["anio"]) + ","+juegos["pais"] + ","+juegos["genero"]+"\n")
                lista.append(lista_auxiliar[juegos])
        elif re.search(patron_dos,modo):
                lista.append(lista_auxiliar[juegos])
    
    print(len(lista))

    return lista

# 5) Exportar a CSV la lista de juegos según opción 1 o 3.

def guardar_csv_stark(nombre_archivo,lista:list):

    archivo=open(nombre_archivo,"w") 

    for juegos in lista:

        linea = str(juegos["id"]) + "," + juegos["nombre"] + "," +juegos["plataforma"] + ","+juegos["modo"] + ","+juegos["empresa"] + ","+str(juegos["anio"]) + ","+juegos["pais"] + ","+juegos["genero"]+"\n"

        archivo.write(linea)

    archivo.close()

def main():

    lista_juegos=parseo_json("parcial_programacion\data_pp.json")
    lista_aux=lista_juegos.copy()
    continuar=True

    while continuar:

        opcion=menu()

        match opcion:
            case "1":
                # print("opcion1")
                # parseo_json("juegos")
                # print(lista_no_pelea(lista_aux))
                lista_de_juegos=lista_no_pelea(lista_aux)
                print(len(lista_de_juegos))
                # print(punto_1)
            case "2":
                decada_juegos(lista_aux)
            case "3":
                print(juegos_ordenados_empresas(lista_aux,"empresa"))      
            case "4":
                lista_de_juegos=buscar_juego_multijugador_coopetativo(lista_aux)
            case "5":
                guardar_csv_stark("parcial_programacion\juegos.csv",lista_de_juegos)




main()