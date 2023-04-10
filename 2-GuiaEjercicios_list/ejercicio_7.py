# Fernando Romero
# Crea una lista con los nombres de tus 3 deportes 
# favoritos y luego agrega otro deporte al final de la lista.

deportes=[]

for sport in range(3): #En este caso sport es el contador porq uso el for con range
    deporte_ingresado = input("ingrese deporte: ")
    deportes.append(deporte_ingresado)
print("Deportes ingresados: ",deportes)

nuevo_deporte=input("Ingrese nuevo deporte: ")
deportes.append(nuevo_deporte)
print("deportes: ",deportes)