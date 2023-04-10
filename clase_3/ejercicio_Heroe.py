from data_stark import lista_heroes

def menu():
    print("A.Recorrer la lista imprimiendo por consola el nombre de cada superhéroe")
    print("B.Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo")
    print("C.Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)")
    print("D.Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)")
    print("E.Recorrer la lista y determinar la altura promedio de los superhéroes PROMEDIO")
    print("F.Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)")
    print("G.Calcular e informar cual es el superhéroe más y menos pesado")
    print("H.")
    print("I.")
    print("J. Salir")

    opcion = input("Eliga una opcion: ")
    #opcion_elegida = int(opcion)

    return opcion

continuar=True
#mayor_altura=None


while continuar:
    opcion_menu = menu()

    if opcion_menu == "A":
        for superhero in lista_heroes:
            print("El nombre es: ",superhero["nombre"])

    elif opcion_menu == "B":
        for superhero in lista_heroes:
            print("Nombre:{} Altura:{}".format(superhero["nombre"],superhero["altura"]))

    elif opcion_menu == "C":
        bandera_altura =False
        for superhero in lista_heroes:
            if bandera_altura == False or mayor_altura > superhero["altura"]:
                nombre_heroe = superhero["nombre"]
                mayor_altura = superhero["altura"]
                bandera_altura=True
                
        print("El superheroe " , nombre_heroe , " es el mas alto con una altura de " + mayor_altura)

    elif opcion_menu == "D":
        bandera_altura_min = False
        for superhero in lista_heroes:
            if bandera_altura_min == False or minima_altura < superhero["altura"]:
                nombre_heroe_min = superhero["nombre"]
                minima_altura = superhero["altura"]
                bandera_altura_min = True

        print("El heroe mas enano es ", nombre_heroe_min , " con una altura de ", minima_altura)
    elif opcion_menu == "E":
        acumulador_altura = 0
        for superhero in lista_heroes:
            acumulador_altura = acumulador_altura + float(superhero["altura"]) #CONVERTI LE DATO DE ALTURA Q ERA CADENA DE TEXTO EN FLOAT PARA SACAR EL PROMEDIO
        
        promedio_alturas = acumulador_altura / len(lista_heroes)#LEN ME DA EL NUMERO DE HEROES EN LA LISTA
        print("La altura promedio es: ", promedio_alturas)

    elif opcion_menu == "G":
        #bandera_peso = False
        bandera_peso = False #La bandera siempre debe estar dentro del for porque sino la bandera tendria siempre el mismo valor
        for superhero in lista_heroes:
            #bandera_peso = False
            if bandera_peso == False:
                peso_maximo = superhero["peso"]
                peso_minimo = superhero["peso"]
                nombre_heroe_peso_max = superhero["nombre"]
                nombre_heroe_peso_min = superhero["nombre"]
                bandera_peso = True
            else:
                if peso_maximo > superhero["peso"]:
                    nombre_heroe_peso_max=superhero["nombre"]
                    peso_maximo = superhero["peso"]
                if peso_minimo < superhero["peso"]:
                    nombre_heroe_peso_min=superhero["nombre"]
                    peso_minimo=superhero["peso"]

            # if bandera_peso == False or peso_maximo > superhero["peso"]:
            #     nombre_heroe_peso_max = superhero["nombre"]
            #     peso_maximo = superhero["peso"]
            
            # if bandera_peso == False or peso_minimo < superhero["peso"]:
            #     nombre_heroe_peso_min = superhero["nombre"]
            #     peso_minimo = superhero["peso"]
            #     bandera_peso = True

        print("El heroe mas pesado es:{} Y el heroe mas liviano es: {}".format(nombre_heroe_peso_max,nombre_heroe_peso_min))


    elif opcion_menu == "K":
        print("Chau")
        continuar=False




