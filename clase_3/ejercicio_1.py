from data import lista_bzrp #IMPORTAMOS LA LISTA DEL data.py


def mostrar_vista_minima(): #defino la funcion
#BUSCAMOS UN MINIMO DE LA LISTA
    minimo = None
    nombre = None
    for video in lista_bzrp:
    
        if minimo == None or video["views"] < minimo:
            minimo = video["views"]
            nombre = video["title"]

    print(nombre,minimo)
#la variable video contiene el primer diccionario de la lista_bzrp, 
# para la primera vez q itera en el for
# y asi con cada vuelta, la segunda vuelta la variable video contiene el segundo
# diccionario de lista_bzrp y asi sucesivamente 
#Como accedemos al valor de un diccionario??
#hay que poner la clave entre [] ej video["views"]

mostrar_vista_minima() #la funcion