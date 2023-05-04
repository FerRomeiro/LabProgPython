#hay una manera de optimizar el algoritmo de swap 


# print(lista)
# for i in range(len(lista)-1): 
#     for j in range (i+1, len(lista)):
#         if lista[i] > lista[j]:
#             aux=lista[i]
#             lista[i]=lista[j]
#             lista[j]=aux
# print(lista)

#VAMOS A BUSCAR LA MANERA QUE SOLO HAYA UN MOVIMIENTO CUANDO TENGO QUE ORDENAR OSEA CUANDO SE CUMPLA LA CONDICION
#REEMPLAZAMOS EL FOR POR UN WHILE, PORQUE EL FOR VA A RECORRER DEL PRIMERO AL ULTIMO Y CON UN WHILE PUEDO AGREGARLE UNA CONDICION PARA EVITAR ESO
#SE EJECUTARIA CUANDO SE CUMPLA LA CONDICION DEL WHILE Y ASI EVITO RECORRER DEL PRIMEOR AL ULTIMO COMO PASARIA CON FOR

lista = [2,5,3,1,6,4]
bandera_swap=True
contador_while=0
contador_for=0
print(lista)

while bandera_swap:
    bandera_swap=False
    contador_while=contador_while+1

    for i in range(len(lista)-1):
        contador_for=contador_for+1
        
        if lista[i] > lista[i+1]:
            aux=lista[i]
            lista[i]=lista[i+1]
            lista[i+1]=aux
            bandera_swap=True
    # bandera_swap=False
    
print(lista)
print(contador_for)
print(contador_while)
        