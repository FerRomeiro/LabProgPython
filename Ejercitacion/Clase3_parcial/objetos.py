# PYTHON ORIENTADO A OBJETOS:
# SE LLAMA OBJETOS PORQUE ANTES TENIAMOS LAS COSAS SUELTAS EN VARIABLES Y PARA RELACIONAR DATOS TENIAMOS QUE TRABAJAR LISTAS DE FORMA PARALELA
# PARA QUE ESOS INDICES TENGAN SIGNIFICADO, TAMBIEN PODIAMOS TRABAJR CON LISTAS DE DICCIONARIO, POR UN LADO TENIAMOS LOS DATOS POR OTRO LADO
# TENIAMOS LAS FUNCIONES QUE SE TRABAJABAN RELACIONADOS CON ESOS DATOS, ENTONCES LA PROGRAMACION ORIENTADA A OBJETOS LO QUE HACE ES INTEGRAR 
# BASICAMENTE LOS DATOS CON LAS FUNCIONES, ES DECIR UN OBJETO VA A TENER EN SI MISMO DATOS QUE SON PROPIOS DE ESE OBJETO Y FUNCIONES 
# QUE SON PROPIOS DE ESE OBJETOS. A LAS VARIABLES DE TIPO DATO LO VAMOS A LLAMAR ATRIBUTOS Y A LAS FUNCIONES QUE FORMAN PARTE DEL OBJETO LO LLAMAMOS METODO
# LOS METODOS SON UN TIPO DE FUNCION EN PARTICULAR QUE FORMAN PARTE DE UNA VARIABLE QUE ESTA VARIABLE TERMINA SIENDO UN OBJETO
#SE AGRUPAN PROPIEDADES Y COMPORTAMIENTOS EN ALGO QUE ES CLASS O CLASE Y ESA CLASE VA A TENER DENTRO PROPIEDADES QUE VAN A SER VARIABLES O DATOS
#Y COMPORTAMIENTOS QUE VAN A SER FUNCIONES O METODOS.
#CUANDO TRABAJAMOS CON CLASES O OBJETOS SE LLAMAN PROPIEDADES 
#FUNCIONES CUANDO ESAS FUNCIONES LAS DEFINIMOS EN UNA CLASE QUE LUEGO ESA CLASE VA A SER UN OBJETO Y ESE COMPORTAMIENTO O FUNCION LO VAMOS A REFERIR COMO METODO
#QUE ES UNA CLASE Y QUE ES UN OBJETO??
#CUANDO HABLAMOS DE CLASE HABLAMOS DE UNA COSA GENERAL O GENERALIZACION Y CUANDO HABLAMOS DE OBJETO HABLAMOS DE ALGO ESPECIFICO O COSA PARTICULAR DE ESA
#GENERALIDAD. PODRIAMOS TENER LA CLASE PERSONA Y EL OBJETO DE ESA PERSONA QUE SERIA CARLOS FERNANDO
#Y TRADUCIR ESTO EN LA PROGRMAAMCION ORIENTADA A OBJETO ES QUE LA CLASE DE PERSONA VA A TENER NOMBRE ES DECIR UN ATRIBUTO QUE SE LLAME NOMBRE
#VA A TENER UN ATRIBUTO QUE SEA EL DNI OTRO QUE SEA EL DOMICILIO, Y ASI CON LOS DATOS PARTICULARES QUE TODA PERSONA TIENE 
#LO CUAL VENDRIA A SER DATOS QUE TODA PERSONA TIENE POR ESA MISMA RAZON SERIA ALGO GENERICO, AHORA SI DECIMOS X PERSONA CON X DNI HACEMOS REFERENCIA
#A UNA PERSONA EN PARTICULAR Y ESA PERSONA EN PARTICULAR VA A SER UN OBJETO, Y DE MANERA GENERICA CON SOLO LAS PROPIEDADES VA A SER UNA PERSONA
#ES DECIR VA A SER UNA CLASE YA QUE LOS DATOS LOS TIENE TODAS LAS PERSONAS
#PARA LA PERSONA TAMBIEN EXISTEN COMPORTAMIENTOS, COMER CAMINAR HABLAR DORMIR. Y ESTOS COMPORTAMIENTOS LOS VAMOS A TRABAJAR A PARTIR DE FUNCIONES DENTRO
#DE LA CLASE O CLASS Y ESAS FUNCIONES QUE VAN A ESTAR DENTRO DE LA CLASE PARA NOSOTROS CUANDO SEAN OBJETOS VAN A SER METODOS
#
#SI PENSAMOS EN UNA TARJETA DE CREDITO LAS PROPIEDADES SERIAN EL NUMERO DE TARJETA, APELLIDO, NOMBRE Y EL METODO SERIAN ACTIVAR ESA TARJETA, ANULARLA
#Y LA CLASE VA A TENER UN NUMERO DE TARJETA, TITULAR, ES DECIR TODAS LAS TARJETAS TIENEN ESO PERO UNA VA A SER DIFERENTE A OTRA PORQUE NO TODAS TIENEN EL MISMO
#NOMBRE.
#SE PUEDE EVITAR LA PROGRAMACION ORIENTA A OBJETOS, PERO SIEMPRE ES MEJOR TRABAJAR CON PROGRAMACION ORIENTADA A OBJETOS YA QUE LA PROGRAMACION ESTRUCTURADA
#ES PREVIA A LA PROGRAMACION DE OBJETOS POR LO CUAL PODEMOS DECIR QUE LA PROG ORIENDATA A OBJETOS MEJORA, EVOLUCIONA LA PROGRAMACION ESTRUCTURADA
#LA ESTRUCTURA DE DATOS PRIMITIVOS SON VARIABLES, DE TIPO CADENA, NUMERICA,BOOL Y DESPUES TENEMOS LISTAS, DICCIONARIOS Y TODO ESTO NOS SIRVE PARA TENER 
#DATOS DE MANERA SIMPLE, CON LISTAS PARALELAS PERO DESPUES PODEMOS HACER ALGO MAS SOTIFISCADO A PARTIR DE ESOS DATOS PRIMITIVOS 
#
#CADA UNA DE NUESTRAS FUNCIONES VA A TRABAJAR CON PARAMETROS Y ESOS PARAMETROS SIEMPRE VAN A RECIBIR EL DICCIONARIO QUE REPRESENTE A ESE PERSONAJE
#O LA LISTA DE DICCIONARIO DE TODOS LOS PERSONAJES. COMO LOS EJERICICOS DE DATA STARK
#TODAS LAS FUNCIONES Q VOY A IR DESARROLLANDO RECIBEN SIEMPRE COMO PARAMETRO EL DICCIONARIO O LA LISTA DE DICCIONARIO 
#PENSANDO EN CUALQUIER FUNCION QUE SE NOS OCCURA
#LA FUNCION COMIENZA CON EL NOMBRE DE DATO QUE ESTAMOS TRABJANADO EJ PERSONAJE_MOSTRAR, PERSONAJE_LISTAR
#SIEMPRE COMENZAMOS CON EL DATO DEL NOMBRE QUE TRABAJAMOS Y ESE DATO ES EL DICCIONARIO
#HASTA VENIAMOS TRABAJANDO DE ESTE MODO, EN LOS EJERCICIOS
#
#CLASES:
#LA PALABRA RESERVADA class Y ES LA QUE UTILIZAMOS PARA PROGRAMAR UNA CLASE SEGUIDO DEL NOMBRE DE LA CLASE QUE DEBE REPRESENTAR DE MANERA GENERICA
#EL GRUPO O CONJUNTO DE INDIVIDUOS QUE VAMOS A TRABAJAR EJ: class Personaje_Heroes: SE ESCRIBE CONO INICIAL CON MAYUSCULA 
#class Personaje:
#pass (aca van las variables o atributos)
#
#PROPIEDADES/ATRIBUTOS:
#SON LAS VARIABLES QUE TODOS LOS OBJETOS DEL TIPO PERSONAJE DEBEN TENER SE DEFINE EN UN METODO LLAMADO INIT O EL CONSTRUCTOR
#_init_ ES LO PRIMERO QUE SE VA A EJECUTAR CUANDO SE CREA UN OBJETO DE UNA CLASE DETERMINADA, SE CONSTRUYE EN MEMORIA LA VARIABLE Y ESA VARIABLE O ESE OBJETO
#DE LA CLASE VA A TENER ASOCIADO OTRAS VARIABLES COMO id,apellido,edad Y CUANDO SE CONSTRUYE ESE OBJETO O CUANDO SE INSTANCIA UN OBJETO DE UNA CLASE DETERMINADA
#PASA A DEJAR DE SER UNA CLASE GENERICA O GENERAL Y PASA A SER UN OBJETO EN ESPECIFICO 
#
#class Personaje:
#   def _init_(self,id,nombre,apellido,edad)->None: #SIEMPRE EL PRIMER PARAMETRO VA A SE self "si mismo" Y LUEGO VAN LOS PARAMETROS Q SON LOS ATRIBUTOS DE ESA CLASE
#       self.id=id #crea un atributo id y le asigna el valor id
#       self.nombre=nombre
#       self.apellido=apellido
#       self.edad=edad #LA EDAD VA A SER ASIGNADO A LO OBJETO.EDAD 

