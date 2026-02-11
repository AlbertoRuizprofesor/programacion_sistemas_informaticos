from ..electronica import Electronica

class Monitor(Electronica):
    def __init__(self, nombre, fabricante, precio, modo, pulgada):
        super().__init__(nombre, fabricante, precio, modo)
        self.pulgada = pulgada
    
    def imprimir(self):
        super().imprimir()
        print(f"Pulgadas: {self.pulgada} ")