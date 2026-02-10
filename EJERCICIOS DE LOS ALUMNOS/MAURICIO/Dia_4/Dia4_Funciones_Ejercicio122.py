# DEFINICIÓN DE FUNCIONES


def largo(cadena):
    return len(cadena)


# BLOQUE PRINCIPAL

nombre1 = input("\nIngrese primer nombre: ")
nombre2 = input("Ingrese segundo nombre: ")
la1 = largo(nombre1)
la2 = largo(nombre2)
if la1 == la2:
    print(f"Los nombres: {nombre1} y {nombre2} tienen la misma cantidad de caracteres")
elif la1 > la2:
    print(f"{nombre1} es más largo")
else:
    print(f"{nombre2} es más largo")
