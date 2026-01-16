def cargar():
    productos=[]
    for x in range(5):
        nombre=input("Ingrese el nombre del producto:")
        precio=int(input("Ingrese el precio:"))
        productos.append((nombre,precio))
    return productos


def imprimir(productos):
    print("Listado de productos y precios")
    for nombre,precio in productos:
        print(nombre,precio)


def imprimir_entre10y15(productos):
    print("Listado de productos que tienen un precio comprendido entre 10 y 15")
    for nombre,precio in productos:
        if precio>=10 and precio<=15:
            print(nombre,precio)


# bloque main

productos=cargar()
imprimir(productos)
imprimir_entre10y15(productos)