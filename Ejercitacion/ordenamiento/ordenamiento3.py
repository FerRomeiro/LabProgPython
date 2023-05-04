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
contador_while=0

while bandera_swap:
    bandera_swap=False
    for i in range(len(lista)-1):    
        # if lista[i] > lista[i+1]:
        if lista[i]["nombre"]>lista[i+1]["nombre"]:
            
            aux=lista[i]["nombre"]
            lista[i]["nombre"]=lista[i+1]["nombre"]
            lista[i+1]["nombre"]=aux

            aux=lista[i]["Edad"]
            lista[i]["Edad"]=lista[i+1]["Edad"]
            lista[i+1]["Edad"]=aux

            aux=lista[i]["Nota"]
            lista[i]["Nota"]=lista[i+1]["Nota"]
            lista[i+1]["Nota"]=aux
            
            bandera_swap=True

print(lista)

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[4])
