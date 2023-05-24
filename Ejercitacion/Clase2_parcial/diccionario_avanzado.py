#DICCIONARIO:
#las claves de un diccionario deben ser unicas, pero los valores pueden repetirse
#es una coleccion de elememtos
#usamos diccionario para guardar todos los datos de una entidad o persona, de un alumno
#las claves deben ser unicas, cada elemento tiene una clave y un valor, accedemos al valor a travez del indice
#dicinario={}
 
#DICCIONARIO ANIDADO:
#python habilita la posibiladad de poder tener como valor de un diccinoaroi cualquier objeto, inclusive otro diccionario
#diccionario={"name":"martin","calle"{"number","123"}}
#print(diccinario[""])

#RECCORER DICCIONARIO
#se usa for para recorrer cualquier iterable, 
#diccionario={"name":"marty","edad":"12"}
#for clave in diccinario:
# print(clave,diccinario[clave]) #name marty edad 18 

#COPIAR DICCINARIO
#no es posible copiar un diccionario con el igual de asignacion
#hay 2 formas: superficial y profunda
#superfificial(shadow copy) se copian las referencias

#GET
#permite consultar el valor de una clave determinada Y a partir de la clave q le pasamos nos devuelve el dato o valor
#El segundo parametro es el valor a devolver si no se encuentra la clave, este parametro es opcional 
#diccionario={"name":"Marty","edad":18}
#print(diccionario.get("name","NO NAME")) # Marty
#print(diccinario.get("nombre","NO NAME")) #NO NAME

#KEYS:
#el metodo keys devuelve una lista con todas las claves del diccionario 
#diccionario={"name":"Marty","edad":18}
#print(list(diccinario.keys())) #["name","edad"]

#VALUES:
#este metodo devuelve una lista con todos los valores del diccinario, a diferencia de keys, values devuelve lo mismo pero los valores de las claves
#diccionario={"name":"Marty","edad":18}
#print(list(diccinario.values())) #["Marty","18"]


#ITEMS:
#este metodo devuelve una lista con las claves y valores del diccinario. Si se convierte en lista se puede acceder utilizando el indice
##diccionario={"name":"Marty","edad":18}
#print(list(diccinario.items())) #[("name","Marty"),("edad",18)] #lo casteamos a list por eso me devuelve ne forma de lista y en forma de tupla por eso 
                                                                # esta entre parentesis cada elemento osea que es inmutable

#POP
#este metodo busca y elimina la key que se pasa como parametro y devuelve su valor asociado. Da error si la key no existe
#tambien se puede pasar un segundo parametro en caso que la key no se ha encontrado. En este caso si no se encuentra da error
##diccionario={"name":"Marty","edad":18}
#diccionario.pop("edad")
#print(diccinario) #{"name":"Marty"}

#IMPORTANTE LO QUE PODRIA HACER CON POP TA QUE DEVUELVE EL VALOR ASOCIADO,ES UNA LISTA DE LO QUE FUE ELIMINADO  
#herramientas_eliminadas = []
#herramientas_eliminadas.append(copia_actualizada.pop(-2))

#TAMBIEN SE PUEDE PASAR UN SEGUNDO PARAMETRO QUE ES VALOR A DEVOLVER SI LA KEY NO SE HA ENCONTRADO. EN ESTE CASO SI NO SE ENCUENTRO NO HABRIA ERROR
##diccionario={"name":"Marty","edad":18}
#valor_eliminado = diccionario.pop("year","none")
#print(valor_eliminado) #none

#UPDATE
#este metodo se llama sobre un diccionario y tiene como entrada otro diccinario. Los valores son actualizados y si alguna clave del nuevo 
#diccionario no esta es añadida
##diccionario={"name":"Marty","edad":18}
#diccionario.update({"year":"1973"})
#print(diccinario) #{"name":"Marty","edad":18,"year":"1973"}
#TAMBIEN PUEDO HACER UN UPDATE DE ALGUN DATO QUE EXISTE Y PUEDO MODIFICARLO
#diccionario.update({"edad":33})
#print(diccinario) #{"name":"Marty","edad":33}

#CLEAR
#este metodo elimina todo el contenido del diccinario 
##diccionario={"name":"Marty","edad":18}
#diccinario.clear()
#print(diccinario) # {} ELIMINA EL CONTENIDO DEL DICCINARIO, NO ELIMINA EL DICCIONARIO

#CLEAR,POP,ITEMS,GET ESTAS FUNCIONES NOS DAN VENTAJA Y AHORRA MUCHO TIEMPO YA QUE ANTES LO TENIAMOS QUE PROGRAMAR. 



# # lista_2 = lista_1 -> Lo que hace es copiar la referencia (dirección de memoria) de la lista, por lo que ambas variables 
# van a modificar la misma lista ya que apuntan al mismo espacio de memoria

# # lista_2 = lista_1.copy() -> El shallow copy (copia de superficie) copia los valores que contiene las variables en caso
#  que sean variables simples (tipo int, float o str). En caso de que los datos de la lista sean datos compuestos (un diccionario, otra lista) 
# lo que copia en ese índice es la referencia de la variable

# # lista_2 = deepcopy(lista_1) -> Hace una copia de TODOS los valores de lista_1, sean simples o compuestos.
# #  Este ultimo te garantiza que si tu lista tiene datos compuestos y no queres tocar la lista original puedas manejar una copia y
# #  modificarla sin afectar a la primera