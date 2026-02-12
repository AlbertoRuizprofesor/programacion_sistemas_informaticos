"""
Crear y cargar en un lista los nombres de 5 países y en otra lista paralela la cantidad de habitantes del mismo. 
Ordenar alfabéticamente e imprimir los resultados. 
Por último ordenar con respecto a la cantidad de habitantes (de mayor a menor) e imprimir nuevamente.
"""
# Cargamos dos listas paralelas: una con países y otra con habitantes
paises = []
habitantes = []

for x in range(5):
    nom = input("Ingrese el nombre del pais:")   # Pedimos el nombre del país
    paises.append(nom)                           # Lo agregamos a la lista de países

    cant = int(input("Cantidad de habitantes"))  # Pedimos la cantidad de habitantes
    habitantes.append(cant)                      # Lo agregamos a la lista de habitantes

# ---------------------------------------------------------
# ORDENAMIENTO ALFABÉTICO (A → Z) USANDO MÉTODO BURBUJA
# ---------------------------------------------------------
for k in range(4):                               # Controla cuántas pasadas se hacen
    for x in range(4 - k):                       # Compara elementos consecutivos
        if paises[x] > paises[x + 1]:            # Si están en orden incorrecto...
            # Intercambiamos los países
            aux1 = paises[x]
            paises[x] = paises[x + 1]
            paises[x + 1] = aux1

            # Intercambiamos también los habitantes para mantener la relación
            aux2 = habitantes[x]
            habitantes[x] = habitantes[x + 1]
            habitantes[x + 1] = aux2

# Mostramos la lista ordenada alfabéticamente
print("Listado de paises en orden alfabetico")
for x in range(5):
    print(paises[x], habitantes[x])

# ---------------------------------------------------------
# ORDENAMIENTO POR HABITANTES (DE MAYOR A MENOR)
# ---------------------------------------------------------
for k in range(4):                               # Controla cuántas pasadas se hacen
    for x in range(4 - k):                       # Compara habitantes consecutivos
        if habitantes[x] < habitantes[x + 1]:    # Si el siguiente tiene más habitantes...
            # Intercambiamos países
            aux1 = paises[x]
            paises[x] = paises[x + 1]
            paises[x + 1] = aux1

            # Intercambiamos habitantes
            aux2 = habitantes[x]
            habitantes[x] = habitantes[x + 1]
            habitantes[x + 1] = aux2

# Mostramos la lista ordenada por cantidad de habitantes
print("Listado de paises por cantidad de habitantes")
for x in range(5):
    print(paises[x], habitantes[x])
