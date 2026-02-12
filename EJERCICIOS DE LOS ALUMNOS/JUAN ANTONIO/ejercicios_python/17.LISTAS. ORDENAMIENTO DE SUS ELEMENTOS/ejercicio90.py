#Crear una lista y almacenar los nombres de 5 países. 
# Ordenar alfabéticamente la lista e imprimirla.

# Creamos una lista vacía donde guardaremos los nombres de los países
paises = []

# Cargamos 5 países ingresados por el usuario
for x in range(5):
    nom = input("Ingrese el nombre de pais:")  # Pedimos un país
    paises.append(nom)                         # Lo agregamos a la lista

# Comienza el proceso de ordenamiento (método burbuja optimizado)
# Primer bucle: controla cuántas pasadas se hacen
for k in range(4):
    # Segundo bucle: recorre los elementos hasta la posición 4 - k
    # Cada pasada deja el elemento más grande al final, así que no hace falta volver a compararlo
    for x in range(4 - k):
        # Comparamos cadenas alfabéticamente
        if paises[x] > paises[x+1]:
            # Intercambiamos si están en orden incorrecto
            aux = paises[x]
            paises[x] = paises[x+1]
            paises[x+1] = aux

# Mostramos la lista ya ordenada alfabéticamente
print("Listado de paises")
print(paises)
