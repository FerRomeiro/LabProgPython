from data_stark import lista_heroes

# import os

hombres=[]
mujeres=[]

#A
def lista_hombres(lista):
    for nombres_H in lista:
        if nombres_H["genero"] == "M":           
            print(nombres_H["nombre"])

#B
def lista_mujeres(lista):
    for nombres_f in lista:
        if nombres_f["genero"] == "F":
            print(nombres_f["nombre"])

#C
def hombre_Mas_Alto(lista):
    nombre_altura_maxima_hombre=None
    maxima_altura = 0
    for altura_hombres in lista:
        if altura_hombres["genero"] == "M":
            altura = float(altura_hombres["altura"])
            if maxima_altura == 0 or altura > maxima_altura:
                maxima_altura = float(altura_hombres["altura"])
                nombre_altura_maxima_hombre = altura_hombres["nombre"]
    return nombre_altura_maxima_hombre
    #print("El heroe mas alto es: {}, con una altura de: {}".format(nombre_altura_maxima_hombre,maxima_altura))

#D
def mujer_Mas_Alta(lista):
    #nombre_altura_maxima_hombre=None
    maxima_altura = 0
    for altura_hombres in lista:
        if altura_hombres["genero"] == "F":
            altura = float(altura_hombres["altura"])
            if maxima_altura == 0 or altura > maxima_altura:
                maxima_altura = float(altura_hombres["altura"])
                nombre_altura_maxima_mujer = altura_hombres["nombre"]
    return nombre_altura_maxima_mujer
    #print("El heroe mas alto es: {}, con una altura de: {}".format(nombre_mujer_mas_alta,maxima_altura))

#E
def hombre_Mas_Bajo(lista):
    #nombre_altura_maxima_hombre=None
    min_altura = 0
    for altura_hombres in lista:
        if altura_hombres["genero"] == "M":
            altura = float(altura_hombres["altura"])
            if min_altura == 0 or altura < min_altura:
                min_altura = float(altura_hombres["altura"])
                nombre_altura_maxima_hombre = altura_hombres["nombre"]
    return nombre_altura_maxima_hombre
    #print("El heroe mas bajo es: {}, con una altura de: {}".format(nombre_hombre_mas_bajo,baja_altura))

#F
def mujer_Mas_Baja(lista):
    min_altura = 0
    for altura_mujer in lista:
        if altura_mujer["genero"] == "F":
            altura = float(altura_mujer["altura"])
            if min_altura == 0 or altura < min_altura:
                min_altura = float(altura_mujer["altura"])
                nombre_mujer_heroe = altura_mujer["nombre"]
    return nombre_mujer_heroe
    #print("La heroe mas baja es: {}, con una altura de: {}".format(nombre_mujer_mas_baja,baja_altura))

#G
def promedio_heroes_masculinos(lista):
    acumulador_heroes_m = 0
    contador_heroes_m = 0
    for heroes_masculinos in lista:
        if heroes_masculinos["genero"] == "M":
            acumulador_heroes_m = acumulador_heroes_m + float(heroes_masculinos["altura"])
            contador_heroes_m = contador_heroes_m + 1 
    promedio_m = acumulador_heroes_m / contador_heroes_m

    return promedio_m

#H
def promedio_heroes_femeninos(lista):
    acumulador_heroes_f = 0
    contador_heroes_f = 0
    for heroes_femeninos in lista:
        if heroes_femeninos["genero"] == "F":
            acumulador_heroes_f = acumulador_heroes_f + float(heroes_femeninos["altura"])
            contador_heroes_f = contador_heroes_f + 1 
    promedio_f = acumulador_heroes_f / contador_heroes_f

    return promedio_f
