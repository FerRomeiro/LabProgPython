import json
import re 

def parse_json(nombre_archivo:str)->list:

    archivo=open(nombre_archivo,"r")
    diccionario=json.load(archivo)["juegos"]
    archivo.close()

    return diccionario

def menu():
    print("opcion1")
    opcion=input("ingrese opcion: ")
    return opcion




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
            # print(lista_aux[i][clave]) 
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

    lista=[]

    for i in range(len(lista_aux)):
        # print(lista_aux[i]["empresa"]) #ordenados pero repetidos
        # print(type(lista_aux)) #list
        lista.append(lista_aux[i][clave])
    # print(lista) #RETORNA LA LISTA ORDENADA, ESTA SERIA LA FORMA QUE ENCONTRE POR AHORA 
    
    lista_sin_repes=[]
    conjunto=set()

    for i in lista:
        if i not in conjunto:
            lista_sin_repes.append(i)
            conjunto.add(i)
    print(lista_sin_repes)
    print(conjunto)
    

    #     empresas=list(lista_aux[i]["empresa"])
    #     # print(empresas) # ordenados pero str
    #     print(type(empresas)) # list
    #     conjunto=set(empresas)
    #     print(conjunto)

    # for i in range(len(lista_aux)):
    #     print(lista_aux[i]["empresa"])
    #     lista_clave=set(empresa_juegos[clave].upper() for empresa_juegos in lista_aux)



    # lista_clave=set(empresa_juegos[clave].upper() for empresa_juegos in lista_aux)
    # # print(lista_clave)
    # diccionario={}
    # for i in lista_clave:
    #     # diccionario["0".format(i)]=0
    #     diccionario[f"{i}"]=0
    #     # print(i)
    #     for empresa_juegos in lista_aux:
    #         print(empresa_juegos["empresa"])
            



    # diccionario_cantidades={}
    # print(lista_clave)
    #     diccionario_cantidades["{0}",format(nivel)] = 0
    #     for elemento in lista:
    #         if elemento[clave].upper()==nivel:
    #             diccionario_cantidades["{0}".format(nivel)] +=1
    # for key in diccionario_cantidades:
    #     print("{0} :cantidad {1}".format(key,diccionario_cantidades[key]))

    return lista_aux


def main():
    lista_juegos=parse_json("burbujeo\data_pp.json")
    lista_auxiliar=lista_juegos.copy()
    continuar=True
    while continuar:
        opcion=menu()
        match opcion:
            case "1":
                # print("opcion1")
                (juegos_ordenados_empresas(lista_auxiliar,"empresa"))
            case "2":
                continuar=False


main()