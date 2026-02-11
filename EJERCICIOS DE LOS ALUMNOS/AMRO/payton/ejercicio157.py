def cargar():
    palabras=[]
    cant=int(input("Cuantas palabras quiere cargar?"))
    for x in range(cant):
        pal=input("Ingrese palabra:")
        palabras.append(pal)
    return palabras


def palabras_mas5(palabras):
    print("Palabras ingresadas con mas de 5 caracteres")
    for palabra in palabras:
        if len(palabra)>5:
            print(palabra)


# bloque main

palabras=cargar()
palabras_mas5(palabras)