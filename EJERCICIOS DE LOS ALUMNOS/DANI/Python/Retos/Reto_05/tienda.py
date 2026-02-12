# Creacion del PRODUCTO
class Producto:
    # -----ATRIBUTOS-----
    def __init__(self):
        self.producto = input("Producto: ")
        self.stock = 0

    # -----METODOS-----
    def reponer(self):
        ingresar = int(input("¿Cuánto deseas reponer? "))
        self.stock += ingresar
        print(f"Nueva stock: {self.stock}\n")

    def vender(self):
        vendido = int(input("¿Cuánto has vendido? "))
        # Comprobar si tiene la cantidad suficiente para poder sacar dinero
        if vendido <= self.stock:
            self.stock -= vendido
            print(f"Nuevo stock: {self.stock}\n")
        else:
            print("No puedes sacar esa cantidad.\n")

    def retornar_stock(self):
        print(f"Stock actual: {self.stock}\n")
        return self.stock

    def menu(self):
        print("\n-----MENU----")
        while True:
            print("1. Ingresar\n2. Retirar.\n3. Comprobar.\n4. Salir")
            opcion = int(input("Seleccione una opción: "))
            
            match opcion:
                case 1:
                    self.reponer()
                case 2:
                    self.vender()
                case 3:
                    self.retornar_stock()
                case 4:
                    print("Salida exitosa.\n")
                    break # Cerrar while
                case _:
                    print("Opción no válida.\n")

# Creacion de la TIENDA
class Tienda:
    def __init__(self):
        self.producto = Producto()

    def operar(self):
        self.producto.menu()