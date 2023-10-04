from data_stark import lista_heroes
import re


# 0. Crear la función 'stark_normalizar_datos()' la cual recibirá por parámetro la
# lista de héroes. La función deberá:
# ● Recorrer la lista y convertir al tipo de dato correcto las keys (solo con
# las keys que representan datos numéricos) por ejemplo fuerza (int),
# altura (float), etc
# ● Validar primero que el tipo de dato no sea del tipo al cual será
# casteado. Por ejemplo si una key debería ser entero (ejemplo fuerza)
# verificar antes que no se encuentre ya en ese tipo de dato.
# ● Si al menos un dato fue modificado, la función deberá retornar el valor
# booleano True
# ● En caso de que la lista esté vacía o ya se hayan normalizado
# anteriormente los datos se deberá retornar el valor booleano False
# ● Crear una opción en el menú que me permita normalizar los datos (No
# se debería poder acceder a ninguna otra opción del menú hasta que
# los datos esten normalizados)
# ● En caso de que la llamada a la función retorne True mostrar un
# mensaje diciendo “Datos Normalizados” sino mostrar el mensaje
# “Hubo un error al normalizar los datos. Verifique que la lista no este
# vacía o que los datos ya no se hayan normalizado anteriormente”

