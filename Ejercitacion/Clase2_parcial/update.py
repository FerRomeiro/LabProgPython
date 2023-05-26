lista =[ {"edad":25,"nota":9},
        {"nombre":"Jose","edad":34,"nota":8},
        {"nombre":"Sol","edad":46,"nota":7},
        {"nombre":"Beto","edad":28,"nota":6},   
        ]

for e_nombre in lista:
    print(e_nombre.get("nombre","SIN NOMBRE"))

dic_cero=dict(lista[0])
dic_cero.update({"nombre":"Soy Matias"}) #AGREGO LA KEY "nombre" AL PRIMER ELEMENTO DE LA LISTA, SIEMPRE DEBO ASEGURARME QUE LA KEY ESTE EN EL DICCINARIO
                                    #SE DEBE VALIDAR QUE LA KEY nombre ESTE EN EL DICCIONARIO O EXISTA
lista[0]=dic_cero
print(lista)


#AHORA SI EXISTE EL NOMBRE
lista =[ {"edad":25,"nota":9},
        {"nombre":"Jose","edad":34,"nota":8},
        {"nombre":"Sol","edad":46,"nota":7},
        {"nombre":"Beto","edad":28,"nota":6},   
        ]

for e_nombre in lista:
    print(e_nombre.get("nombre","SIN NOMBRE"))

dic_cero=dict(lista[1]) #EXISTE EN LA POSICION 1 LA KEY nombre ENTONCES SOLO ACTUALIZA EL NOMBRE
dic_cero.update({"nombre":"Soy Matias"}) #AGREGO LA KEY "nombre" AL PRIMER ELEMENTO DE LA LISTA, SIEMPRE DEBO ASEGURARME QUE LA KEY ESTE EN EL DICCINARIO
                                    #SE DEBE VALIDAR QUE LA KEY nombre ESTE EN EL DICCIONARIO O EXISTA
lista[1]=dic_cero
print(lista)

