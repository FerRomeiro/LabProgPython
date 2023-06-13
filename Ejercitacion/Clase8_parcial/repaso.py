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
#lenguaje de definicion de datos
#lenguaje de manipulacion de datos
#