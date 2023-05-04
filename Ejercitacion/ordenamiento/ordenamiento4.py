#VAMOS HACERLO DE UNA MANERA MAS OPTIMIZADA A LA ANTERIORlista=[{"nombre":"Tito", "Edad":32,"Nota":6},
#YA QUE EN EL ANTERIOR CASO TENIAMOS QUE ESCRIBIR CLAVE POR CLAVE PARA QUE AL ORDENAR POR NOMBRE LO DEMAS DATOS TAMBIEN CAMBIEN DE LUGAR JUNTO AL NOMBRE
#ACA HACEMOS ESO, MOVIENDO EL DICCIONARIO ENTERO
lista=[{"nombre":"Tito", "Edad":32,"Nota":6},
    {"nombre":"Job", "Edad":37,"Nota":7},
       {"nombre":"Juan", "Edad":28,"Nota":8},
       {"nombre":"Ana", "Edad":25,"Nota":9},
       {"nombre":"Jose", "Edad":23,"Nota":4}] #UNA LISTA DE DICCIONARIOS

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])

bandera_swap=True
while bandera_swap:
    bandera_swap=False
    for i in range(len(lista)-1): 
        if lista[i]["nombre"]>lista[i+1]["nombre"]:
            aux=lista[i]
            lista[i]=lista[i+1]
            lista[i+1]=aux
            bandera_swap=True
print(lista)
#SEGUN ASCII LOS NUMEROS DE LAS LETRAS MAYUSCULAS SON DISTINTOS A LAS MINUSCULAS EN CUANTO AL ORDEN SIEMPRE PASAR TODO A MIN O A MAYUS
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])