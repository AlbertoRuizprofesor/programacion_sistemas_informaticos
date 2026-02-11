from menu.menu import menu

producto = menu()

if producto:
    print("\nDatos del producto creada:")
    producto.imprimir()