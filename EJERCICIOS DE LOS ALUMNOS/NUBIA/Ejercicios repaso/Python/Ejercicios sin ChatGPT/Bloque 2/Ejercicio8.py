'''
Representa un inventario como una lista de diccionarios con nombre, precio y stock. 
Crea funciones para añadir productos, buscar por nombre, calcular el valor total del inventario y listar productos con stock bajo. 
Idea clave: Considera stock bajo cuando sea menor que 5. 
'''

inventario = []

def añadirProducto():
    nombre = input("Introduce el nombre del producto: ")
    precio = float(input("Introduce el precio del producto: "))
    stock = int(input("Introduce el stock del producto: "))

    nuevoProducto = {"nombre": nombre, "precio": precio, "stock": stock}
    inventario.append(nuevoProducto)
    print(f"Producto {nombre} añadido.")

def buscarProducto():
    nombreBuscado = input("Introduce el nombre del producto a buscar: ")
    for producto in inventario:
        if producto["nombre"].lower() == nombreBuscado.lower():
            print(f"Encontrado: {producto}")
            return producto
        
    print("Producto no encontrado.")
    return None

def listarStockBajo():
    print("--- Productos con bajo stock (Menos de 5) ---")
    stockBajo = False
    for producto in inventario:
        if producto["stock"] < 5:
            print(f"- {producto['nombre']}: {producto['stock']} unidades")
            stockBajo = True
    if not stockBajo:
        print("No hay productos con bajo stock.")

def valorTotal():
    total = sum(p["precio"] * p["stock"] for p in inventario)
    print(f"Valor total del inventario: {total:.2f}€")
    return total

while True:
    print("\nMENÚ DE INVENTARIO")
    opcion = input("1. Añadir producto \n2. Buscar producto \n3. Listar stock bajo \n4. Valor total \n5. Salir \nOpción: ")

    if opcion == "1":
        añadirProducto()
        
    elif opcion == "2":
        buscarProducto()
        
    elif opcion == "3":
        listarStockBajo()
        
    elif opcion == "4":
        valorTotal()
        
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción no válida, intenta de nuevo.")