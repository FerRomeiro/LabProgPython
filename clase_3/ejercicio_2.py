#Funcion para administrar un menu
#Que hace la funcion?? muestra un menu
#Que retorna la funcion?? retorna un valor, "opcion"
#Que recibe la funcion? recibe un input


def mostrar_Menu():

    print("1. Mostrar minimo")
    print("2. Mostrar maximo")    
    print("3. Mostrar promedio")
    print("4. Salir")
    opcion = input("Eliga una opcion: ")
    opcion = int(opcion)
    #print("Elegiste: ",opcion)
    return opcion

continuar = True
    #print("Elegiste la opcion: ",opcion_Elegida)    

while continuar:
    opcion_Elegida = mostrar_Menu() # TENEMOS QUE GUARDAR EL VALOR 
    if opcion_Elegida == 4:
        print("Chau")
        continuar = False
    elif opcion_Elegida == 3:
        print("Elegiste opcion 3")
    elif opcion_Elegida == 2:
        print("Elegiste opcion 2")
    elif opcion_Elegida == 1:
        print("Elegiste la opcion 1")
