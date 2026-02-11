# Ejercicio 160: Crear un diccionario con 5 productos (nombre y precio).
# Imprimir todos los productos y luego solo aquellos con precio mayor a 100.


# Funciones
def cargar():
    productos = {}
    for x in range(5):
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio: "))
        productos[nombre] = precio
    return productos


def imprimir(productos):
    print("Listado de todos los articulos")
    for nombre in productos:
        print(nombre, productos[nombre])


def imprimir_mayor100(productos):
    print("Listado de articulos con precios mayores a 100")
    for nombre in productos:
        if productos[nombre] > 100:
            print(nombre)


# Bloque Principal

productos = cargar()
imprimir(productos)
imprimir_mayor100(productos)
