#LA FUNCINO LAMBDA O ANONIMA:
#es un tipo de funcion que no tiene un nombre que la defina, son funciones sumamente pequeñas de poco codigo porque tiene que ver con la manera
#de utilizarla o llamarla, es muy breve, trabaja de manera simple.
#Ejemplo:
#def sumar(a,b):
#
#return a+b
#
#lambda a,b : a + b (es la forma abreviada) 
#la palabra reservada en este caso es lambda y no def
#no tiene nombre es anonima 
#se llama asi print(lambda a,b : a+b(4,5)) #9
#OPERADORES TERNARIOS:
#los operadores ternarios son conocidos como expresiones condicionales, evaluan si una expresion es Veradera o no
#se llama ternario porque se decide lo que ocurre si es verdadero o lo q ocurre si es falso
#resultado_if_true if a < b else resultado_if_false
#mayor = lambda a,b : a if a>b else b
#print(mayor(4,5)) # 5
#LISTA:
#son uno de los tipos mas vestiles del lenguaje ya que permiten almacenar un conj arbitrario de datos
#cuando hablamos de versatilibilada es q me permite hacer muchas cosas
#lista=["marty","emmet","biff"]
#
#lista[1]="jennifer"

#LISTA ANIDADAS:
#es algo adentro de algo, nos permite tener como elemento de una lista cualquier objeto, incluse otra lista
#lista_1 = [["asd","asdasd"],["qrqw","asdasdas"]]
#  RECORRER LISTA:
#se recorre con un for
#COPIAR LISTA:
#se puede copiar de dos formas
#superficial(shallow copy)
#profunda(deep copy)
#SUPERFICUAL: solamente se copian las referencias a los elemntos contenidos en el objeto 
#un objeto es una referencia en memoria
#lista_1=[["asdasd","McFly"],"marty","emmet","biff"]
#lista_2=lista_1.copy # lista[:] es equivalente
#lista_1[0][0]="MARTY"
#print(lista_2)
#[["MARTY","McFly"],"marty","emmet","biff"]
#DEEP COPY:si el objeto tiene subobjetos estos se copian recursivamente, copia de manera independiente y no como referencia como el an terio 
#from copy import deepcopy
#lista_1=[["marty","marton"],"asd","fds"]
#lista_2=deepcopy(lista_1) # opcion 1
#lista_1[0][0]="MARTY"
#print(lista_2)
#[["marty","marton"],"asd","fds"]
#APEEND:
#es una funcion asociada a ese objeto, append añade un elemento al final de la lista
##lista=["a","d","w"]
#lista.append("asd")
#print(lista) # []
#
#INSERT:
#añade un elemento a una poscicion o indice determinado le paso 2 parametro 
#el indice y el elemento que le inserto a la lista
##lista=["a","d","w"]
#lista.insert(1,"asd")
#print(lista) # []
#
#EXTEND:
#añade una lista a la lista inicial
###lista=["a","d","w"]
#lista.extend(["asd","asff"])
#print(lista) # []
#POP:
#elimina y retorna el elemento ubicado en el indice pasado por parametro, por defecto elmina el ultimo elemento
###lista=["a","d","w"]
#elemento_eliminado=lista.pop(1)
#print(lista) #["a","w"]
#print(elemento_eliminado) # "d"
#REMOVE():
#el metodo remove recibe como argumento un objeto y lo borra de la lista
###lista=["a","d","w"]
#lista.remove("d")
#print(lista) #["a","w"]
#INDEX:
#el metodo index recibe como parametro un objeto y devuelve el indice de su primera aparicion o ocurrencia xq puede estar mas de una vez el elemento
###lista=["a","d","w"]
#lista.index("asd")
#print(lista) # []
#ENUMERATE:
#podemos 
#ZIP:
#permite iterar multiples listas a la vez 
#MAP:
#pasa como parametro a una funcion a cada uno de los elementos de la lista dando como resultado uan nueva lista formada por los elementos q la funcion retorna
#FILTER
#la funcion filter filtra una lista de elementos para los que una funcion devuelve TRUE
#REDUCE:
#la funcionr reduce utiliza principalmente para llevar a cabo un caculo acumulativos sobre una lista de valores y devolver el resultado
#esta incluida en el modulo functools 
#SHUFFLE
#este metodo del modulo random y se usa para mezclar una lista
#SORT:
#ordena los elementos de menor a mayor por defecto, si quisiera ordenar de manera descendente se usa sort(reverse=True)
#sort(key=)
#el parametro key es para especificar una funcion que se llamara por cada elemento de la lista y su retorno se utilizara para hacer comparaciones
#


