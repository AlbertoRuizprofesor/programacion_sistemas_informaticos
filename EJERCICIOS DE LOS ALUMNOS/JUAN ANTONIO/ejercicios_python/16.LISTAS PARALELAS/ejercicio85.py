"""
Crear y cargar dos listas con los nombres de 5 productos en una y sus respectivos precios en otra. 
Definir dos listas paralelas. Mostrar cuantos productos tienen un precio mayor al primer producto ingresado
"""

# Creamos dos listas vacías: una para los nombres de productos y otra para sus precios
productos = []
precios = []

# Bucle que se repite 5 veces para pedir los datos de 5 productos
for x in range(5):
    nom = input("Ingrese el nombre del producto:")  # Pedimos el nombre del producto
    productos.append(nom)  # Guardamos el nombre en la lista 'productos'

    pre = int(input("Ingrese el precio de dicho producto:"))  # Pedimos el precio
    precios.append(pre)  # Guardamos el precio en la lista 'precios'

# Inicializamos un contador para saber cuántos productos son más caros que el primero
cantidad = 0

# Recorremos los productos desde el índice 1 hasta el 4 (el primero es el índice 0)
for x in range(1, 5):
    if precios[x] > precios[0]:  # Comparamos cada precio con el precio del primer producto
        cantidad = cantidad + 1  # Si es mayor, aumentamos el contador

# Mostramos el resultado final
print("Cantidad de productos con un precio mayor al primer producto ingresado", cantidad)
