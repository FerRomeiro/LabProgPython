import json
# 1. Listar los primeros N héroes. El valor de N será ingresado por el usuario
# (Validar que no supere max. de lista)

def parse_json_stark(nombre_archivo:str)->dict: #parsea el contenido del jason y devuelve una lista 
    # dic_json={} 

    archivo=open(nombre_archivo,"r") 
    dic_json=json.load(archivo)
    archivo.close()
 
    return dic_json["heroes"] #ES UNA LISTA QUE ES COMO LA LISTA DE PY LISTA_PERSONAJES "heroes"

lista_heroes=parse_json_stark("repaso\stark.json") #
print("asdasdsad")
print(lista_heroes) #ARRANCA CON UNA CLAVE QUE TIENE ASOCIADA UNA LISTA si no fuera por la clave ["heroes"]
# print(lista_heroes[0])
# print(lista_heroes)

# 1. Listar los primeros N héroes. El valor de N será ingresado por el usuario
# (Validar que no supere max. de lista)

# def imprimir_heroes():

def parse_json_stark_1(nombre_archivo:str)->list:
    archivo=open(nombre_archivo,"r") 
    list_json=json.load(archivo)["heroes"] #ACA ME DEVOLVERIA UNA LISTA
    archivo.close()

    return list_json 

lista_heroes_1=parse_json_stark("repaso\stark.json")
print("ADASDASDASDASDASDAS")
print(lista_heroes_1)