#id,nombre;apellido Y edad SON PARAMETROS QUE SE RECIBEN EN EL MOMENTO DE LA CREACION DEL OBJETO POR LO TANTO NO SON LO MISMO QUE self.edad,self.apellido, ETC
#NO RETORNA NADA PORQUE EL CONSTRUCTOR SE VA A OCUPAR DE DAR LOS DATOS CORRESPONDIENTES A CADA UNO DE LOS ATRIBUTOS O PROPIEDADES QUE VA A TENER EL OBJETO
#CUANDO DECLARO UNA CLASE TODO LO QUE DEFINAS ADENTRO VA A SER METODOS
#SALVO EN EL CONSTRUCTOR OSEA EL init ESTE INICIA EL ESTADO, SON LOS VALORES CON LOS CUALES VA A INICIAR EL OBJETO
#EL self SE TIENE QUE PASAR SIEMPRE
#LA CLASE VA A TENER METODOS O FUNCIONES Y ATRIBUTOS
#EL CONSTRUCTOR VA A SER EL PRIMER METODO O LA PRIMERA FUNCION QUE SE VA A EJECUTAR SIN SIQUIERA LLAMAR AL METODO init AUTOMATICAMENTE SE VA A EJECUTAR
#LOS CONSTRUCTORES EN PYTHON SE TRABAJAN A PARTIR DE ESE METODO SIEMPRE EL PRIMER PARAMETRO DE ESE METODO VA A SER self Y LUEGO LOS DEMAS PARAMETROS QUE FORMAN
#PARTE COMO PROPIEDADES ATRIBUTOS DE LA CLASE Y NO RETORNA NADA.
#
#class Personaje:
#   tipo="Personaje" #tipo es el nombre de una variable que puede llamarse cualquier cosa seria la propiedad o atributo.Tipo es un atributo de class
                        #un objeto de una clase nunca se va a llamar igual que la clase, pero el tipo si porque es el tipo
                        #y tipo="Personaje" es para identificar de que tipo es la clase o objeto en algun momento y siempre lleva el mismo nombre de la class
                        #se puede no poner, aunque preferiblemente siempre se pone es como el type de una variable y nos sirve para identificar
