'''
Al ingresar una edad debemos informar si la persona es mayor de edad (mas de 18 años) 
o adolescente (entre 13 y 17 años) o niño (menor a 13 años).
'''

edad = input("ingrese edad: ")
edad = int(edad)

if(edad>18):
    print("es mayor de edad")
elif(edad>12 and edad<18):
    print("es adolescente")
else:
    print("es niño")

#ERROR DE SINTAXIS
#NO ES LO MISMO APRETAR ESPACIO Y TABULAR QUE TABULAR DE UNA
#ES UN ERROR DE SINTAXIS QUE ES IMPERCEPTIBLE A LA VISTA


