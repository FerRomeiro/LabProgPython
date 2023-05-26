#



lista =[ {"edad":"25","nota":9},
        {"nombre":"Jose","edad":34,"nota":8},
        {"nombre":"Sol","edad":46,"nota":7},
        {"nombre":"Beto","edad":28,"nota":6},   
        ]


##Da error ya q el primer elemnto del diccionaroi no tiene el key "nombre"
# for e_nombre in lista:
#     print(e_nombre["nombre"])




#Con metodo get() muestra el valor por defecto o none
#con get nos da la key por defecto, ahora si no existe la key no da error 
for e_nombre in lista:
    print(e_nombre.get("nombre","SIN NOMBRE"))#con le digo de la key "nombre" dame el valor y si no existe dame "sin nombre" y si no pongo nada "None"

#con esta opcion uso enumerate y uso el indice del elemento que no tiene key para indicar el indice que me devuelve enumarate 
for i,e_nombre in enumerate(lista): #con enumerate traigo el indice y el elemento, me devuelve 2 valores, el indidce y el elemento
    nom=e_nombre.get("nombre","no hay nombre")

    if nom==("no hay nombre"):
        vacio=i
        print("posicion sin key:",i)
