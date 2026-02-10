from electrodomestico.electrodomestico import Electrodomestico

class Frigorifico(Electrodomestico):
    def __init__(self, nombre, fabricante, precio, consumo, tipo):
        super().__init__(nombre, fabricante, precio, consumo)
        self.tipo = tipo
    
    def imprimir(self):
        super().imprimir()
        print(f"Tipo: {self.tipo}")
