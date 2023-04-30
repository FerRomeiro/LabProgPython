from dt6.data_stark import lista_personajes
import re

def menu():
    print("opcion 1")
    print("opcion 2")
    print("opcion 3")
    print("opcion 4")
    print("opcion 5")
    print("opcion 6")
    print("opcion 7")
    print("opcion 8")
    print("opcion 9")
    print("opcion 10")

    opcion = input("Eliga opcion: ")

    return opcion

# 3.1. Crear la función ‘sanitizar_entero’ la cual recibirá como parámetro:
# ● numero_str: un string que representa un posible número entero
# La función deberá analizar el string recibido y determinar si es un número
# entero positivo. La función debe devolver distintos valores según el problema
# encontrado:
# ● Si contiene carácteres no numéricos retornar -1
# ● Si el número es negativo se deberá retornar un -2
# ● Si ocurren otros errores que no permiten convertirlo a entero entonces
# se deberá retornar -3
# También deberá quitar los espacios en blanco de atras y adelante del string
# en caso que los tuviese
# En caso que se verifique que el texto contenido en el string es un número
# entero positivo, retornarlo convertido en entero


def sanitizar_entero(numero_str:str)->int:

    numero_str=numero_str.strip() # elimino espacios en blanco
    patron = r"[a-zA-Z]" # HAY QUE PONER PATRON PARA USAR RESEARCH
    resultado = re.search(patron,numero_str)
    # if not numero_str.isnumeric():
    if resultado:
        retorno = -1
    elif int(numero_str)<0:
        retorno = -2
    elif int(numero_str)>0:
        retorno = int(numero_str)
    else:
        retorno=-3    

    return retorno




# 3.2. Crear la función ‘sanitizar_flotante’ la cual recibirá como parámetro:
# ● numero_str: un string que representa un posible número decimal
# La función deberá analizar el string recibido y determinar si es un número
# flotante positivo. La función debe devolver distintos valores según el
# problema encontrado:
# ● Si contiene carácteres no numéricos retornar -1
# ● Si el número es negativo se deberá retornar un -2
# ● Si ocurren otros errores que no permiten convertirlo a entero entonces
# se deberá retornar -3
# También deberá quitar los espacios en blanco de atras y adelante del string
# en caso que los tuviese
# En caso que se verifique que el texto contenido en el string es un número
# flotante positivo, retornarlo convertido en flotante


def sanitizar_flotante(numero_str:str)->float:

    patron=r"[a-zA-Z]"
    resultado=re.search(patron,numero_str)
    numero_str=numero_str.strip()

    if resultado:
        retorno = -1
    elif float(numero_str)<0:
        retorno=-2
    elif float(numero_str)>0:
        retorno=numero_str
    else:
        retorno=-3 #ACA COMO HAGO PARA  Q DEVUELVA -3

    return retorno


#   3.3. Crear la función ‘sanitizar_string’’ la cual recibirá como parámetro
# ● valor_str: un string que representa el texto a validar
# ● valor_por_defecto: un string que representa un valor por defecto
# (parámetro opcional, inicializarlo con ‘-’)
# La función deberá analizar el string recibido y determinar si es solo texto (sin
# números). En caso de encontrarse números retornar “N/A”
# En el caso que valor_str contenga una barra ‘/’ deberá ser reemplazada por un
# espacio
# El espacio es un caracter válido

# En caso que se verifique que el parámetro recibido es solo texto, se deberá
# retornar el mismo convertido todo a minúsculas
# En el caso que el texto a validar se encuentre vacío y que nos hayan pasado
# un valor por defecto, entonces retornar el valor por defecto convertido a
# minúsculas
# Quitar los espacios en blanco de atras y adelante de ambos parámetros en
# caso que los tuviese  

def sanitizar_string(valor_str:str,valor_por_defecto="-"):
    
    # retorno=False
    
    patron=r"[0-9]"
    resultado = re.search(patron,valor_str)

    patron_1=r"[a-zA-Z]"
    resultado_1=re.search(patron_1,valor_str)

    valor_str=valor_str.replace("/"," ")
    valor_str = valor_str.replace("_", " ")

    valor_str=valor_str.strip()
    valor_por_defecto=valor_por_defecto.strip()
    # valor_str = re.sub(r'\s+', ' ', valor_str)

    if resultado:
        retorno = "N/A"

    elif resultado_1:
    # elif valor_str.isalpha():
        retorno = valor_str.lower()

    elif len(valor_str) == 0:
        retorno=valor_por_defecto.lower()
    
    return retorno




