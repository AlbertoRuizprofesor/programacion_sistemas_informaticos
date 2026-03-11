#Se debe crear y cargar una lista donde almacenar 5 sueldos. 
#Desplazar el valor mayor de la lista a la última posición.

# Creamos una lista vacía donde guardaremos los sueldos
sueldos = []

# Cargamos 5 sueldos ingresados por el usuario
for x in range(5):
    valor = int(input("Ingrese sueldo:"))  # Pedimos un sueldo
    sueldos.append(valor)                  # Lo agregamos a la lista

# Mostramos la lista tal cual fue ingresada
print("Lista sin ordenar")
print(sueldos)

# Este bucle recorre las posiciones del 0 al 3 (4 elementos)
for x in range(4):
    # Comparamos el sueldo actual con el siguiente
    if sueldos[x] > sueldos[x+1]:
        # Si el actual es mayor, los intercambiamos
        aux = sueldos[x]
        sueldos[x] = sueldos[x+1]
        sueldos[x+1] = aux

# Mostramos la lista después de una sola pasada de intercambio
print("Lista con el último elemento ordenado")
print(sueldos)
