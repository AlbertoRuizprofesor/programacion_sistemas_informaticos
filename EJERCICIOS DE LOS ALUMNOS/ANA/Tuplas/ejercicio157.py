# Definir una función que cargue una lista con palabras y la retorne. 
# Luego otra función tiene que mostrar todas las palabras de la lista que tienen más de 5 caracteres.

def introducir_palabras():

    palabras = []

    
    numelem = int(input("¿Cuantas palabras desea introducir? "))

    for i in range(numelem):
        palabra = input(f"Introduzca la palabra {i}: ")
        palabras.append(palabra)
    
    return palabras

def palabrasmayorcinco(palabras):
    
    print("Palabras con más de 5 caracteres")
    for pal in palabras:
        if len(pal) > 5:
            print(pal)

#Programa

palabras = introducir_palabras()
palabrasmayorcinco(palabras)