# Crear la función ‘sanitizar_dato’ la cual recibirá como parámetros:
# ● heroe: un diccionario con los datos del personaje
# ● clave: un string que representa el dato a sanitizar (la clave del
# diccionario). Por ejemplo altura
# ● tipo_dato: un string que representa el tipo de dato a sanitizar. Puede
# tomar los valores: ‘string’, ‘entero’ y ‘flotante’
# La función deberá sanitizar el valor del diccionario correspondiente a la clave
# y al tipo de dato recibido
# Para sanitizar los valores se deberán utilizar las funciones creadas en los
# puntos 3.1, 3.2, 3.3 y 3.4

# Se deberá validar:
# ● Que tipo_dato se encuentre entre los valores esperados (‘string, ‘entero,
# ‘flotante)’ la validación debe soportar que nos lleguen mayúsculas o
# minúsculas. En caso de encontrarse un valor no válido informar por
# pantalla: ‘Tipo de dato no reconocido’

# ● Que clave exista como clave dentro del diccionario heroe. En caso de
# no encontrarse, informar por pantalla: ‘La clave especificada no
# existe en el héroe’. (en este caso la validación es sensible a
# mayúsculas o minúsculas)
# Ejemplo de llamada a la función válida:
# sanitizar_dato(dict_personaje, “altura”, “Flotante”)
# La función deberá devolver True en caso de haber sanitizado algún dato y
# False en caso contrario.

def sanitizar_dato(heroe:dict,clave:str,tipo_dato:str)->bool:

    retorno=False    
    # patron=r"[0-9]"
    # resultado=re.search(patron,tipo_dato)

    clave=clave.lower()
    tipo_dato=tipo_dato.lower()

    # if tipo_dato not in ["flotante", "entero", "string"]:
    if tipo_dato != "flotante" and tipo_dato!= "entero" and tipo_dato!= "string":
        print("Tipo de dato no reconocido")
        retorno=False

    if clave not in heroe:
        print("La clave especificada no existe en el heroe")
        retorno=False

    # if tipo_dato == "entero":
    #     valor=heroe[clave]
    #     heroe[clave]=sanitizar_entero(valor)
    #     retorno = True

    # elif tipo_dato == "flotante":
    #     valor=heroe[clave]
    #     heroe[clave]=sanitizar_flotante(valor)
    #     print(heroe[clave])
    #     retorno = True

    # elif tipo_dato=="string":
    #     valor=heroe[clave]
    #     heroe[clave]=sanitizar_string(valor)
    #     print("string")
    #     retorno = True

    match tipo_dato:
        case "entero":
            valor=heroe[clave]
            heroe[clave]=sanitizar_entero(valor)
            print(heroe[clave])
            retorno = True            
        case "flotante":
            valor=heroe[clave]
            heroe[clave]=sanitizar_flotante(valor)
            print(heroe[clave])
            retorno = True            
        case "string":
            valor=heroe[clave]
            heroe[clave]=sanitizar_string(valor)
            print("string")
            retorno = True

    return retorno

# 3.5. Crear la función 'stark_normalizar_datos’ la cual recibirá como parámetros:
# ● lista_heroes: la listas personajes
# La función deberá recorrer la lista de héroes y sanitizar los valores solo de las
# siguientes claves: ‘altura’, ‘peso’, ‘color_ojos’, ‘color_pelo’, ‘fuerza’ e
# ‘inteligencia’
# ● Un vez finalizado el proceso mostrar el mensaje ‘Datos normalizados’,
# ● Validar que la lista de héroes no esté vacía para realizar sus acciones,
# caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía”
# ● La función no retorna nada
# ● Reutilizar la función sanitizar_dato

def stark_normalizar_datos(lista_heroes:list):
    valor=False
    if len(lista_personajes)>0:

        for i in range(len(lista_heroes)):
            valor=True
            print(i)
            sanitizar_flotante(lista_heroes[i]["altura"])
            sanitizar_dato(lista_heroes[i],"altura","flotante")

            sanitizar_flotante(lista_heroes[i]["peso"])
            sanitizar_dato(lista_heroes[i],"peso","flotante")

            sanitizar_string(lista_heroes[i]["color_ojos"])
            sanitizar_dato(lista_heroes[i],"color_ojos","string")

            sanitizar_string(lista_heroes[i]["color_pelo"])
            sanitizar_dato(lista_heroes[i],"color_pelo","string")

            sanitizar_entero(lista_heroes[i]["fuerza"])
            sanitizar_dato(lista_heroes[i],"fuerza","entero")

            sanitizar_string(lista_heroes[i]["inteligencia"])
            sanitizar_dato(lista_heroes[i],"inteligencia","string")


            # print("Datos normalizados")

            # # sanitizar_dato(lista_heroes[i],"altura","string")
            # sanitizar_flotante(i["peso"])
            # sanitizar_string(i["color_ojos"])
            # sanitizar_string(i["color_pelo"])
            # sanitizar_entero(i["fuerza"])
            # sanitizar_string(i["inteligencia"])
    else:
        print("Lista de heroes vacia")

    if valor:
        print("Datos normalizados")
        
    

