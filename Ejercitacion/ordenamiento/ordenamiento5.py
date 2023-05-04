#ACA HACEMOS LA FUNCION DE ORDANMIENTO QUE USAMOS EN EL ANTERIOR

lista=[{"nombre":"Tito", "Edad":32,"Nota":6},
    {"nombre":"Job", "Edad":37,"Nota":7},
       {"nombre":"Juan", "Edad":28,"Nota":8},
       {"nombre":"Ana", "Edad":25,"Nota":9},
       {"nombre":"Jose", "Edad":23,"Nota":4}]



def ordenar(lista:list,clave:str,tipo:str)->list:

    bandera_swap=True
    while bandera_swap:
        bandera_swap=False
        for i in range(len(lista)-1): 
            if tipo=="ASC" and lista[i][clave]>lista[i+1][clave]:
                aux=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=aux
                bandera_swap=True
            elif tipo=="DESC" and lista[i][clave]<lista[i+1][clave]:
                aux=lista[i]
                lista[i]=lista[i+1]
                lista[i+1]=aux
                bandera_swap=True

    return lista            


    
lista_ordenada=ordenar(lista,"Nota","ASC")
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
print(lista_ordenada)
lista_ordenada=ordenar(lista,"Nota","DESC")
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
print(lista_ordenada)
