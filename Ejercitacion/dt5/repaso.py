from data_stark import lista_personajes
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
    patron = r"[a-zA-Z]+" # HAY QUE PONER PATRON PARA USAR RESEARCH
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









continuar = True

while continuar:

    opcion=menu()
    match opcion:
        case "1":
            c=sanitizar_entero("-8")
            print(c)
        case "2":
            print("opcion")
        case "3":
            print("opcion")
        case "4":
            print("opcion")
        case "5":
            print("opcion")
        case "6":
            print("opcion")
        case "7":
            print("opcion")
        case "8":
            print("opcion")
        case "9":
            print("opcion")
        case "10":
            continuar=False
            print("CHAU")
        