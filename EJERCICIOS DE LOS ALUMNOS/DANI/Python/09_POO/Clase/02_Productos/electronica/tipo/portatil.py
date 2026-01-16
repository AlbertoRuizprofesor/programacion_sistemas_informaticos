from ..electronica import Electronica

class Portatil(Electronica):
    def __init__(self, nombre, fabricante, precio, modo,ram):
        super().__init__(nombre, fabricante, precio, modo)
        self.ram = ram
        
    def imprimir(self):
        super().imprimir()
        print(f"RAM: {self.ram}")