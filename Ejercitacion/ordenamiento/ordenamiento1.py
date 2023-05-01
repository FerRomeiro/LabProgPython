#Como hariamos para ordenar la lista ?? 
#estado inicial
lista = [2,5,3,1,6,4]
#primero debo recorrer la lista
#comparar cada numero con su vecino a la derecha 
#si el dato_que_contiene_el_indice_actual es mayor que el dato_que_contiene_el_indice_actual = 1
#swap
#
contador_for=0
contador_for_1=0




print(lista)
for i in range(len(lista)-1): #recorro i hasta q llegue a 6 de la lista para q compare con el 4
    # print(i)
    contador_for=contador_for+1

    for j in range (i+1, len(lista)):
        # print(j)
        contador_for_1=contador_for_1+1

        if lista[i] > lista[j]:#si tengo que ordenar de manera asc 
            aux=lista[i]
            lista[i]=lista[j]
            lista[j]=aux
print(lista) #ESTO SE LLAMA BURBUJEO "bubble sort"

print(contador_for)
print(contador_for_1)
#asi compararia
# i j j j j j
#   i j j j j
#     i j j j
#       i j j
#         i j



#i lista[i]   lista[i+1]  swap    lista 
#0   2           5         no     [2,5,3,1,6,4]
#1   5           3         si     [2,3,5,1,6,4]
#2   5           1         si     [2,3,1,5,6,4]
#3   5           6         no     [2,3,1,5,6,4]
#4   6           4         si     [2,3,1,5,4,6]
#5   6           FUERA DE RANGO 
#algoritmo
