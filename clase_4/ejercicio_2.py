from data_stark import lista_heroes


def menu():

    print("A.Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M")
    print("B.Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F")
    print("C.Recorrer la lista y determinar cuál es el superhéroe más alto de género M")
    print("D.Recorrer la lista y determinar cuál es el superhéroe más alto de género F")
    print("E.Recorrer la lista y determinar cuál es el superhéroe más bajo de género M")
    print("F.Recorrer la lista y determinar cuál es el superhéroe más bajo de género F")
    print("G.Recorrer la lista y determinar la altura promedio de los superhéroes de género M")
    print("H.Recorrer la lista y determinar la altura promedio de los superhéroes de género F")
    print("I.Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)")
    print("J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.")
    print("K.Determinar cuántos superhéroes tienen cada tipo de color de pelo.")
    print("L.Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).")
    print("M.Listar todos los superhéroes agrupados por color de ojos.")
    print("N.Listar todos los superhéroes agrupados por color de pelo.")
    print("O.Listar todos los superhéroes agrupados por tipo de inteligencia")

    opcion = input("Eliga una opcion: ")

    return opcion

continuar = True
while continuar:

    opcion=menu()

    if opcion == "A":
        for heroe in lista_heroes:
            if heroe["genero"] == "M":
                nombre_heroe = heroe["nombre"]
                print("Heroes masculinos: ",nombre_heroe )

    if opcion == "K":
        print("Chau")
        continuar=False