#J
def tipo_color_ojos(lista):
    

    # contador_ojos_brown = 0
    # contador_ojos_green = 0
    # contador_ojos_blue = 0
    # contador_ojos_yellow_w = 0
    # contador_ojos_yellow = 0
    # contador_ojos_silver = 0 
    # contador_ojos_red = 0
    # contador_ojos_hazel = 0

    # for ojos in lista:
    #     if ojos["color_ojos"] == "Brown":
    #         contador_ojos_brown = contador_ojos_brown + 1
    #     elif ojos["color_ojos"] == "Blue":
    #         contador_ojos_blue = contador_ojos_blue + 1
    #     elif ojos["color_ojos"] == "Green":
    #         contador_ojos_green = contador_ojos_green + 1
    #     elif ojos["color_ojos"] == "Yellow (without irises)"
    #         contador_ojos_yellow_w == contador_ojos_yellow_w + 1
    #     elif ojos["color_ojos"] == "Hazel":
    #         contador_ojos_hazel = contador_ojos_hazel +1 
    #     elif ojos["color_ojos"] == "Silver":
    #         contador_ojos_silver = contador_ojos_silver + 1
    #     elif ojos["color_ojos"] == "Yellow":
    #         contador_ojos_yellow = contador_ojos_yellow + 1
    #     elif ojos["color_ojos"] == "Red":
    #         contador_ojos_red = contador_ojos_red + 1
        
        
        
def menu_final():
    #os.system("cls")
    print("A. Lista de hombres")
    print("B. Lista de mujeres")
    print("C. Superheroe mas alto hombre")
    print("D. Superheroe mas alto mujer")
    print("E. Super heroe mas bajo hombre")
    print("F. Superheroe mas bajo mujer")
    print("G. Promedio de altura de heroes masculinos")
    print("H. Promedio de altura de heroes femeninas")
    print("I. Informar desde el punto C al F")
    print("J. Determinar cuantos heroes tienen cada tipo de color de ojos")
    print("K. ")
    print("O. salir")
    #os.system("pause")
    opcion_menu = input("Eliga una opcion: ")

    return opcion_menu
#menu_final()

# opcion=input("Seleccione una opcion: ")
continuar = True
el_heroe_mas_alto = " "
la_heroina_mas_alta = " "
heroe_mas_bajo = " "
mujer_heroe_mas_baja = " "
flag_mas_alto_m=False
flag_heroina_alta=False
flag_hombre_mas_bajo=False
flag_mujer_mas_baja=False
while continuar:

    opcion=menu_final()
    
    match opcion:
        case "A":
            lista_hombres(lista_heroes)
        case "B":
            lista_mujeres(lista_heroes)
        case "C":
            el_heroe_mas_alto = hombre_Mas_Alto(lista_heroes)
            flag_mas_alto_m=True
            #print("El heroe masculino mas alto es: ", el_heroe_mas_alto)
        case "D":
            la_heroina_mas_alta = mujer_Mas_Alta(lista_heroes)
            flag_heroina_alta=True
#            print("La heroina mas alta es: ", la_heroina_mas_alta)
        case "E":
            heroe_mas_bajo = hombre_Mas_Bajo(lista_heroes)
            flag_hombre_mas_bajo=True
#            print("El heroe masculino mas bajo es: ",heroe_mas_bajo)
        case "F":
            mujer_heroe_mas_baja = mujer_Mas_Baja(lista_heroes)
            flag_mujer_mas_baja=True
#            print("La heroina mas baja es: ",mujer_heroe_mas_baja)
        case "G":
            promedio = promedio_heroes_masculinos(lista_heroes)
            print("El promedio de altura de heroes masculinos es: ", promedio)
        case "H":
            promedio_f = promedio_heroes_femeninos(lista_heroes)
            print("El promedio de altura de heroes femeninos es: ", promedio_f)
        case "I":
            if flag_mas_alto_m:
                print("El heroe masculino mas alto es: ", el_heroe_mas_alto)
            if flag_heroina_alta:            
                print("La heroina mas alta es: ", la_heroina_mas_alta)
            if flag_hombre_mas_bajo:
                print("El heroe masculino mas bajo es: ",heroe_mas_bajo)
            if flag_mujer_mas_baja:
                print("La heroina mas baja es: ",mujer_heroe_mas_baja)
        case "J":

        case "O":
            continuar=False
        
    

