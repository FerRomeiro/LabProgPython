#marisa

#ATRIBUTOS=DATOS DEL OBJETO
#METODOS=ACCIONES DEL OBJETO

#

persona_3={"nombre":"Marina","apellido":"Cardozo","edad":25,"genero":"femenino"}

persona_3["dni"]=123131

print(persona_3) #nos imprime toda esa entidad, pero tiene limitaciones

persona_3["edad"]=50

print(persona_3) #me reemplaza la edad ya existente, me la pisa esto seria una limitacion



class Usuario: #LAS CLASES SON PLANTILLA DE UNA ENTIDAD 

    tipo="Basico"

    def __init__(self,nombre,apellido,password,edad=0):
            
            self.nombre=nombre 
            self.apellido=apellido
            self.edad=edad
            self.password=password

    def presentarse(self):
        print(f"Hola mi nombre es {self.nombre} {self.apellido}, tengo {self.edad} años y soy {self.tipo}")


#INSTANCIA PERSONA
usuario_uno=Usuario("Pedro","Perez","1234","20") #usuario_uno es un objeto 

print(usuario_uno.password) #no deberia suceder esto porque cualquier tendria acceso al password
print(usuario_uno.nombre) #el atributo nombre es publico, lo q quiere decir q puedo acceder haciendo punto desde un objeto desde su propia instancia
                        #NO ES RECOMENDADO QUE LOS ATRIBUTOS DE UNA CLASE SE PUEDAN ACCEDER DESDE AFUERA,SIEMPRE DEBEN SER LOS ATRIBUTOS PROTECTED O PRIVADOS
                        #EL PROTECTED ES UNA CONVENCION ASI Q ES MEDIO ENGAÑOSO
                        

print(usuario_uno.__password) #esto si esta bien, ya q seria el atributo privado y no puedo acceder desde el objeto







class Usuario: #LAS CLASES SON PLANTILLA DE UNA ENTIDAD 

    tipo="Basico"

    def __init__(self,nombre,apellido,password,edad=0):
            
            self.nombre=nombre 
            self.apellido=apellido
            self.edad=edad
            self.__password=password

    def password(self):
        return self.__password
    
    def presentarse(self):
        print(f"Hola mi nombre es {self.nombre} {self.apellido}, tengo {self.edad} años y soy {self.tipo}")


#INSTANCIA PERSONA
usuario_uno=Usuario("Pedro","Perez","1234","20") #usuario_uno es un objeto 

print(usuario_uno.password) #no deberia suceder esto porque cualquier tendria acceso al password
print(usuario_uno.nombre)