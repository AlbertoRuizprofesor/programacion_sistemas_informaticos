print("Ejercicio 136")
print("")
print("")

def cargar_datos():
    articulos = []
    precios = []
    for n in range(5):
        articulo = input(f"Ingrese el nombre del artículo {n+1}: ")
        precio = float(input(f"Ingrese el precio de {articulo}: "))
        articulos.append(articulo)
        precios.append(precio)
    return [articulos, precios]

def mostrar_articulos(lista):
    print("Artículos y sus precios:")
    for n in range(len(lista[0])):
        print(f"{lista[0][n]}: €{lista[1][n]:.2f}")

def mascaro(lista):
    max_precio = max(lista[1])
    indice = lista[1].index(max_precio)
    print(f"El artículo más caro es {lista[0][indice]} con un precio de €{max_precio:.2f}"  )

def buscarpreciomenor(lista):
    precio_buscar = float(input("Ingrese un precio a buscar: "))
    encontrados = []
    for n in range(len(lista[0])):
        if lista[1][n] <= precio_buscar:
            encontrados.append(lista[0][n])
            print(f"Artículo encontrado: {lista[0][n]} con precio €{lista[1][n]:.2f}")


datos = cargar_datos()
mostrar_articulos(datos)
mascaro(datos)
buscarpreciomenor(datos)

print("Fin del programa")