#   def _init_(self,id, nombre,apellido,edad)->None:
#       self.id=id 
#       self.nombre=nombre
#       self.apellido=apellido
#       self.edad=edad

#El constructor primer parametro la propia clase o propio objeto self y la clase tiene una propiedad self.id self.nombre self.apellido y self.edad
#y estan dentro del propio objeto dentro de la misma clase
#y que nada tiene que ver con los demas parametros que son id,nombre,apellido y edad, sino  
#CREAR UNA INSTANCIA es crear una variable y en esa variable lo que voy a tener una variable del tipo objeto desarrollado por mi mismo
#y no una variable del tipo cadena,numerica,lista, etc 
#ej:
#personaje_A = Personaje(0,"Marty","McFly",18) Personaje no es una variable empieza en mayus y por lo tanto es una clase llamada Personaje
                                            #uso el nombre de la clase que es Personaje para instanciar un objeto, osea crear una variable del tipo objeto
                                            #de una clase determinada
#personaje_A ahora seria mi objeto, y (0,"Marty","McFly",18) es el constructor 
#
#ACCEDER A LOS ATRIBUTOS: accedo a partir de la notacion de puntos 
#peronaje_A = Personaje(0,"Marty","McFly",18) 
#peronsaje_B = Personaje(1,"Emmet","Brown",54)
#
#print(personaje_A.nombre) #Marty
#print(peronsaje_B.nombre) #Emmet

