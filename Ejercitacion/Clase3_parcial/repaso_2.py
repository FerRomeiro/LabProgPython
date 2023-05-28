#marisa


class Usuario: #LAS CLASES SON PLANTILLA DE UNA ENTIDAD 

    tipo="Basico"

    def __init__(self,nombre,apellido,password,edad=0):
            
            self.nombre=nombre 
            self.apellido=apellido
            self.edad=edad
            self.__password=password


    #ESTO ES PARA ACCEDER A ATRIBUTOS Q SON PRIVADOS 
    #ESTO ES UN GETTER, RETORNA EL ATRIBUTO PRIVADO(LEER)
    @property #SI NO PONDRIA PROPERTY NO ME IMPRIME, SOLO IMPRIME LA POSICION DE MEMORIA DEL PASSWORD. EL PROPERTY ES COMO UN INTERCEPTOR 
                #PROPERTY ES PROPIEDAD Y SIEMPRE VA CON EL self QUE ES EL OBJETO SOLAMENTE, A DIFERENCIA DE setter QUE ES DONDE SETEO EL NUEVO PASS 
    def password(self): #le decimo q me traiga x atributo
        return self.__password

    #SI QUISIERAMOS CAMBIAR LA CONTRASEÑA
    #ESTO ES UN SETTER Q TE PERMITE MODIFICAR EL ATRIBUTO PRIVADO (ESCRIBIR O MDIFICAR)
    @password.setter #ACA LO QUE VOY A SETEAR ES EL NUEVO PASSWORD POR ESO NO VA SOLO EL self ENTRE () SINO Q TAMBIEN VA new_password
    def password(self,new_password):
        self.__password=new_password
    
    def nombre(self): #TAMBIEN PUEDO ACCEDER ASI AUNQE ES LO MISMO QUE ESCRIBIR usuario_uno.nombre PERO SIEMPRE DEBE ESCRIBIRSE DE ESTA FORMA Y RECORDAR Q FUNCIONA PARA ATRIBUTOS PUBLICOS Y NO PRIVADOS
        return self.nombre.upper() #PUEDO USAR TMB ESTO PARA VALIDAR YA Q PODRIA HACER Q ME DEVUELVA MAYUS O OTRAS COSAS


    #ESTA ES UNA MANERA DE TRABAJAR LOS ATRIBUTOS PRIVADOS Y MEJOR
    def cambiar_password(self,old_password,new_password): #ESTO ES LO Q SE HACE O HARIA, ES LA VERDADERA FORMA DE TRABAJAR UN ATRIBUTO PRIV
        if old_password == self.password:               #cambiar_password es un metodo q se encarga de recibir la contra vieja y la nueva 
            self.__password = new_password              #si tu contra coincide con la q tiene guardada deja sino no
        else:
            print("La pass es incorrecta")



    def presentarse(self):
        print(f"Hola mi nombre es {self.nombre} {self.apellido}, tengo {self.edad} años y soy {self.tipo}")


#INSTANCIA PERSONA
usuario_uno=Usuario("Pedro","Perez","1234","20") #usuario_uno es un objeto 

print(usuario_uno.password) 
print(usuario_uno.nombre)
usuario_uno.password="asaqqwe"
print(usuario_uno.password)
