# Fernando Romero
# Crear un programa que solicite al usuario ingresar precio unitario y cantidad de 5 productos. 
# Almacenar cada valor en dos listas distintas. Luego imprimir el precio total de cada artículo.

lista_precio=[]
lista_productos=[]

for precio in range(5):
    precio=int(input("Ingrese un precio: "))
    lista_precio.append(precio)

for productos in range(5):
    productos=input("Ingrese producto: ")
    lista_productos.append(productos)

precio_articulos=[]

for impresion in range(len(lista_productos)):
    precio_articulos.append(lista_productos[impresion])
    precio_articulos.append(lista_precio[impresion]) 

print(precio_articulos)