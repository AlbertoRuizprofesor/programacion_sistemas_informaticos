#Solicitar por teclado la cantidad de empleados que tiene la empresa. 
#Crear y cargar una lista con todos los sueldos de dichos empleados. 
#Imprimir la lista de sueldos ordenamos de menor a mayor.

cantidad = int(input("Cuantos empleados tiene la empresa?"))
sueldos = []

# Cargamos los sueldos según la cantidad indicada
for x in range(cantidad):
    su = int(input("Ingrese sueldo:"))   # Pedimos un sueldo
    sueldos.append(su)                   # Lo agregamos a la lista

# Ordenamos la lista usando el método burbuja (bubble sort)
for k in range(cantidad - 1):            # Controla cuántas pasadas se hacen
    for x in range(cantidad - 1 - k):    # Recorre los elementos comparando pares
        if sueldos[x] > sueldos[x + 1]:  # Si están en orden incorrecto...
            aux = sueldos[x]             # Guardamos el valor actual
            sueldos[x] = sueldos[x + 1]  # Intercambiamos posiciones
            sueldos[x + 1] = aux

# Mostramos la lista ya ordenada
print("Lista de sueldos ordenados")
print(sueldos)


