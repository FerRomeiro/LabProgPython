def normalizar_flotantes(lista:list,clave:str):

    for i in lista:
        i[clave]=float(i[clave])

def normalizar_str(lista:list,clave:str):

    for i in lista:
        i[clave]=str(i[clave])


