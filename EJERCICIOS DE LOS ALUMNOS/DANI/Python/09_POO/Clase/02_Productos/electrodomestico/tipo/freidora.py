from electrodomestico.electrodomestico import Electrodomestico

class Freidora(Electrodomestico):
    def __init__(self, nombre, fabricante, precio, consumo, temp_max):
        super().__init__(nombre, fabricante, precio, consumo)
        self.temp_max = temp_max
    
    def imprimir(self):
        super().imprimir()
        print(f"Temperatura máxima: {self.temp_max}")