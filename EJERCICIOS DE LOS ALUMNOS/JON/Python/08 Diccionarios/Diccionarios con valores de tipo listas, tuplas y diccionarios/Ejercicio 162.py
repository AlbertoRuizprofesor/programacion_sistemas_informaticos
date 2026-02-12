print("Ejercicio 163")
print("")
print("")

def cargar():
    productos={}
    continua="s"
    while continua=="s":
        
        codigo=int(input("Introduce el codigo del artículo: "))
        descripcion=input("Introduce la descripción del artículo: ")
        precio=float(input("Introduce el precio del artículo: "))
        stock=int(input("Introduce el stock actual del artículo: "))
        productos[codigo]={descripcion,precio,stock}
        continua=input("Desea cargar otro artículo? (s/n)")
    return productos

def imprimir(productos):
    print("Lista completa de artículos")
    for codigo in productos:
        print(codigo, productos [codigo][0], productos[codigo][1], productos[codigo][2])

def consulta(productos):
    art=int(input("Introduce el código del artículo: "))
    if art in productos:
        print(productos[art][0],productos[art][1],productos[art][2])
        
def sinstock(productos):
    print("Listado de artículos sin stock: ")
    for codigo in productos:
        if productos[codigo][2]==0:
            print(codigo, productos[codigo][0],productos[codigo][1],productos[codigo][2])


almacen=cargar()
imprimir(almacen)
consulta(almacen)
sinstock(almacen)

        