#COMO DEFINIR METODOS: lso metodos de instancia son funciones que se definen dentro de la clase y solo se pueden llamar desde una instacia de esa clase
#Al igual que _init_(), el primer parametro de un metodo de instancia siempre es self
#
#class Personaje:
    #def _init_(self,id,nombre,apellido,edad)->None: #EL METODO ES UNA FUNCION USAMOS LA PALABRA DEF 
        #self.id=id
        #self.nombre=nombre
    
    #def descripcion(self)->str: #DESCRIPCION ES UN METODO QUE RECIBE COMO PARAMETRO LA PROPIA CLASE self Y ES CLASE PORQUE ESTAMOS ESCRIBIENDO LA CLASE 
        #return "(0)-(1).formar(self.nombre,self.apellido)"

#Y CUANDO ESTO SE INSTANCIA RECIBIRA EL PROPIO OBJETO DE ESA CLASE

#LA CLASE ES ABSTRACTA Y EL OBJETO ES CONCRETO, LA CLASE ES GENERAL Y EL OBJETO ES PARTICULAR. TODOS LOS DATOS QUE TIENE UN OBJETO SON TODOS LOS ATRIBUTOS 
#Y METODOS QUE VA A TENER UNA CLASE LA DIFERENCIA ES QUE LA CLASE ES GENERAL O GENERICA Y EL OBJETO ES PARTICULAR.
#SIEMPRE TODOS LOS METODOS QUE DESARROLLAMOS VAN A TENER COMO PARAMETRO MINIMAMENTE self COMO EL METODO descripcion
#
#LOS ATRIBUTOS DE LA class Peronsaje VENDRIAN A SER self,id;nombre;apellido y edad DONDE SELF ES EL CONSTRUCTOR PORQUE SE CONSTRUYE A PARTIR DE ESO 
#EL METODO COMO MINIMO TIENE QUE TENER self 
#personaje_A ES EL OBJETO SU INSTANCIA VA A RETORNAR martin mcfly  
#LA INSTANCIA ES LA ACCION DE CONSTRUIR Y HAY UNA DIFERENCIA ENTRA LA CLASE Y LA INSTANCIA, LA CLASE ES LA GENERALIDAD Y EL OBJETO ES LA PARTICULARIDAD 
#
#_init_ es el constructor y descripcion es un metodo del objeto que se va a ejecutar solamente si yo lo llamo despues del . ej objeto.descripcion pero cuando
#yo creo el objeto el constructor se va a ejecutar si o si. Y esa es la gran diferencia
#
#personaje_A = Personaje(0,"Marty","McFly",18) # personaje es la clase y entre () son los valores del constructor, se construyo un objeto de la clase 
#peronsaje y el objeto peronsaje_A es del tipo class o clase Personaje y va a tener id,nombre,apellido,edad
# 
#personaje_A = Personaje(0,"Marty","McFly",18) al constructor le paso los datos entre()
#print(personaje_A.descripcion) #Marty-McFly para usar el metodo descprcion tengo q llamarlo con el . y metodo y el constructor no
#porque le paso los datos que van a ir a cada de los atributos de la clase o class Personaje

#2° parte
#ATRIBUTOS PROTEGIDOS: tanto atributos como metodos son publicos que significa que podemos acceder sin hacer una instancia a partir del nombre del objeto punto 
#atributo pero muchas veces no debe ser asi, sino que deberiamos acceder a los atributos a partir de un metodo 
# personaje_A = Personaje(0,"Marty","McFly",18) #Personaje() es el metodo constructor y a partir de este metodo nosotros le asignamos los datos,propiedades o atributos
# 
#por defecto los atributos son publicos, aunque conceptualmente no seria lo correcto aunque se puede hacer personaje_A.id(123) peronsaje_A.nombre("Luis")
#la asignacion se deberia trabajar a partir de un metodo, entonce por convencion se coloca un guion bajo para notar q el atributo esta protegido
#class Personaje:
    #def __init__(self,id,nombre,apellido,edad)->None:
        #self.id=id
        #self._nombre=nombre #GUION BAJO PARA NOTAR QUE ES UN ATRIBUTO PROTEGIDO LOS ATRIBUTOS PRIVADOS VAN CON DOBLE GUION BAJO
