"""
Confeccionar un programa con las siguientes funciones:1) Cargar una lista con 5 palabras.2) 
Intercambiar la primer palabra con la última.3) Imprimir la lista
"""





# Función que pide 5 palabras al usuario y las guarda en una lista
def cargar_palabras():
    lista = []  # Lista vacía donde se almacenarán las palabras

    for i in range(5):
        palabra = input("Introduce una palabra: ")
        lista.append(palabra)  # Agregamos cada palabra a la lista

    return lista


# Función que intercambia la primera palabra con la última
def cambiar_extremos(lista):
    temp = lista[0]        # Guardamos la primera palabra
    lista[0] = lista[-1]   # La primera pasa a ser la última
    lista[-1] = temp       # La última pasa a ser la primera


# Función que imprime la lista completa
def mostrar(lista):
    print(lista)


# Bloque principal del programa
coleccion = cargar_palabras()
mostrar(coleccion)
cambiar_extremos(coleccion)
mostrar(coleccion)
