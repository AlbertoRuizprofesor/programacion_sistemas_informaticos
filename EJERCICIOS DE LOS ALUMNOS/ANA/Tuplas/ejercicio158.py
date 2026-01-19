
# 1) Cargar por teclado.
# 2) Listar los productos y precios.
# 3) Imprimir los productos con precios comprendidos entre 10 y 15.

def cargar_datos():

    productos = []

    for i in range(5):

        nombre = input(f"Nombre del producto {i}: ")
        precio = int(input(f"Precio del producto {i}: "))
        productos.append((nombre,precio))

    return productos

def imprmir_productos(productos):

    print("Listado de productos: ")

    for n, p in productos: 
        print(n,p)

def imprimir_productos10y15(productos):

    print("Listado de productos con precio entre 10 y 15: ")

    for n, p in productos: 
        if p >= 10 and p <= 15:
            print(n,p)

# Programa
productos = cargar_datos()
imprmir_productos(productos)
imprimir_productos10y15(productos)