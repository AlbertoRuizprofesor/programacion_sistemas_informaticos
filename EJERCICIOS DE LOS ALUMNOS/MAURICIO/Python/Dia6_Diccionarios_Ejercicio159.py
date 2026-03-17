productos = {"PORTATIL": 39, "RATONES": 45, "TECLADOS": 50}
print(productos)
print(productos["RATONES"])  # Imprime 45
for clave in productos:
    print("Clave:", clave, "Valor:", productos[clave])
print("Listado de productos y sus códigos:")
for clave, valor in productos.items():
    print("Producto:", clave, "Código:", valor)
