




# #la sobrecarga seria sobreescribir un comportamiento, darle un comportamiento q me interese
# #como si una clase q invento quiero q haga cierto comportamiento cuando yo ejecute cierto comando 



# # EXPLICACION

# def __str__(self):
#     return "{0}-{1}-{2}".format(self.apellido,self.nombre,self.edad)

# def __lt__(self,item): #esto tiene q retornar un bool
#     return self.edad < item.edad #aca se sobrecarga el operador <, voy a tener dos objetos de tipo dato y voy agarrar el atributo edad de uno y de otro para comparar
#                                 #y decir quien es mas grande
#                                 #cuando lo estoy sobrecargando yo decido en base a q lo voy a sobrecargar, q es lo q yo considero q un objeto sea mas grande 
#                                 #q otro, q dato hace q uno sea mas grande q otro q en este caso es edad, pero podria ser cualquier cosa como calificacion
#                                 #ventas, etc
#                                 #LOS OPERADORES RELACIONABLES SIEMPRE DEVUELVEN UN BOOL 
# lista=[1,2,3,"a"]
# print(lista) #no me recorre la lista, sin embargo me imprime todos los elementos de la lista
# #ahora si quiero imprimir:
# print(usuario_uno) #lo ejecuto con la sobrecarga del str
# usuario_uno.presentarse() #aca es un metodo de objeto que realiza un print

# print(usuario_uno < usuario_dos) #esta comparacion se realiza en base al atributo edad





#LO PONGO EN PRACTICA ACA.

persona_3={"nombre":"Marina","apellido":"cardozo","edad":25,"genero":"femenino"}


persona_3["dni"]=1232323

print(persona_3)

persona_3["edad"]=50
print(persona_3)

persona_3["dni"]="dfsdsf"

print(persona_3)


class Usuario:

    #ATRIBUTO DE CLASE O "ESTÁTICO"
    tipo = "Basico"

    #CONSTRUCTOR (donde se definen e inicializan los atributos de instancia)
    def __init__(self, nombre, apellido, password,estrellas = 0, edad = 0):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.estrellas = estrellas      
        self.__password = password   

    def nombre(self):
        return self.nombre.upper()

    #getter, retornarte el atributo privado
    @property
    def password(self):
        return self.__password

    #setter te permite modificar el atributo privado
    @password.setter
    def password(self,new_password):
        self.__password = new_password

    def cambiar_password(self,old_password,new_password):
        if old_password == self.__password:
            self.__password = new_password
        else:
            print("La pass es incorrecta")
    
    def __str__(self):
        return "{0} - {1} - {2}".format(self.apellido,self.nombre,self.edad)

    def __lt__(self,item): #esto tiene que retornar un boolean
        return self.estrellas < item.estrellas

    def presentarse(self):
        print(f"¡Hola! Mi nombre es {self.nombre} {self.apellido}, tengo {self.edad} años y soy {self.tipo}")

    


usuario_uno = Usuario("Pedro", "Perez", "12234",2,20) #atributo estrellas es 2
usuario_dos = Usuario("Marina", "Cardozo", "12234",30) #atributo estrellas es 30

print(usuario_uno.nombre) #el atributo nombre, es publico 
print(usuario_uno.password) #atributo es privado, que no puedo acceder desde el objeto 
usuario_uno.password = "sadsadf"
print(usuario_uno.password)

lista = [1,2,3, "a"]
print(lista)
print(usuario_uno) #con el metodo magico
usuario_uno.presentarse() #un metodo de objeto que realiza un print

print(usuario_uno < usuario_dos) #esta comparacion se realiza en base al atributo estrellas(calificacion de ventas)