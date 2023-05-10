

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

    for i in valor:
        pokemon=i.split(",")
        diccionario_pokemon={"N° Pokedex":pokemon[0],"Nombre":pokemon[1],"Tipo":pokemon[2],"Poder de ataque":pokemon[3],"Poder de defensa":pokemon[4],"Habilidades":pokemon[5]}
        
        # print(diccionario_pokemon)
        lista_pokemones.append(diccionario_pokemon)

        # archivo.write(diccionario)

    archivo.close()

    return lista_pokemones

# 2. Listar cantidad por tipo: mostrará todos los tipos indicando la cantidad de
# pokemones que corresponden a ese tipo.

def cantidad_tipo(lista:list):

    contador_planta=0

    for i in lista:
        if i["Tipo"] == "Planta/Veneno":
            contador_planta=contador_planta+1
        # elif "Tipo" == ""
    print(contador_planta)






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
            cantidad_tipo(pokemones)
            input("Ingrese una tecla para continuar...")
        case "3":
            print("asd")
            input("Ingrese una tecla para continuar...")
        case "4":
            print("asd")
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