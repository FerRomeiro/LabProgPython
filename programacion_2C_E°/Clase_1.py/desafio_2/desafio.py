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
            if bandera_altura ==False or superhero["altura"] > heroina_mas_alta:
                heroina_mas_alta = superhero["altura"]
                nombre_mas_alta = superhero["nombre"]
                bandera_altura = True
        
    return nombre_mas_alta



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

            # case "C":
            # case "D":
            # case "E":
            # case "F":
            # case "G":
            # case "H":
            # case "I":
            # case "J":
            case "K":
                print("chau")
                continuar = False




main()