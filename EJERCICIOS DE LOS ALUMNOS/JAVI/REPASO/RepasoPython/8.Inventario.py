def agregar_producto(inventario, nombre, precio, stock):
    inventario.append({"nombre": nombre, "precio": precio, "stock": stock})

def buscar_producto(inventario, nombre):
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None

def valor_total(inventario):
    total = 0
    for producto in inventario:
        total += producto["precio"] * producto["stock"]
    return total

def stock_bajo(inventario, limite=5):
    return [p for p in inventario if p["stock"] < limite]

inventario = []
agregar_producto(inventario, "Teclado", 25.5, 3)
agregar_producto(inventario, "Ratón", 14.9, 12)
print(buscar_producto(inventario, "teclado"))
print(valor_total(inventario))
print(stock_bajo(inventario))
