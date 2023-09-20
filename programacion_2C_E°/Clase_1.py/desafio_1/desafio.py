#nombre: Fernando Romero Montero

from data_stark import lista_heroes

# A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
# B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
# fuerza (MÁXIMO)
# C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
# (MÍNIMO)
# D. Recorrer la lista y determinar el peso promedio de los superhéroes
# masculinos (PROMEDIO)
# E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
# género) los cuales su fuerza supere a la fuerza promedio de todas las
# superhéroes de género femenino


def menu():

    print("A.Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe")
    print("B.Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)")
    print("C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)")
    print("E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino")
    print("J. Salir")

    opcion = input("Eliga una opcion: ")

    return opcion

continuar=True


while continuar:
    opcion_menu = menu()

    if opcion_menu == "A":
        for superhero in lista_heroes:
            print(superhero["nombre"],superhero["altura"],superhero["identidad"],superhero["peso"],superhero["genero"],superhero["color_ojos"],superhero["color_pelo"],superhero["fuerza"],superhero["inteligencia"])
            # print("NOMBRE: {} IDENTIDAD: {} EMPRESA: {} ALTURA: {} PESO:{} GENERO: {} OJOS: {} PELO: {} FUERZA: {} INTELIGENCIA: {}".format(superhero["nombre"],superhero["identidad"],superhero["altura"],superhero["peso"],superhero["genero"],superhero["color_ojos"],superhero["color_pelo"],superhero("fuerza"),superhero["inteligencia"]))
        
    elif opcion_menu == "B":
        bandera_fuerza=False
        for superhero in lista_heroes:
            if bandera_fuerza == False or superhero["fuerza"] > mayor_fuerza:
                nombre_heroe_mayor_fuerza = superhero["nombre"]
                mayor_fuerza = superhero["fuerza"]
                bandera_fuerza=True
        
        print("Heroe mas fuerte: ", nombre_heroe_mayor_fuerza , " con una fuerza de ", mayor_fuerza)
    
    elif opcion_menu == "C":
        bandera_altura=False
        for superhero in lista_heroes:
            if bandera_altura == False or superhero["altura"] < altura_baja:
                nombre_heroe_bajo = superhero["nombre"]
                altura_baja = superhero["altura"]
                bandera_altura=True
        
        print("Heroe mas bajo: ", nombre_heroe_bajo , " con una altura de ", altura_baja)        
    
    elif opcion_menu == "D":
        acumulador_fuerza=0
        lista_heroes_fuerza=[]
        for superhero in lista_heroes:
            acumulador_fuerza = acumulador_fuerza + int(superhero["fuerza"])
        
        promedio_fuerza_heroes = acumulador_fuerza / len(lista_heroes)
        print(promedio_fuerza_heroes)

        for heroes in lista_heroes:

            if float(heroes["fuerza"]) > promedio_fuerza_heroes: 
                lista_heroes_fuerza.append(heroes["nombre"])
        print(lista_heroes_fuerza)
    
    elif opcion_menu == "J":
        print("Chau")
        continuar=False