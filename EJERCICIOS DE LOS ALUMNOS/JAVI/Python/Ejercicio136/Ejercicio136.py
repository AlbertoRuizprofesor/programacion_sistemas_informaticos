"""
Desarrollar una aplicación que permita ingresar por teclado los nombres de 5 artículos y sus precios. 
Definir las siguientes funciones:
1) Cargar los nombres de artículos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y luego mostrar todos los artículos con un precio menor igual al valor ingresado.
"""

def cargar_datos(articulos, precios):
    articulos = []
    precios = []
    for x in range(5):
        art = input("Introduce un articulo: ")
        articulos.append(art)
        precio = float(input("Introduce su precio: "))
        precios.append(precio)

    return articulos, precio

def imprimir(articulos, precios):
    print("Lista de articulos y su precio: ")
    for x in range(len(articulos)):
        print(articulos[x], precios[x])

def mayor(articulos, precios):
    mayor = precios [0]
    posicion = 0
    for x in range(1, len(precios)):
        if precios[x] > mayor:
            mayor = precios[x]
            posicion = x

    print("El articulo con mas caro es: " , articulos[posicion], " precio: " , mayor)



    
    


