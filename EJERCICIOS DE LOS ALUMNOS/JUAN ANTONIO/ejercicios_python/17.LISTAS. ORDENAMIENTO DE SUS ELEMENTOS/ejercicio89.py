#Se debe crear y cargar una lista donde almacenar 5 sueldos. 
#Ordenar de menor a mayor la lista.

# Creamos una lista vacía donde guardaremos los sueldos
sueldos = []

# Cargamos 5 sueldos ingresados por el usuario
for x in range(5):
    valor = int(input("Ingrese sueldo:"))  # Pedimos un sueldo
    sueldos.append(valor)                  # Lo agregamos a la lista

# Mostramos la lista tal como fue ingresada
print("Lista sin ordenar")
print(sueldos)

# Comienza el proceso de ordenamiento (método burbuja)
# Primer bucle: controla la cantidad de pasadas
for k in range(4):
    # Segundo bucle: recorre los elementos comparando pares consecutivos
    for x in range(4):
        # Si el elemento actual es mayor que el siguiente, los intercambiamos
        if sueldos[x] > sueldos[x+1]:
            aux = sueldos[x]          # Guardamos temporalmente el valor actual
            sueldos[x] = sueldos[x+1] # El siguiente pasa a la posición actual
            sueldos[x+1] = aux        # El valor guardado pasa a la posición siguiente

# Mostramos la lista ya ordenada de menor a mayor
print("Lista ordenada")
print(sueldos)