#por convencion se usa el guion bajo por delante del nombre del atributo para notar q el atributo es protegido 
#existen atributos con 3 scopes o 3 alcances q tiene q ver de q manera nosotros podemos acceder a un atributo de una clase a partir de un objeto
#que un atributo este protegido significa q solamente se puede acceder a ese atributo a partir de los objetos de la propia clase o aquellas clases q heredan
#de la clase que tiene el atributo
#Podemos tener una clase general una clase generica q puede ser la clase o class Persona como los ejemplos,y de la clase persona podemos hacer una instancia
#es decir un objeto y esa clase instancia podia llamarse Bizarrap q es una persona, y Messi tmb es una persona, pero q Messi es futbolista y Bizarrap es musico
#yo podria tener una clase q se llame musico, futbolista y un futbolista tiene apellido y nombre como tmb un musico, se encuentran varias similitudes
#un futbolista no tiene una discografia como tampoco un musico no tiene una copa
#comparten datos, metodos pero llega un momento que un musica va a tener propiedades y metodos propios como tmb un futbilista }
#esto significa q puedo tener la clase persona y la clase futbolista, y q la clase futbolista HEREDA todos los atributos y todos los metodos q tiene la clase
#Persona y a la vez la clase futbolista va a tener atributos y metodos propios que no tiene la clase Persona porque son propias de la clase futbolista
# y lo mismo ocurre con el musico hereda atributos y metodos de la clase persona como tmb metodos propios de la clase musico q la clase perosna no tiene
#Las clases son genericas y los objetos son especificos, pero puedo tener en el medio de los dos una clase antes del objeto por ejemplo como recien
#un musico o un futbolista q son clases y yo puedo instanciar un objeto del tipo musico que va a tener atributos propios de la clase musico pero ademas 
#va a tener todos los atributos y metodos su clase Personaje o clase padre, y todo esto esta relacionado con el guion bajo del ejemplo
#self._nombre = nombre
#el guion bajo significa q solamente se va a poder acceder cuando el atributo es protegido, lo protego con un guion aquellos objeto q son de una misma clase
#o aquellos objetos q son herencia de otra clase que heredo ese atributo
#ATRIBUTOS PRIVADOS: doble guion bajo, delante del nombre. Es similar al anterior la diferencia radica q es _ es por convencion y el  __ es explicito 
#y aca no vamos a poder acceder de manera directa sino que solamente podemos acceder a partir de un metodo que manipule ese atributo 
#significa q voy a tener un metodo y ese metodo me va a permitir asignar un nombre
#class_Personaje:
    #def __init__(self,id,nombre,apellido,edad):
        #self.id=id
        #self.__nombre=nombre 
#el agregar el guion bajo es algo convencional para documentar. 
#esto ocurre porque la idea es q los programas sean robustos es decir que sea seguro q no sea de facil acceso para evitar problemas
#al dato voy acceder a traves de un metodo, voy a tener atributos privados y metodos publicos
#los atributos por defecto son publicos y si quiero un atributo protegido le doy un guion bajo y si quiero uno privado doble guion bajo
#lo q me permite q el atributo sea protegido o privado q el programa q estoy desarrollando tenga mayor robustes q no se pueda acceder facil de cualquier lado
#a un atributo sino q tenga q seguir una normativa la cual es trabajar un metodo para poder interactuar con un atributo ya sea colocandole un dato a ese atributo
#o ya sea obteniendo un dato de ese atributo y es lo q se conoce como setter y getter. Set es colocar un dato y get es obtener un dato 
# y lo hago atraves de metodos, no se hace de forma cruda (objeto.atributo) sino es objeto.metodo y si tengo q darle un valor al atributo uso el metodo q corres
#ponda y si tengo q traer un dato de un atributo uso el metodo q corresponda
#print(peronsaje_A.nombre) #NO
#print(personaje_A.descripcion) #SI

#PROPERTY: esta funcion no permite interceptar la escritura, lectura y borrado de los atributos y ademas nos permitira inscorporar una documentaion sobre los
#mismos
#
#METODOS DUNDER: o metodos magicos son los metodos de una clase que tienen dos subrayados de prefijo y sufijo de nombre. Hay muchos y se pueden usar para 
#peronsalizar el comportamientos de los objetos en python 
#La sobrecarga es darle una funcionalidad diferente a una funcionalidad ya existente.
#El segundo metodo mas utilizado teniendo en cuenta q el primero es el constructor(__init__) es __str__ con lo q podemos hacer es darle un comportamiento 
#distinto, un comportamiento programado por nosotros
#ej:
#class Personaje:
    #def __init__(self,id,nombre,apellido,edad)->None:
        #self.id=id
        #self.nombre=nombre

    #def __str__(self)->str: #esta es la sobrecarga q lo q hace es retornar una cadena, recibe el propio objeto y retorna el apellido y nombre
        #return "{0}-{1}.format(self.nombre,self.apellido)"
