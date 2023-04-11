# Fernando Romero
# Crea una lista vacía y pide al usuario que ingrese una palabra. 
# Luego, agrega la palabra a la lista si no se encuentra ya en la lista. 
# Repite este proceso hasta que la lista tenga al menos 5 palabras.

palabras=[]
for palabrotas in range(5): # EN CASO QUE ME PONGA UN LIMITE DE VUELTAS TAMBIEN PODRIA USAR len(palabras)<5
    palabra=input("ingrese una palabra: ")
    
    if palabra and palabra not in palabras:
        palabras.append(palabra)
    else:
        print("La palabra ya existe")
        
    
print(palabras)