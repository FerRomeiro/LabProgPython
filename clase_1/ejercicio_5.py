'''
Fernando Romero

Ejercicio 5:
Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
por cada estadía como base, se pide el ingreso de una estación del
año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
Plata/Córdoba) para vacacionar para poder calcular el precio final:
-en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un
descuento del 10% Mar del Plata tiene un descuento del 20%
-en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene
un aumento del 10% Mar del Plata tiene un aumento del 20%
-en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el
precio sin descuento.
Validar el ingreso de datos
'''

VALOR_ESTADIA = 15000

estacion_Año = input("ingrese estacion : ")
while estacion_Año != "invierno" and estacion_Año != "verano" and estacion_Año != "primavera" and estacion_Año != "otoño":
    estacion_Año = input("Error, reingrese estacion: ")

localidad = input("ingrese localidad: ")
while localidad != "mar del plata" and localidad != "cordoba" and localidad != "cataratas" and localidad != "bariloche":
    localidad = input("Error, reingrese localidad: ")

#en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un
#descuento del 10% Mar del Plata tiene un descuento del 20%
if estacion_Año == "invierno":
    if localidad == "bariloche":
        porcentaje = 20
    elif localidad == "cordoba":
        porcentaje = -10 
# #-en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene
# un aumento del 10% Mar del Plata tiene un aumento del 20%
if estacion_Año == "verano":
    if localidad == "bariloche":
        porcentaje = -20
    elif localidad == "cataratas" or localidad == "cordoba":
        porcentaje = 10
    else:
        porcentaje = 20
# -en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
# aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el
# precio sin descuento.
if estacion_Año == "otoño" or estacion_Año == "primavera":
    if localidad == "bariloche" or localidad == "cataratas" or localidad == "cordoba":
        porcentaje = 10
    else:
        porcentaje = 0;

Precio_Final = VALOR_ESTADIA+(VALOR_ESTADIA * porcentaje/100)

if porcentaje == 0:
    print("Estacion del año: {} Localidad: {} El precio final es {} SIN DESCUENTO".format(estacion_Año,localidad,Precio_Final))
elif porcentaje > 0:
    print("Estacion del año: {} Localidad: {} El precio final es {} Con un aumento de {}%".format(estacion_Año,localidad,Precio_Final,porcentaje))
else:
    porcentaje=porcentaje*-1
    print("Estacion del año: {} Localidad: {} El precio final es {} Con un descuento de {}%".format(estacion_Año,localidad,Precio_Final,porcentaje))