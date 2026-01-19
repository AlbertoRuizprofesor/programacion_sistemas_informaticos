# FUNCIONES
def cantidad_vocal_a(palabra):
    cant = 0
    for x in range(len(palabra)):
        if palabra[x] == "a" or palabra[x] == "A":
            cant = cant + 1
    return cant


# MAIN
palabra = input("\nIngrese una palabra:")
print(f"\nLa palabra {palabra} tiene {cantidad_vocal_a(palabra)} aes")
