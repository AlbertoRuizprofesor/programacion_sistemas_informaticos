"""
En el bloque principal del programa:
definir un diccionario que almacene los nombres de paises como clave y como valor la cantidad de habitantes. 
Implementar una función para mostrar cada clave y valor.
"""

paises = {"España": 46754778, "Francia": 67090000, "Italia": 60490000, "Alemania": 83160000}

def imprimir_paises(paises):
    for pais in paises:
        print(f"El pais {pais} tiene {paises[pais]} habitantes.")
        
# Bloque principal:
imprimir_paises(paises)