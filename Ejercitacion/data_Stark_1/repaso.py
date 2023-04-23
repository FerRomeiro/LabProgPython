from data_stark import lista_personajes

def menu():

    print("1.")
    print("2.")
    print("3.")
    print("4.")
    print("5.")
    print("6.")
    print("7.")
    print("8.")
    print("9.")
    print("10.")
    print("11.")
    print("12.")
    print("13.")
    print("14.")
    print("15.")
    print("16. Exit")

    opcion = input("Eliga una opcion: ")
    opcion = int(opcion)
    return opcion

# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# # género M
# def sexo_m(lista_personajes):

#     lista_masculinos=[]

#     for heroes in lista_personajes:
#         if heroes["genero"] == "M":
#             lista_masculinos.append(heroes["nombre"])
    
#     return lista_masculinos

# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# # género F
# def sexo_f(lista_personajes):

#     lista_femenina=[]

#     for heroes in lista_personajes:
#         if heroes["genero"] == "F":
#             lista_femenina.append(heroes["nombre"])

#     return lista_femenina

# OTRA FORMA DE IMPLEMENTAR AMBOS PUNTOS ANTERIORES
def sexo_f_m(lista_personajes,valor=True):

    lista_vacia=[]
    
    for i in lista_personajes:
        if valor:
            if i["genero"] == "F":
                lista_vacia.append(i["nombre"])
        else: 
            lista_vacia.append(i["nombre"])

    return lista_vacia

# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M 
def mas_alto(lista_personajes):
    
    nombre = lista_personajes[0]["nombre"]
    # altura = float(lista_personajes[0]["altura"])
    altura = 0
    for heroes in lista_personajes:
        # altura_max = float(heroes["altura"])
        if heroes["genero"] == "M" and float(heroes["altura"]) > altura:
            nombre=heroes["nombre"]
            altura=float(heroes["altura"])
    return nombre

# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F 
def mas_alto_f(lista_personajes):
    
    nombre = lista_personajes[0]["nombre"]
    # altura = float(lista_personajes[0]["altura"])
    altura = 0
    for heroes in lista_personajes:
        # altura_max = float(heroes["altura"])
        if heroes["genero"] == "F" and float(heroes["altura"]) > altura:
            nombre=heroes["nombre"]
            altura=float(heroes["altura"])
    return nombre
#PUEDO JUNTAR AMBOS 
def mas_alto_f_m(lista,valor=True):
    nombre=lista[0]["nombre"]
    altura=0
    for heroes in lista:
        if valor:
            if  heroes["genero"] == "M" and float(heroes["altura"]) > altura:
                nombre=heroes["nombre"]
                altura = float(heroes["altura"])
        else:
            if heroes["genero"] == "F" and float(heroes["altura"])>altura:
                nombre=heroes["nombre"]
                altura=float(heroes["altura"])
    return nombre

# E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M 
def heroe_mas_bajo(lista):
    nombre=lista[0]["nombre"]
    altura=float(lista[0]["altura"]) #AGARRE LA ALTURA DEL PRIMERO DE LA LISTA YA QUE SI PONGO "0" NADIE ES MAS BAJO QUE 0 
    for bajo in lista:
        if bajo["genero"]=="M" and float(bajo["altura"])<altura:
            nombre=bajo["nombre"]
            altura=float(bajo["altura"])
    return nombre

# F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F 
def heroe_mas_bajo_f(lista):
    # nombre=lista[0]["nombre"]
    # altura=float(lista[0]["altura"]) #AGARRE LA ALTURA DEL PRIMERO DE LA LISTA YA QUE SI PONGO "0" NADIE ES MAS BAJO QUE 0 
    altura=0
    for bajo in lista:
        if bajo["genero"]=="F":
            altura_min= float(bajo["altura"])
            if altura == 0 or altura_min < altura:
                nombre=bajo["nombre"]
                altura=float(bajo["altura"])
    return nombre
# G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
def promedio_heroes_m(lista):
    acumulador_altura=0
    contador_heroes=0
    for i in lista:
        if i["genero"] == "M":
            acumulador_altura = acumulador_altura + float(i["altura"])
            contador_heroes=contador_heroes+1

    promedio=acumulador_altura/contador_heroes

    return promedio
# H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
def promedio_heroes_f(lista):
    acumulador_altura=0
    contador_heroes=0
    for i in lista:
        if i["genero"] == "F":
            acumulador_altura = acumulador_altura + float(i["altura"])
            contador_heroes=contador_heroes+1

    promedio=acumulador_altura/contador_heroes

    return promedio

# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
def contar_colores_ojos(lista):

   # Crear un conjunto de los colores de ojos únicos en mayúsculas
    lista_colores_ojos = set(personaje["color_ojos"].upper() for personaje in lista)
    
    # Inicializar el diccionario de contadores
    d = {}
    for color in lista_colores_ojos:
        d["contador {0}".format(color)] = 0
    
    # Contar la cantidad de personajes con cada color de ojos
    for personaje in lista:
        color_ojos = personaje["color_ojos"].upper()
        d["contador {0}".format(color_ojos)] += 1

    return d

    # Crear un conjunto de los colores de ojos únicos en mayúsculas
    # lista_colores_ojos = set(personaje["color_ojos"].upper() for personaje in lista) #{'YELLOW (WITHOUT IRISES)', 'HAZEL', 'SILVER', 'RED', 'YELLOW', 'BLUE', 'BROWN', 'GREEN'}
    # contador_color_ojos=[]
    # d=[]
    # for i,color in enumerate(lista_colores_ojos): 
    #     # color=print(i,color)#0 RED 1 SILVER 2 YELLOW 3 BROWN 4 GREEN 5 BLUE 6 HAZEL 7 YELLOW (WITHOUT IRISES)
    #     d["contadores{0}".format(color)]= 0
    #     for personaje in lista:
    #         if personaje["color ojos "] == color:
    #             d["color"] += 1 

    # return d

# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
def tipo_color_pelo(lista):
    lista_tipo_pelo = set(personaje["color_pelo"].upper() for personaje in lista) # iteramos una lista de color unicos de pelo, salen 1 vez

    d={} #diccionario vacio
    for pelo in lista_tipo_pelo:
        d["tipo de pelo {0}".format(pelo)]=0 #lo unicializamos en 0 cada contador de pelo
    
    for personaje in lista: 
        color_pelo=personaje["color_pelo"].upper()
        d["tipo de pelo {0}".format(color_pelo)] += 1
    
    return d

# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
# no tener, Inicializarlo con ‘No Tiene’).
def tipo_inteligencia(lista):
    
    lista_inteligencia = set(personaje["inteligencia"].upper() for personaje in lista)
    
    d={}
    d["no tiene"]=0

    for inteligencia in lista_inteligencia:
        d["Tipo de inteligencia: {0}".format(inteligencia)] = 0
    
    for personajes in lista:
        i=personajes["inteligencia"].upper()
        if i:
            d["Tipo de inteligencia: {0}".format(i)] += 1
        else:
            d["no tiene"]+=1

    return d

# M. Listar todos los superhéroes agrupados por color de ojos.
def heroes_color_ojos(lista):
    lista_colores_ojos = set(personaje["color_ojos"].upper() for personaje in lista)
    
    d={}
    for color_ojos in lista_colores_ojos:
        lista_heroes=[]
        
        for heroe in lista:
            if heroe["color_ojos"].upper() == color_ojos:
                lista_heroes.append(heroe["nombre"])

        d[color_ojos] = lista_heroes
        

    return d

# N. Listar todos los superhéroes agrupados por color de pelo.

def heroes_color_pelo(lista):
    lista_color_pelo=set(heroe["color_pelo"].upper() for heroe in lista)

    d={}
    for pelo in lista_color_pelo:
        lista_pelo_heroes=[]
        for personaje in lista:
            if personaje["color_pelo"].upper() == pelo:
                lista_pelo_heroes.append(personaje["nombre"])
        d[pelo] = lista_pelo_heroes
    
    return d

# O. Listar todos los superhéroes agrupados por tipo de inteligencia

def heroes_inteligencia(lista):
    lista_inteligencia=set(personaje["inteligencia"].upper() for personaje in lista)

    d={"no tiene":[]}
    
    for inteligencia in lista_inteligencia:
        lista_heroe_inteligencia=[]
        for heroe in lista:
            if heroe["inteligencia"].upper() == inteligencia: 
                lista_heroe_inteligencia.append(heroe["nombre"])
        d[inteligencia] = lista_heroe_inteligencia

    return d 




continuar=True

while continuar:

    opcion_menu = menu()

    match opcion_menu:
        case 1:
            # print("Eligio opcion 1")
            # lista_masculinos=sexo_m(lista_personajes)
            # print(lista_masculinos)
            lista_masculinos=sexo_f_m(lista_personajes,valor=True)
            print(lista_masculinos)
            input("Presione una tecla para continuar ... ")
        case 2:
            # print("Eligio opcion 2")
            # lista_heroes_femenina=sexo_f(lista_personajes)
            # print(lista_heroes_femenina)           
            lista_femeninos=sexo_f_m(lista_personajes,valor=False)
            print(lista_femeninos)
            input("Presione una tecla para continuar ... ")
        case 3:
            # print("Eligio opcion 3")
            nombre_p_mas_alto_m=mas_alto(lista_personajes)
            print(nombre_p_mas_alto_m)
            input("Presione una tecla para continuar ... ")
        case 4:
            nombre_p_mas_alto_f=mas_alto_f(lista_personajes)
            print(nombre_p_mas_alto_f)
            input("Presione una tecla para continuar ... ")
        case 5:
            # print("Eligio opcion 5")
            heroe_mas_alto=mas_alto_f_m(lista_personajes,valor=True)
            print(heroe_mas_alto)
            input("Presione una tecla para continuar ... ")
        case 6:
            hero_bajo=heroe_mas_bajo(lista_personajes)
            print(hero_bajo)
        case 7:
            heroe_bajo_femenino = heroe_mas_bajo_f(lista_personajes)
            print(heroe_bajo_femenino)
        case 8:
            heroes_masculinos_p= promedio_heroes_m(lista_personajes)
            print(heroes_masculinos_p)
        case 9:
            heroes_femeninos_p= promedio_heroes_f(lista_personajes)
            print(heroes_femeninos_p)
        case 10:
            color=contar_colores_ojos(lista_personajes)
            print(color)
        case 11:
            pelo=tipo_color_pelo(lista_personajes)
            print(pelo)
        case 12:
            inteligencia=tipo_inteligencia(lista_personajes)
            print(inteligencia)
        case 13:
            heroes_c=heroes_color_ojos(lista_personajes)
            print(heroes_c)
        case 14:
            pl=heroes_color_pelo(lista_personajes)
            print(pl)
        case 15:
            i=heroes_inteligencia(lista_personajes)
            print(i)
        case 16:
            print("CHAU")
            continuar=False

        