#Crear una lista y almacenar 10 enteros pedidos por teclado. 
#Eliminar todos los elementos que sean iguales al número entero 5.

# Creamos una lista vacía donde iremos guardando los valores ingresados
lista = []

# Cargamos 10 valores en la lista
for x in range(10):
    valor = int(input("Ingrese valor:"))
    lista.append(valor)

# Mostramos la lista original tal como fue ingresada
print(lista)

# Inicializamos una variable que usaremos como índice manual
posicion = 0

# Recorremos la lista mientras la posición sea válida
while posicion < len(lista):
    # Si el elemento actual es igual a 5...
    if lista[posicion] == 5:
        # ...lo eliminamos usando pop()
        # IMPORTANTE: al eliminar, los elementos se corren hacia la izquierda
        # por eso NO incrementamos 'posicion' aquí
        lista.pop(posicion)
    else:
        # Si el elemento NO es 5, avanzamos a la siguiente posición
        posicion = posicion + 1

# Mostramos la lista final después de eliminar todos los 5
print(lista)
