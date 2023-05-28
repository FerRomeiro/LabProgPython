#ATRIBUTOS = DATOS DEL OBJETO con el q trabajamos nombre,apellido,edad
#METODOS = ACCIONES DEL OBJETO 

class Persona:

    #atributo de clase o "estatico". que es distinto a un atributo de instancia 
    tipo="Humano" # ES UN ATRIBUTO ESTATICO ES EDECIR TODAS LAS INSTANCIA LO VAN A COMPARTIR 

    #constructor(donde se definen e inicializan los atributos de instancia ya q los estaticos van afuera del constructor)
    def __init__(self,nombre,apellido,edad,genero=""): #GENERO ES UN PARAMETRO OPCIONAL
        self.nombre=nombre      #ACA CREAMOS UNA ATRIBUTO DE INSTANCIA LLAMADA NOMBRE Y LE ASIGNAMOS LO QUE RECIBIMOS POR PARAMETRO 
        self.apellido=apellido  #
        self.edad=edad
        self.genero=genero

    #metodo de instancia es de instancia porque este metodo esta realacionado con una instancia que acabo de crear
    def presentarse(self): #SELF ES UNA REFENRECIA A LA INSTANCIA QUE ESTA INVOCANDO ESTE METODO
        print(f"Hola mi nombre es {self.nombre} {self.apellido}, tengo {self.edad} años y soy {self.tipo}")


#instancia de persona

persona_1=Persona("Juan","Perez",31) #para acceder al constructor siempre el nombre de la class o clase en este caso Persona
#SI YO NO HAGO LO DEL RENGLON 22 NO PUEDO ACCEDER A presentarse PORQUE MI INSTANCIA NO VA A TENER DATOS NO ESTARIA CREADA 

#voy a crear una segunda instancia
persona_2=Persona("Lautaro","Gonzalez",25) # (atributos de instancia)


#acceso  a un metodo a partir de una instancia 
persona_1.presentarse() #persona_1 es una insctancia de la clase Persona #persona_1 es la variable donde guardamos el objeto instanciado 
persona_2.presentarse()


#CUANDO HACEMOS LO DE SELF Q ES OBLIGATORIO YA Q VA A ESTAR ALOJADO AHI LA DIRECCION DE MEMORIA DE LA INSTANCIA Q VA A TENER EL ACCESO HACIA DONDE SE ENCUENTRA
#EL ATRIBUTO
        # self.edad=edad
        # self.genero=genero
#EL SELF ES LA DIRRECCION DE MEMORIA DONDE SE VA A ESTAR ENCONTRANDO LA VARIABLE AL MOMENTO DE CONSTRUIRSE, CUANDO ESTAMOS CONSTRUYENDO TENEMOS Q DECIRLE 
#CON EL SELF EL LUGAR DONDE VAMOS A GUARDAR LAS COSAS O DE DONDE VAMOS A TENER LAS COSAS. HAY 2 FORMAS DE ESCRIBIR, CUANDO CREAMOS EL __init__ 
#ESTAS GUARDANDO COSAS EN LO QUE VA A SER EL OBJETO, DECIS Q CUANDO SE USE EL CONSTRUCTOR DONDE SE VA A ESTAR GUARDANDO LAS COSAS
#EN EL MOMENTO DE USAR EL METODO presentarse LE DECIMOS DE DONDE TIENE QUE LEER LAS COSAS
#LOS ATRIBUTOS SON CARACTERISTICAS QUE CONTIENEN Y TMB DATOS.
#EL SELF ES EL Q NOS DICE EN Q LUGAR ESTA ALOJADO ESE DATO TANTO COMO PARA GUARDAR AHI COMO PARA PODER LEERLO
# 
#EL OBJETO SERIA persona 1 Y persona 2 ES EL RESULTADO DE CUANDO HACEMOS Persona() Q AHI ES DONDE INSTANCIAMOS LA CLASE, DONDE LA ESTAMOS CONSTRUYENDO 
#LO DE LA LINEA 23 Y 24 ES EL OBJETO DE LA CLASE Persona ENTONCES CUANDO HACEMOS persona_1.presentarse() ESTAMOS ACCEDIENDO AL METODO DE LA CLASE
#
#metodo de clase no es necesario instanciar un objeto y para un metodo de objeto tenes q instanciar el objeto
#el metodo presentarse es un metodo de clase 
#instancia y objeto son lo mismo son sinonimos ahora si hicieramos el nombre de la clase . alguna accion ahi cambia las cosas 
#persona_1.presentarse() != Persona.tipo 
