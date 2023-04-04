lista_numero = list(range(5))
print(lista_numero) # 0,1,2,3,4

lista_numero = list(range(10, 20, 2)) #inicio, fin, salto 
print(lista_numero) #10,12,14,16, 18

#for 
#es distinto en python 

lista_numero = [1,2,4,5,77,-1]

# el for solo puede iterar a objetos iterables 

for numero in lista_numero: #numero es una variable q itera la lista numeros
                         #el for toma de la lista y lo imprime en print
                         #asi hasta que se acaben los datos, q son 6 numeros

    print(numero,end="")   #end="" es el espacio q hay entre numeros

    #salida: 1 2 4 5 77 -1 #imprime 1 por 1 los elementos de la lista_numero

#break 
#rompe un ciclo repetitivo 
lista_numero = [1,2,3,4,5]
for numero in lista_numero:
    if(numero==5):
        break
    print(numero,end="")

#salida: 1,2,3,4

#match 
#es una especie de switch 
match status:
        case 400:
          return "Error de request"
        case 404:
          return "no encontrado"
#Tambien se puede se puede usar el |
match status:
        case 400 | 401:
          return "Error de request"
        case 404:
          return "no encontrado"
    
#list 

lista=[1,"hola",3.67]
print(type(lista)) # <class "list">
print(lista[1]) #hola el 1 es el indice
lista[1]="chau"
print(lista[1]) #chau

#tuplas
# # es lo mismo q la lista solo que no podemos cambiar los valores
lista=tuple([1,"hola",3.67])

#diccionario 
#aca tengo la clave y a partir de esa el valor
diccionario = {"nombre" : "juan", "edad" : 21}
print(diccionario["nombre"]) #"juan"
print(diccionario["edad"]) # 21

#set 
#