
# 1) Cargar una lista con 5 palabras.
# 2) Intercambiar la primer palabra con la última.
# 3) Imprimir la lista

def cargar_palabras():

    palabras = []
    print("Introduzca 5 palabras: ")

    for i in range(5):
        
        palabra = input(f"Introduzca la palabra {i}: ")
        palabras.append(palabra)
    
    return palabras

def intercambiar_pos(palabras):
    
    aux = palabras[0]
    palabras[0] = palabras[-1]
    palabras[-1] = aux

def imprimir(palabras):
    print(palabras)

#Programa

palabras = cargar_palabras()
intercambiar_pos(palabras)
imprimir(palabras)