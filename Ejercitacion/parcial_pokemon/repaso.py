import re

def menu():
    print("1.Traer datos desde archivo.")
    print("2.Listar cantidad por tipo.")
    print("3.Listar pokemones por tipo")
    print("4.Listar pokemones por habilidad:")
    print("5.Listar pokemones ordenados")
    print("6.Guardar Json")
    print("7.Leer Json")
    print("8.Salir del programa")

    opcion=input("Ingrese una opcion: ")

    return opcion

# 1. guardar el contenido del archivo
# pokemones.csv en una colección. Tener en cuenta que tanto tipos y
# habilidades deben estar guardadas en algún tipo de colección, debido a que
# un pokemón puede tener más de un tipo y más de una habilidad.
def pokemon_json(nombre_archivo_csv:str)->list:
    lista_pokemones=[]
    archivo=open(nombre_archivo_csv,"r")
    valor=archivo.read() #como se trata de un string el archivo csv entonces usamos la funcion read para extraer el string del archivo
    # print(valor)
    valor=valor.split("\n")
    # print(valor)
    # valor=archivo.readlines()

    for i in valor[1:]:
        pokemon=i.split(",")
        diccionario_pokemon={}
        # diccionario_pokemon={"N° Pokedex":pokemon[0],"Nombre":pokemon[1],"Tipo":pokemon[2],"Poder de ataque":pokemon[3],"Poder de defensa":pokemon[4],"Habilidades":pokemon[5]}
        diccionario_pokemon["N° Pokedex"] = (pokemon[0])
        diccionario_pokemon["Nombre"] = (pokemon[1])
        diccionario_pokemon["Tipo"] = (pokemon[2].split("/"))
        diccionario_pokemon["Poder de ataque"] = (pokemon[3])
        diccionario_pokemon["Poder de defensa"] = (pokemon[4])
        diccionario_pokemon["Habilidades"] = re.sub("\n","",pokemon[5])
        diccionario_pokemon["Habilidades"] = diccionario_pokemon["Habilidades"].split("|*|")

        # print(diccionario_pokemon)
        lista_pokemones.append(diccionario_pokemon)

        # archivo.write(diccionario)

    archivo.close()

    return lista_pokemones

# 2. Listar cantidad por tipo: mostrará todos los tipos indicando la cantidad de
# pokemones que corresponden a ese tipo.

def acentos(lista:list):
    lista=[]
    for i in lista:
        tipos=i["Tipo"]
        for j in tipos:
            # print(j)
            j_sin_acento=j.replace("á","a").replace("Ã©","e").replace("Ã­","i").replace("Ã³","o").replace("ú","u")
            # print(j_sin_acento)
            lista.append(j_sin_acento)

    print(lista)

    # return lista



def cantidad_tipo(lista:list)->list:

    lista_tipo=[]
    contador_planta=0
    contador_veneno=0
    contador_fuego=0
    contador_bicho=0
    contador_hielo=0
    contador_psiquico=0
    contador_tierra=0
    contador_roca=0
    contador_lucha=0
    contador_normal=0
    contador_hada=0
    contador_electrico=0
    contador_agua=0
    contador_volador=0

    for i in lista:
        # print(i["Tipo"])

        if "Planta" in i["Tipo"]:
            contador_planta=contador_planta+1
        elif "Veneno" in i["Tipo"]:
            contador_veneno=contador_veneno+1
        elif "Fuego" in i["Tipo"]:
            contador_fuego=contador_fuego+1
        elif "Bicho" in i["Tipo"]:
            contador_bicho=contador_bicho+1
        elif "Hielo" in i["Tipo"]:
            contador_hielo=contador_hielo+1
        elif "Psiquico" in i["Tipo"]:
            contador_psiquico=contador_psiquico+1
        elif "Tierra" in i["Tipo"]:
            contador_tierra=contador_tierra+1
        elif "Roca" in i["Tipo"]:
            contador_roca=contador_roca+1
        elif "Lucha" in i["Tipo"]:
            contador_lucha=contador_lucha+1
        elif "Normal" in i["Tipo"]:
            contador_normal=contador_normal+1
        elif "Hada" in i["Tipo"]:
            contador_hada=contador_hada+1
        elif "Electrico" in i["Tipo"]:
            contador_electrico=contador_electrico+1
        elif "Agua" in i["Tipo"]:
            contador_agua=contador_agua+1
        elif "Volador" in i["Tipo"]:
            contador_volador=contador_volador+1
        
    lista_tipo.append("Tipo planta: "+str(contador_planta))
    lista_tipo.append("Tipo veneno: "+str(contador_veneno))
    lista_tipo.append("Tipo fuego: "+str(contador_fuego))
    lista_tipo.append("Tipo bicho: "+str(contador_bicho))
    lista_tipo.append("Tipo hielo: "+str(contador_hielo))
    lista_tipo.append("Tipo psiquico: "+str(contador_psiquico))
    lista_tipo.append("Tipo tierra: "+str(contador_tierra))
    lista_tipo.append("Tipo lucha: "+str(contador_lucha))
    lista_tipo.append("Tipo roca: "+str(contador_roca))
    lista_tipo.append("Tipo normal: "+str(contador_normal))
    lista_tipo.append("Tipo electrico: "+str(contador_electrico))
    lista_tipo.append("Tipo agua: "+str(contador_agua))
    lista_tipo.append("Tipo volador: "+str(contador_volador))
    lista_tipo.append("Tipo hada: "+str(contador_hada))

    # print(contador_planta)

    return lista_tipo

# 3. Listar pokemones por tipo: mostrará cada tipo indicando el nombre y poder
# de ataque de cada pokemon que corresponde a ese tipo.
def lista_pokemones(lista:list):

    lista_pokemones=[]

    for i in lista:
        # tipo=i["Tipo"]
        if "Planta" in i["Tipo"]:
            nombre=i["Nombre"]
            ataque=i["Poder de ataque"]
            lista_pokemones.append(f"Nombre: {nombre}\n Poder de ataque:{ataque}")
            # lista_pokemones.append(ataque)
    print(lista_pokemones)
# 4. Listar pokemones por habilidad: el usuario ingresa la descripción de una
# habilidad y el programa deberá mostrar nombre, tipo y promedio de poder
# entre ataque y defensa.

def lista_pokemones_habilidad(lista:list):



    print(lista_pokemones)

    # for i in  lista:
    #     tipo=i["Tipo"]
    #     print(tipo)
    #     for j in tipo:
    #         print(j)
    #         if j in tipo:
    #             print(lista["Nombre"])
    #             nombre=lista["Nombre"]
    #             ataque=lista["Poder de ataque"]
    #             lista.append(nombre)

    #     print(lista_pokemones)



continuar=True

while continuar:

    opcion=menu()

    match opcion:
        case "1":
            # print("asd")
            pokemones=pokemon_json("parcial_pokemon\pokemones.csv")
            print(type(pokemones))
            print(pokemones)
            input("Ingrese una tecla para continuar...")
        case "2":
            print(cantidad_tipo(pokemones))
            input("Ingrese una tecla para continuar...")
        case "3":
            acentos(pokemones)
            input("Ingrese una tecla para continuar...")
        case "4":
            lista_pokemones(pokemones)
            input("Ingrese una tecla para continuar...")
        case "5":
            print("asd")
            input("Ingrese una tecla para continuar...")
        case "6":
            print("asd")
            input("Ingrese una tecla para continuar...")
        case "7":
            print("asd")
            input("Ingrese una tecla para continuar...")
        case "8":
            continuar=False
            print("CHAU")