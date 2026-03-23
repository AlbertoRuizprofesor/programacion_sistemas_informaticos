#Representa un inventario como una lista de diccionarios con nombre, precio y stock. 
#Crea funciones para añadir productos, buscar por nombre, 
# calcular el valor total del inventario y listar productos con stock bajo.

def agregar_producto(inventario, precio, stock):
inventario.append({"nombre": nombre, "precio", precio, "stock": stock})

def buscar_producto(inventario, nombre):
    for producto in inventario:
        if producto ["nombre"] = nombre():
            return producto
        return None


def stock_bajo(inventario, limite =5):
    return[p for p in inventario if p["stock"]< limite]

inventario = []
agregar_producto(inventario, "monitor", 69.00, 5 )
agregar_producto(inventario, "teclado", 30.50, 2 )
print buscar_producto((inventario, teclado))
print(valor_total(inventario))
print(stock_bajo(inventario))

