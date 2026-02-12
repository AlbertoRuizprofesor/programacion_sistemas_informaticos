from productos import Producto

class Electrodomestico(Producto):
    def __init__(self, nombre, fabricante, precio,consumo):
        super().__init__(nombre, fabricante, precio)
        self.consumo = consumo
    
    def imprimir(self):
        super().imprimir()
        print(f"Consumo: {self.consumo}")