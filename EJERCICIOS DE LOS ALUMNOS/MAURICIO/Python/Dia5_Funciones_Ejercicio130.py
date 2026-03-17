# Funciones


def mascaracteres(palabras):
    pos = 0
    for x in range(len(palabras)):
        print(x, palabras[x])
        if len(palabras[x]) > len(palabras[pos]):
            pos = x
    return palabras[pos]


# Bloque Principal

palabras = ["enero", "febrero", "marzo", "abril", "mayo", "junio"]
print(f"La longitud de la lista: {len(palabras)}")
print(f"El rango de la lista: {range(len(palabras))}")
print(f"\nLa palabra con mas caracteres: {mascaracteres(palabras)}")
