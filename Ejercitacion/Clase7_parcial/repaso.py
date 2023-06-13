#MAS O MENOS AL MINUTO 20 EXPLICA LAS COORDENADAS DE X Y Y, IMPORTANTE ESCUCHAR LA EXPLICACION
#EXCEPCIONES:
#con las excepciones lo que hacemos es capturar errores y evitar que el programa explote o deje de funcionar. Ej: la division cuando tengo una variable
#para numerador y denominador, lo que generaria q el programa deje de funcionar es dividir por 0 osea si el denominador es 0
#si el programa en ejecucion divide divide continuamente y en algun momento da 0 dejaria de funcionar durante la ejecucion es por eso que se deben
#programar excepciones, que lo que hace es que posiblemente ocurra un problema en tiempo de ejecucion entonces lo que hago es ponerlo en un bloque
#y si ese problema realmente se hace efectivo y con un bloque digo lo que quiero q haga el programa y en vez de explotar o dejar de funcionar 
#le digo a traves de un bloque lo que debe hacer y de esa forma evitaria que explote
#Los errores detectados durante la ejecucion se llaman excepciones y salvo q tratemos ese error el programa se cerrara 
#
#a=4 : b=0
#print(a/b)
#Tracenback (most recent call last)
#    File "<stdin>", line 1, in <module>
#ZeroDivisionError: division by Zero

#Tipos de excepciones:
#existen diferentes tipos de excepciones para los distintos tipos de errores e inclusive la posibilidad de declarar nuevas excepciones
#
#Capturar excepciones:
#Hay bloques en los cuales vamos a trabajar para capturar las excepciones, cuando entiendo que puede haber una parte del programa deje de funcionar
#en tiempo de ejecucion lo que hago es colocar lineas de codigo dentro de un try.
#try:
#   int("Hola mundo") #SI ESTO EXPLOTA, LO QUE HAGO ES CAPTURAR LAS DISTINTAS EXCEPCIONES Y DENTRO DE CADA UNA VOY A INDICAR ALGO
#except ValueError:
#   print("No puede convertirse a un entero")
#except TypeError:
#   print("No es una cadena")
#except:
#   print("Es otro tipo de error")
#
#si yo trabajo sin excepciones el programa explota, si trabajo con excepciones se ejecutara la excepcione del tipo de error q se genere y se hace algo 
#al respecto.
#
#excepciones existen en todos los lenguajes de alto nivel, no es propio de python. 
#
#LANZAR EXCEPCIONES:
#
#BLOQUE ELSE:
#el bloque else se ejecutara si no ha ocurrido ninguna excepcion
#
#def divide(x,y):
#   try:
#       resultado=x/y
#   except ZeroDivisionError:
#       print("No es posible dividir por eso")
#   else:
#       print("El resultado es: ",resultado)

#BLOQUE FINALIZADOR:
#como se puede ver este bloque finally siempre se ejecuta. Puede ser util para liberar recursos externos. (como archivos o conexiones de red)
#El finally se va a ejecutar siempre, 
#def divide(x,y):
#   try:
#       resultado=x/y
#   except ZeroDivisionError:
#       print("No es posible dividir por eso")
#   else:
#       print("El resultado es: ",resultado)
#   finally:
#       print("Se ejecuto finally")
#
#VALIDAR CON EXCEPCIONES:
#esta funcion intenta obtener un valor entero ingresado por el usuario
#
#def leer_entero(intentos):
#   entorno = None
#   for i in range(intentos):
#       valor=input("Ingrese un numero: ")
#       try:
#           valor=int(valor)
#           retorno=valor
#           break
#       except ValueError:
#           print("Error se debe ingresar un numero entero")
#   return retorno






























