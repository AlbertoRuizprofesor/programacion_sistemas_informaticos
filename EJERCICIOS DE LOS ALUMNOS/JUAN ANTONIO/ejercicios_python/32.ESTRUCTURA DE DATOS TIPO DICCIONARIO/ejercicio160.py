"""
Crear un diccionario que permita almacenar 5 artículos, utilizar como clave el nombre de productos y como valor el precio del mismo.

Desarrollar además las funciones de:

1) Imprimir en forma completa el diccionario

2) Imprimir solo los artículos con precio superior a 100.
"""

def cargar_productos():
    """
    Solicita al usuario el nombre y precio de 5 productos
    y los almacena en un diccionario donde:
        - clave: nombre del producto
        - valor: precio del producto
    Devuelve el diccionario completo.
    """
    inventario = {}
    for i in range(5):
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio_producto = int(input("Ingrese el precio: "))
        inventario[nombre_producto] = precio_producto
    return inventario


def mostrar_productos(inventario):
    """
    Muestra todos los productos del diccionario
    junto con sus precios.
    """
    print("Listado de todos los artículos:")
    for nombre, precio in inventario.items():
        print(nombre, precio)


def mostrar_productos_caros(inventario):
    """
    Muestra únicamente los productos cuyo precio
    es mayor a 100.
    """
    print("Artículos con precio mayor a 100:")
    for nombre, precio in inventario.items():
        if precio > 100:
            print(nombre)


# Bloque principal

productos_registrados = cargar_productos()
mostrar_productos(productos_registrados)
mostrar_productos_caros(productos_registrados)
