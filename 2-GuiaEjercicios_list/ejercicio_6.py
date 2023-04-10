# Fernando Romero
# Crea una lista con 3 
# números enteros y luego agrega un 
# nuevo número al final de la lista.

lista=[]

for numero in range(3):
    n = input("ingrese un numero: ")
    n = int(n)
    lista.append(n)
print(lista)

nuevo_numero = input("ingrese un nuevo numero: ")
nuevo_numero_ingresado = int(nuevo_numero)
lista.append(nuevo_numero_ingresado)
print(lista)

# {
#     "window.zoomLevel": 3,
#     "bracket-pair-colorizer-2.depreciation-notice": false,
#     "liveServer.settings.donotShowInfoMsg": true,
#     "[python]": {
#         "editor.formatOnType": true
#     },
#     "diffEditor.ignoreTrimWhitespace": false,
#     "workbench.colorTheme": "Night Wolf (black)"
# }