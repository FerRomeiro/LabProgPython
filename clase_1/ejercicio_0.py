lista_numero = list(range(5))
print(lista_numero) # 0,1,2,3,4

lista_numero = list(range(10, 20, 2)) #inicio, fin, salto 
print(lista_numero) #10,12,14,16, 18

#for 
#es distinto en python 

lista_numero = [1,2,4,5,77,-1]

for numero in lista_numero #numero es una variable q itera la lista numeros
                         #el for toma de la lista y lo imprime en print
                         #asi hasta que se acaben los datos, q son 6 numeros

    print(numero,end="")   #end="" es el espacio q hay entre numeros

    #salida: 1 2 4 5 77 -1 #imprime 1 por 1 los elementos de la lista_numero
