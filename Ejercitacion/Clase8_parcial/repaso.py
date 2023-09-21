#SQ LITE    
#lenguaje estructurado de consulta, es un lenguaje que se utiliza para trabajar y manipular objetos y datos de una base de datos, objetos que no es 
#la programacion orientada a objetos sino todos los objetos que pertencen a una base de datos que pueden ser tablas o vistas
#podemos agregar informacion o datos a una base de datos y obtener informacion o datos de una base de datos.
#para eso se utiliza este lenguaje sql 
#Un SQL para python va a estar dentro de un modulo por lo cual no hay que instalar nada, osea que la 
#arquitectura cliente-servidor no la vamos a usar, no hace falta que se instale un motor de datos porque 
#SQL LITE va a estar en un modulo propio de python.

#que es un BD ?? una base de datos permite guardar informacion de forma persistente. Todo se agrupa en tablas y cada tabla contiene sus propias columnas
#en una base de datos la hoja seria una tabla, y cada  columna seria un campo de esa tabla
#una base de datos es un contenedor de tablas y una tabla es un contenedor de registros que va a estar formado cada registro por campos.
#Cuando los datos e informacion tienen complejidad se empieza a trabajar con base de datos caso contrario podria trabajarse con archivos json para 
#obtener informacion y se guardaba en csv
#En algun momento se podria sacar informacion de la base de datos a traves de un archivo csv y abrirlo en una planilla de calculo o aplicacion
#e incorporar esos datos a la base de datos de otra aplicacion q estuviese trabajando. Hay una trazabilididad y dependediendo de lo q tenga q hacer
#se trabaja con base de datos o archivo. Cuando cobramos los haberes en blanco y esta bancarizado, la empresa genera un archivo de los datos 
#para q el banco haga los haberes y lo q hace la entidad bancaria es agarrar ese archivo para luego acreditar los salarios en una fecha determinada
#q figura en ese archivo el soporte seria el archivo csv

#Que es SQLite?? es un gestor de bases de datos racionales. Es open source y se ha instalado por defecto con python, es decir forma parte de la biblioteca
#estandar, no tenemos que instalar ningun modulo con pip
#Este gestor de base de datos tiene por objetivo ser parte de la misma aplicacion con la que colabora, es decir no cumple los conceptos de cliente y servidor
#Si necesitamos almacenar informacion local con cierta estuctura el empleo de sqlite es una excelente opcion 
#Firefox usa SQLite para almacenar los favoritos el historial,las cookies,etc.
#
#SQL, las BD relacionales utilizan un lenguaje llamado SQL mediante el cual se puede gestionar la base de datos
#Formado por:
#lenguaje de definicion de datos(DDL)
#lenguaje de manipulacion de datos(DML)
#
#SQL lenguaje de consulta estructurado, esta formado basicamente por dos lenguajes que son DDL y DML
#DDL nosotros vamos a poder hacer cosas con respecto a los objetos de la base de datos y con respecto a la tabla voy a poder crearla tmb voy a póder 
#crear base de datos, alterar la tabla, voy a poder borrar la tabla.
#DML voy a poder manipular los datos, voy a poder acceder a la base de datos, voy a poder agregar modificar eliminar datos
#
#DDL podemos crear,alterar,eliminar y truncar. La diferencia entre eliminar o drop y truncar es que si nosotros usamos la sentencia drop lo q hacemos es borrar
#tabla y datos, y si usamos truncar o truncate lo q hacemos es eliminar la tabla pero los datos siguen existiendo
#alter o crear es si yo quiero agregar campos, restricccion de campos 
#
#DML vamos a poder seleccionar o  select, insert o insertar, update o actualizar, delete o borrar. Con select voy a poder traer informacion de la base de datos
# con insert puedo agregar datos a la base de datos, con update voy a poder modificar datos de la base de datos y con delete voy a poder borrar datos de la base de 
#datos y cuando se dice base de datos nos referimos a la tabla que pertenece a la base de datos. Nosotros trabajamos con una sola tabla 
#
#TIPO DE DATOS DE SQLite
#null:  es un valor nulo, significa q no hay dato
#intenger:  entero con signo,  
#real:  valor de coma flotante
#text:  cadena de texto
#blob:  son bytes almacenados exactamente como se ingresaron, aca podemos guardar imagenes y muchas cosas mas
#
#LA BASE DE DATOS ES UN CONTENEDOR DE TABLAS Y LA TABLA ES UN CONTENEDOR DE REGISTROS Y LOS REGISTROS ESTAN COMPUESTOS DE DATOS
#LA DIFERENCIA ENTRE BASE DE DATOS Y PYTHON ES QUE PYTHON ES UN LENGUAJE NO TIPADO Y LA BASE DATOS TENEMOS Q DECIRLE EL TIPO DE DATOS Q SE VA A 
#GUARDAR EN CADA CAMPO DONDE LA SUMATORIA DE ESOS CAMPOS VAN A DAR EL REGISTRO DE ESA FILA 
#
#Conectar SQLite: para poder trabajr con bases de datos de tipo SQLite debemos primero importar el modulo "sqlit3", luego conectar con la base de datos
#despues operar, y por ultimo no olvidar cerrar la conexion
#para conectar con la base de datos hay 2 maneras:
#
#import sqlite3
#conexion = sqlit3.connect("bd_btf.db") #lo q esta entre () es el nombre de la base de datos
#...
#conexion.close()

#la otra manera:
#import sqlit3
#with sqlit3.connect("bd_btf.db") as conexion: 
#...
#
#crear tabla en SQlite
#para poder crear una tabla en la base de datos:
#import sqlit3
#with sqlit3.connect("CLASE_sqlite/bd_btf") as conexion 
#try:
#   sentencia = ''' create table personaje #ACA CRE LA TABLA CON LAS 2 PALABRAS RESERVADAS create table
#                   (
#                           id integer primary key autoincrement #primary key significa q es unico y irrepetible, en este caso la ID va a ser unico y autonumerico
#                           nombre text, 
#                           apellido text,
#                           anio real            
#                   )                           
#               ''' 
#   conexion.execute(sentencia) #CON ESTO EJECUTO LA SENTENCIA
#   print("Se creo la tabla de personajes")
#   except sqlit3.OperationalError:
#       print("La tabla personajes ya existe")

#1:11:20

#Insert con SQLite
#para poder insertar filas en una tabla:
#usamos la sentencia insert
#
#import sqlite3
#with sqlite.connect("CLASE_sqlite/bd_btf.bd") as conexion:
#   try:
#       conexion.execute("insert into personajes(nombre,apellido,anio)")  #ACA USAMOS LAS DOS PALABARAS RESERVADAS INSERTE INTO y luego le paso la tabla q en este caso es personaje
                                                                            #y le paso el nombre de los campos entre ()
                                                                            #no podemos el id porque es autoincremental y no se pone 
#values (?,?,?)", ("Marty","McFLy","1968")) ##EN EL ORDEN DE OCURRENCIAS DE LOS NOMBRES DE LOS CAMPOS TIENE Q SER EL ORDEN DE OCURRENCIAS DE LOS DATOS QUE QUIERO GUARDAR COMO REGISTRO EN LA BASE DE DATOS 
#       conexion.execute("insert into personajes(nombre,apellido,anio)")
#values (?,?,?)", ("Emmet","Brown","1914"))
#   conexion.commit() #Actualiza los datos realmente en la tabla
#   except:
#       print("Error")





































