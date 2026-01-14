"""
Desarrollar una función que reciba una lista de string y 
nos retorne el que tiene más caracteres. 
Si hay más de uno con dicha cantidad de caracteres debe retornar 
el que tiene un valor de componente más baja. 
En el bloque principal iniciamos por asignación la lista de string:
"""

def mayor_cadena (cadena):
    posicion = 0
    for x in range (len(cadena)):
        if len(cadena[x]) > len(cadena[posicion]):
            posicion = x

    return cadena[posicion]

cadena = ["casa", "metronomo", "guitarra", "coche", "tiniebla"]
print("Palabra con más caracteres: " , mayor_cadena(cadena))




