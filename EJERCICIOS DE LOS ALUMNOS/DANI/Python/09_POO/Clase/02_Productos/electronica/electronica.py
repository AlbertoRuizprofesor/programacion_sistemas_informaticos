from productos import Producto

class Electronica(Producto):
    def __init__(self,nombre,fabricante,precio,modo):
        super().__init__(nombre,fabricante,precio)
        self.modo = modo

    def mostrar_datos(self):
        super().imprimir()
        print(f"Modo: {self.modo}")