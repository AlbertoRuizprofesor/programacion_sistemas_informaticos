def cargar():
    palabras=[]
    for x in range(0,5):
        pal=input("Ingrese una palabra:")
        palabras.append(pal)
    return palabras


def intercambiar(palabras):
    aux=palabras[0]
    palabras[0]=palabras[-1]
    palabras[-1]=aux


def imprimir(palabras):
    print(palabras)


# bloque main

palabras=cargar()
imprimir(palabras)
intercambiar(palabras)
imprimir(palabras)