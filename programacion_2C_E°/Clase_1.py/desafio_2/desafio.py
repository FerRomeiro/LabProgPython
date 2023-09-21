from data_stark import lista_heroes
import re
# Desafío #02:
# Usando como base lo realizado en el anterior desafío realizar los siguientes
# informes en un menú
# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género NB
# B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
# E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
# F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
# género NB
# G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# I. Listar todos los superhéroes agrupados por color de ojos.
# J. Listar todos los superhéroes agrupados por tipo de inteligencia
# NOTA: Se debe aplicar el tema Funciones visto en clase para cada opción del menú


def menu():

    print("A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB")
    print("B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F")
    print("C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M")
    print("D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M")
    print("E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB")
    print("F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB")
    print("G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.")
    print("H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
    print("I. Listar todos los superhéroes agrupados por color de ojos.")   
    print("I. Listar todos los superhéroes agrupados por color de ojos.")
    print("J. Listar todos los superhéroes agrupados por tipo de inteligencia")
    print("K. Salir")


    opcion=input("ingrese una opcion: ")

    return opcion

# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género NB
def genero_nb(lista_personajes:list)->list:
    
    lista_nb=[]

    for superhero in lista_personajes:
        patron=r"NB"
        genero=superhero["genero"]
        resultado=re.search(patron,genero)

        if resultado:
            lista_nb.append(superhero["nombre"])
    
    return lista_nb

# B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F

def heroe_femenina_mas_alta(lista_personajes:list)->str:
    bandera_altura=False
    for superhero in lista_personajes:
        patron=r"F"
        genero=superhero["genero"]
        resultado=re.search(patron,genero)

        if resultado:
            if bandera_altura == False or float(superhero["altura"]) > float(heroina_mas_alta):
                heroina_mas_alta = superhero["altura"]
                nombre_mas_alta = superhero["nombre"]
                bandera_altura = True
        
    return nombre_mas_alta

# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M

def heroe_masculino_mas_alto(lista_personajes:list)->str:
    bandera_altura=False
    for superhero in lista_personajes:
        patron=r"M"
        genero=superhero["genero"]
        resultado=re.search(patron,genero)

        if resultado:
            if bandera_altura == False or float(superhero["altura"]) > float(heroe_mas_alto):
                heroe_mas_alto = superhero["altura"]
                nombre_mas_alto = superhero["nombre"]
                bandera_altura = True
        
    return nombre_mas_alto

# D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M

def heroe_mas_debil(lista_personajes:list)->str:
    bandera_debil=False
    for superhero in lista_personajes:
        patron=r"M"
        genero=superhero["genero"]
        resultado=re.search(patron,genero)

        if resultado:
            if bandera_debil == False or int(superhero["fuerza"]) < int(heroe_debil):
                heroe_debil = superhero["fuerza"]
                nombre_heroe_debil = superhero["nombre"]
                bandera_debil = True

    return nombre_heroe_debil

# E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB

def heroe_mas_debil_nb(lista_personajes:list)->str:
    bandera_debil=False
    for superhero in lista_personajes:
        patron=r"NB"
        genero=superhero["genero"]
        resultado=re.search(patron,genero)

        if resultado:
            if bandera_debil == False or int(superhero["fuerza"]) < int(heroe_debil):
                heroe_debil = superhero["fuerza"]
                nombre_heroe_debil_nb = superhero["nombre"]
                bandera_debil = True

    return nombre_heroe_debil_nb

# F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
# # género NB

def promedio_fuerza_nb(lista_personajes:list)->float:

    contador_heroes_nb = 0    
    acumulador_fuerza=0
    for superhero in lista_personajes:
        
        patron=r"NB"
        genero=superhero["genero"]
        resultado=re.search(patron,genero)

        if resultado:
            contador_heroes_nb=contador_heroes_nb+1
            fuerza=int(superhero["fuerza"])
            acumulador_fuerza = acumulador_fuerza + fuerza

        promedio_fuerza = acumulador_fuerza / contador_heroes_nb

    return promedio_fuerza

# G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.

def listar_cantidad_clave(lista_personajes,clave):

        lista_clave = set(superhero[clave].upper() for superhero in lista_personajes)

        diccionario_ojos={}
        # print(lista_clave)
        for ojos in lista_clave:
            diccionario_ojos["{0}".format(ojos)] = 0
            # print(diccionario_ojos)
            for color_ojos in lista_personajes:
                if color_ojos[clave].upper() == ojos:
                    diccionario_ojos["{0}".format(ojos)] += 1
        for cantidad in diccionario_ojos:
            print("{0}:{1}".format(cantidad,diccionario_ojos[cantidad]))

# H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.

def listar_cantidad_clave(lista_personajes,clave):

        lista_clave = set(superhero[clave].upper() for superhero in lista_personajes)

        diccionario_ojos={}
        # print(lista_clave)
        for ojos in lista_clave:
            diccionario_ojos["{0}".format(ojos)] = 0
            # print(diccionario_ojos)
            for color_ojos in lista_personajes:
                if color_ojos[clave].upper() == ojos:
                    diccionario_ojos["{0}".format(ojos)] += 1
        for cantidad in diccionario_ojos:
            print("{0}:{1}".format(cantidad,diccionario_ojos[cantidad]))

# I. Listar todos los superhéroes agrupados por color de ojos.
def listar_cantidad_heroes(lista_personajes,clave):

    diccionario_heroes={}
    heroes=[]
    lista_clave = set(superhero[clave].upper() for superhero in lista_personajes)
    print(lista_clave)
    for ojos in lista_clave:
        for color_ojos in lista_personajes:
            if color_ojos[clave].upper() == ojos:
                diccionario_heroes[color_ojos[clave]].append(ojos["nombre"])
            print(diccionario_heroes)


def main():

    continuar=True

    while continuar:

        opcion = menu()

        match opcion:
            case "A":
                # lista_heroes_genero_nb = genero_nb(lista_heroes)
                print(genero_nb(lista_heroes))
            case "B":
                print(heroe_femenina_mas_alta(lista_heroes))
            case "C":
                print(heroe_masculino_mas_alto(lista_heroes))
            case "D":
                print(heroe_mas_debil(lista_heroes))
            case "E":
                print(heroe_mas_debil_nb(lista_heroes))
            case "F":
                print(promedio_fuerza_nb(lista_heroes))
            case "G":
                listar_cantidad_clave(lista_heroes,"color_ojos")
            case "H":
                listar_cantidad_clave(lista_heroes,"color_pelo")
            case "I":
                listar_cantidad_heroes(lista_heroes,"color_ojos")
            # case "J":
            case "K":
                print("chau")
                continuar = False




main()