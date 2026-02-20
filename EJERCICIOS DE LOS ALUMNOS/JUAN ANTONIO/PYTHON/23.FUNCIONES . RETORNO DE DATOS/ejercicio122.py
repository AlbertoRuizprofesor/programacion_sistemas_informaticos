"""
Confeccionar una función que le enviemos como parámetro un string y nos retorne la cantidad de caracteres que tiene. En el bloque principal solicitar la carga de dos nombres por teclado y llamar a la función dos veces. 
Imprimir en el bloque principal cual de las dos palabras tiene más caracteres.

"""

# Definimos una función llamada 'largo' que recibe una cadena de texto
# y devuelve la cantidad de caracteres que contiene usando len()
def largo(cadena):
    return len(cadena)

# ---------------------------------------------------------
# BLOQUE PRINCIPAL DEL PROGRAMA
# ---------------------------------------------------------

# Pedimos al usuario que ingrese dos nombres
nombre1 = input("Ingrese primer nombre:")
nombre2 = input("Ingrese segundo nombre:")

# Calculamos la longitud de cada nombre usando la función 'largo'
la1 = largo(nombre1)
la2 = largo(nombre2)

# Comparamos las longitudes para determinar cuál es más largo
if la1 == la2:
    # Si tienen la misma cantidad de caracteres, lo informamos
    print("Los nombres:", nombre1, nombre2, "tienen la misma cantidad de caracteres")
else:
    # Si no son iguales, verificamos cuál es mayor
    if la1 > la2:
        print(nombre1, "es más largo")
    else:
        print(nombre2, "es más largo")

