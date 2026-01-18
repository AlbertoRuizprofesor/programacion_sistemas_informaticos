#Desarrollar una aplicación que permita ingresar por teclado los nombres de 5 artículos y sus precios. Definir las siguientes funciones:
#1) Cargar los nombres de artículos y sus precios.
#2) Imprimir los nombres y precios.
#3) Imprimir el nombre de artículo con un precio mayor
#4) Ingresar por teclado un importe y luego mostrar todos los artículos con un precio menor igual al valor ingresado.


# ---------------------------------------------------------
# FUNCIÓN: cargar_datos
# Carga 5 artículos y sus precios en listas paralelas.
# Devuelve ambas listas dentro de una lista contenedora.
# ---------------------------------------------------------
def cargar_datos():
    articulos = []   # Lista para los nombres de los artículos
    precios = []     # Lista para los precios correspondientes

    for x in range(5):
        ar = input("Ingrese el nombre del articulo:")
        articulos.append(ar)   # Guardamos el nombre del artículo

        pre = int(input("Ingrese el precio de dicho articulo:"))
        precios.append(pre)    # Guardamos el precio del artículo

    return [articulos, precios]   # Devolvemos ambas listas


# ---------------------------------------------------------
# FUNCIÓN: imprimir
# Muestra todos los artículos junto con sus precios.
# ---------------------------------------------------------
def imprimir(articulos, precios):
    print("Listado completo de articulos y sus precios")
    for x in range(len(articulos)):
        print(articulos[x], precios[x])


# ---------------------------------------------------------
# FUNCIÓN: precio_mayor
# Busca el artículo con el precio más alto y lo muestra.
# ---------------------------------------------------------
def precio_mayor(articulos, precios):
    may = precios[0]   # Suponemos que el primer precio es el mayor
    pos = 0            # Guardamos su posición

    # Recorremos desde el segundo elemento en adelante
    for x in range(1, len(precios)):
        if precios[x] > may:   # Si encontramos un precio mayor...
            may = precios[x]   # Actualizamos el valor máximo
            pos = x            # Guardamos la posición del artículo

    print("Articulo con un precio mayor es:", articulos[pos], "su precio es:", may)


# ---------------------------------------------------------
# FUNCIÓN: consulta_precio
# Pide un valor y muestra los artículos cuyo precio es menor.
# ---------------------------------------------------------
def consulta_precio(articulos, precios):
    valor = int(input("Ingrese un importe para mostrar los articulos con un precio menor:"))
    for x in range(len(precios)):
        if precios[x] < valor:   # Si el precio es menor al valor ingresado...
            print(articulos[x], precios[x])


# ---------------------------------------------------------
# BLOQUE PRINCIPAL DEL PROGRAMA
# ---------------------------------------------------------

articulos, precios = cargar_datos()   # Cargamos los datos
imprimir(articulos, precios)          # Mostramos la lista completa
precio_mayor(articulos, precios)      # Mostramos el artículo más caro
consulta_precio(articulos, precios)   # Consultamos artículos por precio

