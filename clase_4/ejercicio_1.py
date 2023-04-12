from data_stark import lista_heroes


opciones = ["1.Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M",
            "2.Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F",
            "3.Recorrer la lista y determinar cuál es el superhéroe más alto de género M",
            "4)salir"
            ]

def menu_principal(opciones):
    for i in opciones:
        print(i)
    opcion_elegida = input("Elija opcion: ")

    return opcion_elegida

while True:
    opcion_elegid=menu_principal(opciones)
    #int(opcion_elegid)
    match opcion_elegid:
        case 1:
            #print("Opcion 1")
            for heroe in lista_heroes["genero"]:
                if heroe == "M":
                    nombre_heroe = lista_heroes["nombre"]
                    print("Heroes de genero masculino: ",heroe)
        case 2:
            print("opcion 2")
        case 3:
            print("opcion 3")
        case 4:
            print("opcion 4")