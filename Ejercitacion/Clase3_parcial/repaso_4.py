#renato 

#ATRIBUTOS = DATOS DEL OBJETO
#METODOS = ACCIONES DEL OBJETO

class Persona:

    #ATRIBUTO DE CLASE O "ESTÁTICO"
    tipo = "Humano"

    #CONSTRUCTOR (donde se definen e inicializan los atributos de instancia)
    def __init__(self, nombre, apellido, edad, genero = ""):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad      
        self.genero = genero    

    #METODO DE INSTANCIA
    def presentarse(self):
        print(f"¡Hola! Mi nombre es {self.nombre} {self.apellido}, tengo {self.edad} años y soy {self.tipo}")

    def __str__(self):
        return f"Persona: {self.nombre} {self.apellido}, {self.edad} años"

#INSTANCIA DE PERSONA
persona_1 = Persona("Juan", "Perez", 20) #VARIABLE (OBJETO)
persona_2 = Persona("Lautaro","Gonzalez",25)


#ACCEDO A UN METODO A PARTIR DE UNA INSTANCIA
#persona_1.presentarse()
#persona_2.presentarse()

print(persona_1)