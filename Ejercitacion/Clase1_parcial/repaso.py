
#1) Se tiene la siguiente lista [100.00, 200.00, 400.00, 800.00]
# mapearla realizando un descuento del 15% a cada elemento de lista. Por ultimo mostrar la lista mapeada.


#OPCION 1
from random import shuffle
from copy import deepcopy
lista=[1,3,4,2,5,6,7]
print(lista)
lista_2=deepcopy(lista)
print(lista_2)
shuffle(lista_2)
print(lista_2)

#OPCION 2

lista_3=[100.00,200.00,400.00,800.00]
lista_4=deepcopy(lista_3) #NO ES NECESARIO HACER UNA COPIA PERO IGUAL LO HAGO 
lista_descuento=list(map(lambda x:x*0.85,lista_4))
print(lista_3)
print(lista_descuento)

#OPCION 3 PRO

def mapear(lista):
    
    lista_mapeada=list(map(lambda x : x["precio"]["sin_iva"] + (x["precio"]["sin_iva"]*21/100),lista))

    return lista_mapeada



#2) Se tiene la siguiente lista ["Manuel","Ana","Esteban","Lia"] mezclar la lista, mostrarla solamente si fue efectivo el mezclado.

#OPCION 1 
from random import shuffle
from copy import deepcopy

lista=["Manuel","Ana","Esteban","Lia"]
copia=deepcopy(lista)
shuffle(copia)

flag_shuffle=True

while flag_shuffle:
    if copia == lista:
        flag_shuffle = False
        shuffle(copia)
        
    else:
        flag_shuffle=True
        print(copia)
        break

#OPCION 2
from random import shuffle
from copy import deepcopy

lista=["Manuel","Ana","Esteban","Lia"]
copia=deepcopy(lista)
shuffle(copia)
contador=0

while True:
    
    if lista == copia:
        print("lista original: ", lista)
        print("copia: ",copia)
        print(contador)
        break
    else:
        shuffle(copia)
        print("lista mezclada: ",copia)
    

    contador=contador+1

