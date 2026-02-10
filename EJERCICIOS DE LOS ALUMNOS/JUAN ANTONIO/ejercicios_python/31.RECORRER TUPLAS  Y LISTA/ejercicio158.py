"""
- Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y cada elemento una tupla con el nombre y el precio. Desarrollar las funciones
1) Cargar por teclado.
2) Listar los productos y precios.
3) Imprimir los productos con precios comprendidos entre 10 y 15.
"""

def cargar_productos():
    """
    Solicita al usuario los datos de 5 productos (nombre y precio)
    y devuelve una lista de tuplas con esa información.
    """
    lista_productos = []
    for i in range(5):
        nombre_producto = input("Ingrese el nombre del producto: ")
        precio_producto = int(input("Ingrese el precio: "))
        lista_productos.append((nombre_producto, precio_producto))
    return lista_productos


def mostrar_productos(lista_productos):
    """
    Muestra todos los productos junto con sus precios.
    """
    print("Listado de productos y precios:")
    for nombre, precio in lista_productos:
        print(nombre, precio)


def mostrar_productos_en_rango(lista_productos):
    """
    Muestra únicamente los productos cuyo precio
    está entre 10 y 15 (incluidos).
    """
    print("Productos con precio entre 10 y 15:")
    for nombre, precio in lista_productos:
        if 10 <= precio <= 15:
            print(nombre, precio)


# Bloque principal

productos_registrados = cargar_productos()
mostrar_productos(productos_registrados)
mostrar_productos_en_rango(productos_registrados)
