from random import shuffle
from copy import deepcopy
lista=[1,3,4,2,5,6,7]
print(lista)
lista_2=deepcopy(lista)
print(lista_2)
shuffle(lista_2)
print(lista_2)

# Se tiene la siguiente lista [100.00, 200.00, 400.00, 800.00]
# mapearla realizando un descuento del 15% a cada elemento de lista. Por ultimo mostrar la lista mapeada.
lista_3=[100.00,200.00,400.00,800.00]
lista_4=deepcopy(lista_3)
lista_descuento=list(map(lambda x:x*0.85,lista_4))
print(lista_3)
print(lista_descuento)