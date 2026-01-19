#Plantear una función que reciba un string en mayúsculas o minúsculas y retorne la cantidad de letras 'a' o 'A'.

# Definimos una función que cuenta cuántas veces aparece la vocal 'a'
# (en minúscula o mayúscula) dentro de una palabra.
def cantidad_vocal_a(palabra):
    cant = 0                     # Inicializamos el contador en 0
    for x in range(len(palabra)):   # Recorremos cada posición de la palabra
        # Si el carácter actual es 'a' o 'A', incrementamos el contador
        if palabra[x] == 'a' or palabra[x] == "A":
            cant = cant + 1
    return cant                  # Devolvemos la cantidad encontrada

# ---------------------------------------------------------
# BLOQUE PRINCIPAL DEL PROGRAMA
# ---------------------------------------------------------

# Pedimos al usuario que ingrese una palabra
palabra = input("Ingrese una palabra:")

# Mostramos cuántas 'a' contiene usando la función definida
print("La palabra", palabra, "tiene", cantidad_vocal_a(palabra), "a")