#
#al imprimir el objeto podemos ver algo relacionado al contenido
#personaje_A=Persona(0,"Marty","Mcfly",18) # se hace instancia del primer objeto del objeto A
#personaje_B=Persona(1,"Emmet","Brown",54) 
#
#print(personaje_A) #Marty-Mcfly #ACA DIRECTAMENTE ME IMPRIME EL OBJETO A DIFERENCIA DEL EJ DE DESCRIPCION (peronsaje_A.descripcion) SIRECTAMENTE ME LO IMPRIME
                                #ME EJECUTA DIRECTAMENTE EL METODO SOBRECARGADO EN LA CLASE O CLASS PERSONAJE 
#print(personaje_B) #Emmet-Brown #ACA PASA LO MISMO

#__LEN__: en caso q el elemento tenga un numero de elementos podriamos usar la funcion len para obtenerlo
#ej:
#class Peronsaje:
    #def __init__(self,id,nombre,apellido,edad)->None:
        #self.id=id
        #self.nombre=nombre
        #self.cantidad=1
    #def __len__(self)->str: #ESTO SERIA LA SOBRECARGA Q RETORNA LA CANTIDAD O RETORNA EL ATRIBUTO 
        #return self.__cantidad

#HAY VARIOS METODOS MAS Q PERMITEN SOBRECARGAR LOS OPERADORES DE COMPARACION:
#METODO      OPERADOR    METODO   OPERADOR
#__IT__         <        __NE__     !=
#__LE__         <=       __GT__     >
#__EQ__         ==       __GE__     >=
#ESTOS TIENEN UN SEGUNDO PARAMETRO Q HACE REFERENCIA AL OTRO OBJETO CON EL QUE SE OPERA. SIENDO NECESARIO DEVOLVER EL RESULTADO

#HEREDAR DE OTRAS CLASES:  la herencia es el proceso por el cual una clase adquiere los atributos y metodos de otra
#para heredar solo se requiere colocar el nombre de la clase padre entre parentesis 
#









# LO QUE HACE ES INTEGRAR LOS DATOS CON LAS FUNCIONES, ES DECIR UN OBJETO VA A TENEER EN SU MISMO DATOS QUE SON PROPIOS DE ESE OBEJTO
# Y FUNCIONES QUE SON PROPIOS QUE SON TMB DE ESE OBEJTO, A LA PRIMERA SE LLAMA ATRIBUTOS Y SEGUNDA ---
# SE AGRUPAN PROPIEDADES Y COMPORTAMIENTOS ---
# QUE ES UNA CLASE Y QUE ES UN OBJETO?? 
# ESTRUCTURAS DE DATOS PRIMITIVOS SON NUMEROS, CADENAS, DICCIONARIOS Y LISTAS
# SI QUIERO REPRESENTAR ALGO MAS COMPLEJO, UNA ALTERNATIVA SERIA CON VARIABLES INDIVIDUALES, OTRA ALTERNATIVA ES LISTA, OTRA ALTERNATIVA ES DICCIONARIO
# LA MEJOR OPCION ES DICCIOANRIO O DICT, UNA LISTA UTILIZANDO DICCIONARIO 
# COMO DEFINIR CLASE ? 
# COMIENZA CON LAS PALABRA class SEGUIDA DEL NOMBRE DE LA CLASE Y LOS DOS PUNTOS 
# class Personaje:
#   pass (ACA ADENTRO VAN LAS VARIABLES O ATRIBUTOS)
# PROPIEDAS/ATRIBUTOS
# SON LAS VARIABLES, SE DEFINEN EN UN METODO LLAMADO __init__ 
# class personaje
#   def __init__(self,id,nombre,apellido,edad) -> None:
#       self.id = id #crea un atributo id y le asigna el valor id
#       self.nombre = nombre
#       self.apellido = apellido
#       self.edad = edad
# CREAS UNA INSTANCIA 
# LA CREACION DE UN OBJETO A PARTIR DE UNA CLASE  SE DENOMINA INSTANCIA DE UN OBJETO, SE PUEDE ---
# ACCEDE A LOS ATRIBUTOS, SE PUEDE ACCEDER MEDIANTE NOTACION DE PUNTOS
# COMO DEFINIR METODOS --- 
