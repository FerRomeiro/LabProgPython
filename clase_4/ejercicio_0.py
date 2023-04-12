opciones = [1,2,3,"4)salir"]

def menu_principal(opciones):
    for i in opciones:
        print(i)
    opcion_elegida = input("Elija opcion: ")

    return opcion_elegida

while True:
    opcion_elegid=menu_principal(opciones)
    int(opcion_elegid)
    match opcion_elegid:
        case 1:
            print("Opcion 1")
        case 2:
            print("opcion 2")
        case 3:
            print("opcion 3")
        case 4:
            print("opcion 4")