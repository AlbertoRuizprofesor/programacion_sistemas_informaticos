"""
Confeccionar un programa que permita cargar un código de producto como clave en un diccionario. Guardar para dicha clave el nombre del producto, su precio y cantidad en stock.

Implementar las siguientes actividades:

1) Carga de datos en el diccionario.

2) Listado completo de productos.

3) Consulta de un producto por su clave, mostrar el nombre, precio y stock.

4) Listado de todos los productos que tengan un stock con valor cero.
"""

def cargar_inventario():
    """
    Permite ingresar productos al inventario.
    Cada producto se guarda con:
        - código (clave del diccionario)
        - descripción
        - precio
        - stock actual
    Devuelve un diccionario donde cada clave es un código
    y cada valor es una tupla con (descripción, precio, stock).
    """
    inventario = {}
    continuar = "s"

    while continuar == "s":
        codigo = int(input("Ingrese el código del producto: "))
        descripcion = input("Ingrese la descripción: ")
        precio = float(input("Ingrese el precio: "))
        stock = int(input("Ingrese el stock actual: "))

        inventario[codigo] = (descripcion, precio, stock)

        continuar = input("¿Desea cargar otro producto? [s/n]: ")

    return inventario


def mostrar_inventario(inventario):
    """
    Muestra todos los productos del inventario
    con su código, descripción, precio y stock.
    """
    print("Listado completo de productos:")
    for codigo, datos in inventario.items():
        descripcion, precio, stock = datos
        print(codigo, descripcion, precio, stock)


def consultar_producto(inventario):
    """
    Permite consultar un producto por su código.
    Si existe, muestra su descripción, precio y stock.
    """
    codigo = int(input("Ingrese el código del producto a consultar: "))
    if codigo in inventario:
        descripcion, precio, stock = inventario[codigo]
        print(descripcion, precio, stock)
    else:
        print("No existe un producto con ese código.")


def mostrar_sin_stock(inventario):
    """
    Muestra únicamente los productos cuyo stock es cero.
    """
    print("Listado de artículos con stock en cero:")
    for codigo, datos in inventario.items():
        descripcion, precio, stock = datos
        if stock == 0:
            print(codigo, descripcion, precio, stock)


# Bloque principal

inventario_productos = cargar_inventario()
mostrar_inventario(inventario_productos)
consultar_producto(inventario_productos)
mostrar_sin_stock(inventario_productos)
