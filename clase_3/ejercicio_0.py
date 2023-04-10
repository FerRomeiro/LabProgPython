from data import lista_bzrp  # IMPORTAMOS DE data LA LISTA DE BIZARAP

# """
# {
# 'title': 'QUEVEDO || BZRP Music Sessions #52'
# 'views': 227192970
# 'length': 204
# 'img_url': 'https://i.ytimg.com/vi/A_g3lMcWVy0/sddefault.jpg'
# 'url': 'https://youtube.com/watch?v=A_g3lMcWVy0'
# 'date': '2022-07-06 00:00:00'
# }

# lista_empleados = [{"nombre": "Juan","apellido":"Perez","dni":33},
#                    {"nombre":"Ezequiel","apellido":"Rodriguez","dni:"22},
#                    {"nombre":"German","apellido":"Luna","dni":11}]
# """
#"Queremos recorrer la lista y mostrar el titulo de cada video" Y USAMOS EL FOR

bandera_Mayor = False
mayor_Cantidad = None # 0 LE DAMOS UN VALOR SIMBOLICO PARA Q NOS PERMITA USAR LA BANDERA
video_Mas_Reproducciones = "" # como va a ser una cadena el titulo del video lo inicializo asi

for video in lista_bzrp: #recorremos la lista con For y el tipo de elemento q contiene la lista es dictinario
            # cada diccionario representa un video y cada iteracion de For la variable video
            #guarda un diccionario disstinto por cada iteracion de for
    #Si quiero mostrar solo el titulo de cada video puedo hacerlo con []
    #  
    print(video["title"]) #tittle es la clave q me devuelve un valor, le paso una clave y me devuelve un valor
                        #hasta aca puedo ver la lista de los videos de bzrp de cada uno, donde cada uno es un diccionario
    print(video["title"],"visualizaciones: ",video["views"]) # para mostrar el titulo y sus views
    #AHORA RECORREMOS LA LISTA Y BUSCAMOS ALGO ESPECIFICO, EJ: LA MAYOR CANT DE REPRODUCIONES   
    #PARA ESO CREAMOS BANDERA MAYOR
    if bandera_Mayor == False or video["views"] > mayor_Cantidad:
        mayor_Cantidad = video["views"] #views en este caso es la clave para acceder al diccionario video
        video_Mas_Reproducciones = video["title"]# me guardo el nombre del video mas reproducido  
        bandera_Mayor = True

print(video_Mas_Reproducciones,mayor_Cantidad)

#PODEMOS INICIALIZAR LA VARIABLE MAYOR CANTIDAD CON EL PRIMER ELEMENTO DE LA LISTA
#Y DE ESA MANERA NOS AHORRAMOS LA BANDERA

mayor_Cantidad = lista_bzrp[0] ["views"] #LE PASAMOS UN INDICE, la cant de reproducciones del primer diccionario
                #accedemos a un diccionario y de ese al valor de reproducciones con la calve views
for video in lista_bzrp:

    if video["views"] > mayor_Cantidad: #accedemos a una lista y a su vez a una clave valor de ese primer elemento
        mayor_Cantidad = video["views"] 
        video_Mas_Reproducciones = video["title"]

print(video_Mas_Reproducciones,mayor_Cantidad)

