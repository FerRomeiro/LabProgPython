# Fernando Romero
# Crea una lista de palabras y muestra las palabras que tienen más de 5 letras.

lista_palabras = ["casa","perro","medicina","veterinaria","gato"]

for letras in lista_palabras:

    if len(letras) > 5:
        print("palabras: ",letras)