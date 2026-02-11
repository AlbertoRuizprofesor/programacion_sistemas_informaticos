# Desarrollar una aplicación que permita ingresar por teclado los nombres de 5 artículos y sus precios. Definir las siguientes funciones:
# 1) Cargar los nombres de artículos y sus precios.
def articulos():
    lista = [[], []]
    for x in range(5):
        print(f"\nArtículo número {x+1}:")
        articulo = input("Artículo: ")
        precio = float(input("Precio: "))
        lista[0].append(articulo)
        lista[1].append(precio)
    return lista

# 2) Imprimir los nombres y precios.
def impresion(lista):
    print("\nRecopilacion de datos: ")
    for i in range(len(lista[0])):
        print(f"El artículo {lista[0][i]} cuesta {lista[1][i]}€")

#3) Imprimir el nombre de artículo con un precio mayor
def mayor_precio(lista):
    mayor_precio = lista[1][0]
    articulo_mayor = lista[0][0]
    for i in range(len(lista[0])):
        if lista[1][i] > mayor_precio: 
            articulo_mayor = lista[0][i]
    print(f"\nEl artículo con el precio mayor es {articulo_mayor}")

# 4) Ingresar por teclado un importe y luego mostrar todos los artículos con un precio menor igual al valor ingresado.
def menos_precio(lista):
    importe = float(input("\nDame un importe: "))
    print(f"Articulos que cuestan menos que {importe}€")
    for i in range(len(lista[0])):
        if lista[1][i] <= importe: 
            print(f"{lista[0][i]}")

# -----PROGRAMA PRINCIPAL-----
datos = articulos()
impresion(datos)
mayor_precio(datos)
menos_precio(datos)