# Ejercicio 8. Gestión de inventario
# Representa un inventario como una lista de diccionarios con
# nombre, precio y stock. Crea funciones para añadir productos,
# buscar por nombre, calcular el valor total del inventario
# y listar productos con stock bajo.
# Idea clave: Considera stock bajo cuando sea menor que 5.


def agregar_producto(lista, nombre, precio, stock):
    lista.append({"nombre": nombre, "precio": precio, "stock": stock})


def buscar_producto(lista, nombre):
    for producto in lista:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None


def valor_total_inventario(lista):
    valor_total = 0
    for producto in lista:
        valor_total += producto["precio"] * producto["stock"]
    return valor_total


def stock_bajo(lista):
    productos_bajos = []
    for producto in lista:
        if producto["stock"] < 5:
            productos_bajos.append(producto)
    return productos_bajos


# Main ejemplo
inventario = []

agregar_producto(inventario, "Laptop", 1000, 10)
agregar_producto(inventario, "Mouse", 25, 3)
agregar_producto(inventario, "Teclado", 50, 2)
agregar_producto(inventario, "Monitor", 200, 8)
agregar_producto(inventario, "Impresora", 150, 1)

print("\nProducto buscado:", buscar_producto(inventario, "Mouse"))
print("\nValor total del inventario:", valor_total_inventario(inventario))
print("\nProductos con stock bajo:", stock_bajo(inventario))
