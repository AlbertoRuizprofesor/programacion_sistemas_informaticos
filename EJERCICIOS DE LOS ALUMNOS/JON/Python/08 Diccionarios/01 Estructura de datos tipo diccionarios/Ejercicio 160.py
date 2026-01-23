print("Ejercicio 160")
print("")
print("")

def cargar():
    productos={}
    for i in range (5):
        nombre=input("Introduce el nombre del producto: ")
        precio=int(input("Introduce el precio del producto: "))
        productos[nombre]=precio
    return productos

def imprimir(productos) :
    print("Listado de artículos y precios: ")
    for nombre in productos:
        print(nombre, productos[nombre])

def imprimir_mayorde100 ( productos ) :
    print("Listado de productos de precio superior a 100")
    for nombre in productos:
        if productos [ nombre ] > 100 :
            print(nombre)
    

listado=cargar()
imprimir(listado)
imprimir_mayorde100(listado)
