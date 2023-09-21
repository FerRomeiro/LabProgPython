#USAMOS FOR SIN USAR BANDERA PERO SOLO SI COMPARAMOS CON int O float, NO FUNCIONA CON STRING YA QUE PARA ESO DEBERIAMOS PASARLO A float COMO HICIMOS EN EL SEGUNDO CASO

from data_stark import lista_heroes

nombre_heroe = lista_heroes[0] ["nombre"] 
mayor_altura = lista_heroes[0]["altura"]

for heroe in lista_heroes:

    if heroe["altura"] > mayor_altura: 
        mayor_altura = heroe["altura"] 
        nombre_heroe= heroe["nombre"]

print(nombre_heroe,mayor_altura)


#USAMOS FOR SIN BANDERA PERO SI EL DATO COMO EN ESTE CASO "altura" ES UN STRING, LO PASAMOS A float Y ADENTRO DEL FOR AL ITERAR HACERMOS LO MISMO PARA DESPUES COMPARAR

from data_stark import lista_heroes

nombre_heroe = lista_heroes[0] ["nombre"] 
mayor_altura = float(lista_heroes[0]["altura"])

for heroe in lista_heroes:
    altura=float(heroe["altura"])
    if altura > mayor_altura: 
        mayor_altura = float(heroe["altura"]) 
        nombre_heroe= heroe["nombre"]

print(nombre_heroe,mayor_altura)