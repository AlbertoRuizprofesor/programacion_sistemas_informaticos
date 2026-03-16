#Definir una función que cargue una lista con palabras y la retorne. 
#Luego otra función tiene que mostrar todas las palabras de la lista que tienen más de 5 caracteres

def cargar_palabras():
    """
    Solicita al usuario cuántas palabras quiere ingresar
    y luego las almacena en una lista.
    Devuelve la lista completa de palabras.
    """
    lista_palabras = []
    cantidad = int(input("¿Cuántas palabras desea cargar? "))

    for i in range(cantidad):
        palabra_ingresada = input("Ingrese una palabra: ")
        lista_palabras.append(palabra_ingresada)

    return lista_palabras


def mostrar_palabras_largas(lista_palabras):
    """
    Muestra únicamente las palabras que tienen
    más de 5 caracteres.
    """
    print("Palabras con más de 5 caracteres:")
    for palabra in lista_palabras:
        if len(palabra) > 5:
            print(palabra)


# Bloque principal

palabras_cargadas = cargar_palabras()
mostrar_palabras_largas(palabras_cargadas)
