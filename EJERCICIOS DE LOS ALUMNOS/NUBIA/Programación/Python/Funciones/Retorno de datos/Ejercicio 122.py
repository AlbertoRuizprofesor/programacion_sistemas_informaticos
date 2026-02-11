# Confeccionar una función que le enviemos como parámetro un string y nos retorne la cantidad de caracteres que tiene.
# En el bloque principal solicitar la carga de dos nombres por teclado y llamar a la función dos veces. 
# Imprimir en el bloque principal cual de las dos palabras tiene más caracteres.

string = input("Ingrese una palabra: ")

def longitud(string):
    print(f"La palabra {string} tiene {len(string)} caracteres.")
    return len(string)

longitud(string)

palabra1 = input("Ingrese una palabra: ")
palabra2 = input("Ingrese otra palabra: ")

largo1 = longitud(palabra1)
largo2 = longitud(palabra2)

if largo1 > largo2:
    print(f"La palabra {palabra1} es más larga que {palabra2}.")
else:
    print(f"La palabra {palabra2} es más larga que {palabra1}.")
    
