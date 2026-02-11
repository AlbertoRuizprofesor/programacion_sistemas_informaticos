"""
Desarrollar una aplicación que nos permita crear un diccionario ingles/castellano. La clave es la palabra en ingles y el valor es la palabra en castellano.

Crear las siguientes funciones:

1) Cargar el diccionario.

2) Listado completo del diccionario.

3) Ingresar por teclado una palabra en ingles y si existe en el diccionario mostrar su traducción.
"""

def cargar_traducciones():
    """
    Permite ingresar pares de palabras (inglés → castellano)
    y almacenarlas en un diccionario.
    El usuario decide cuándo dejar de cargar datos.
    """
    traducciones = {}
    continuar = "s"

    while continuar == "s":
        palabra_castellano = input("Ingrese palabra en castellano: ")
        palabra_ingles = input("Ingrese palabra en inglés: ")
        traducciones[palabra_ingles] = palabra_castellano
        continuar = input("¿Desea cargar otra palabra? [s/n]: ")

    return traducciones


def mostrar_diccionario(traducciones):
    """
    Muestra todas las palabras almacenadas en el diccionario
    junto con su traducción al castellano.
    """
    print("Listado completo del diccionario:")
    for palabra_ingles, palabra_castellano in traducciones.items():
        print(palabra_ingles, "→", palabra_castellano)


def consultar_traduccion(traducciones):
    """
    Permite consultar la traducción al castellano
    de una palabra en inglés ingresada por el usuario.
    """
    consulta = input("Ingrese la palabra en inglés a consultar: ")
    if consulta in traducciones:
        print("En castellano significa:", traducciones[consulta])
    else:
        print("La palabra no se encuentra en el diccionario.")


# Bloque principal

diccionario_traducciones = cargar_traducciones()
mostrar_diccionario(diccionario_traducciones)
consultar_traduccion(diccionario_traducciones)