# 4.1. Crear la función ‘generar_indice_nombres’ la cual recibirá como parámetro:
# ● lista_heroes: la lista de personajes
# La función deberá iterar la lista de personajes y generar una lista donde cada
# elemento es cada palabra que componen el nombre de los personajes.

# Por ejemplo la lista que se deberá retornar tiene la siguiente forma:
# [‘Howard’, ‘the’, ‘Duck’, ‘Rocket’, ‘Raccoon’, ‘Wolverine’, ... ]
# La función deberá validar que:
# ● La lista contenga al menos un elemento
# ● Todos los elementos de lista_heroes sean del tipo diccionario
# ● Todos los elementos contengan la clave ‘nombre’
# En caso de encontrar algún error, informar por pantalla: ‘El origen de datos no
# contiene el formato correcto’

def generar_indice_nombres(lista_heroes:list):

    # espacio=" "
    lista_vacia=[]

    for heroe in range(len(lista_heroes)):
        # espacio = " "
        print(lista_heroes[heroe]["nombre"])
        nombre=lista_heroes[heroe]["nombre"]
        nombre_split=nombre.split()
        print(nombre_split)
        # nombres_unidos=espacio.join(nombre_split)
        lista_vacia.extend(nombre_split)

    print(lista_vacia)

def generar_indice_otro(lista_heroes:list):

    lista_vacia=[]

    for heroe in lista_heroes:
        # nombre=heroe["nombre"]
        nombre=heroe["nombre"].split()
        for i in nombre:
            lista_vacia.append(i)

    print(lista_vacia)

def generar_indice_otro_1(lista_heroes:list):

    lista_vacia=[]

    for heroe in lista_heroes:
        nombre=heroe["nombre"]
        nombre=nombre.split()
        lista_vacia=lista_vacia+nombre
    # print(lista_vacia)
    




        # coma=","
        # nombre_unidos_con_coma=coma.join(nombre_split)
        # print(nombre_unidos_con_coma)

        # split_nombre=heroe["nombre"].split()
        # valor=espacio.join(split_nombre)
        # print(f"{valor}")

# 4.2. Crear la función ‘stark_imprimir_indice_nombre’ la cual recibirá como
# parámetro:
# ● lista_heroes: la lista de personajes
# La función deberá mostrar por pantalla el índice generado por la función
# generar_indice_nombres con todos los nombres separados con un guión.
# Por ejemplo:
# Howard-the-duck-Rocket-Raccoon-Wolverine...

def stark_imprimir_indice_nombre(lista_heroes:list):
    
    generar_indice_otro_1(lista_heroes)
    listavacia=[]
    for i in range(len(lista_heroes)):
        print("i")
        print(i)
        nombre=lista_heroes[i]["nombre"].split()
        print(nombre)
        valor="-".join(nombre)
        print(valor)
        listavacia.append(valor)
    #     for e in nombre:
    #         print("e")
    #         print(e)
    #         guion="-"
    #         valor=guion.join(e)
    #         listavacia.append(valor)

    resultado_final="-".join(listavacia)
    
    print(resultado_final)

    # lista=[]
    # for i in range(len(lista_heroes)):
    #     nombre=lista_heroes[i]["nombre"]
    #     nombre=nombre.split()
    #     print(nombre)
    #     for e in nombre:
    #         e=e.split()
    #         for a in e:
    #             a=a.split()
    #             print(a)
    #             print("asd")
    #             resultado="-".join(a)
    #             lista.append(resultado)

    # print(lista)



        # guion="-".join(nombre)
        # resultado=lista.append(guion)
    # guion = "-"
    # nombres_guion = guion.join(nombres)
    # print(resultado)







continuar = True

while continuar:

    opcion=menu()
    match opcion:
        case "1":
            c=sanitizar_entero("-8")
            print(c)
        case "2":
            a=sanitizar_flotante("1.12")
            print(a)
        case "3":
            m=sanitizar_string("color_ojos","")
            print(m)
        case "4":
            l=sanitizar_dato(lista_personajes[0],"altura","flotante")
            print(l)
        case "5":
            stark_normalizar_datos(lista_personajes)
            # print("opcion")
        case "6":
            generar_indice_nombres(lista_personajes)
            # print("opcion")s
        case "7":
            generar_indice_otro(lista_personajes)
            # print("opcion")
        case "8":
            generar_indice_otro_1(lista_personajes)
            # print("opcion")
        case "9":
            stark_imprimir_indice_nombre(lista_personajes)
            # print("opcion")
        case "10":
            continuar=False
            print("CHAU")
        