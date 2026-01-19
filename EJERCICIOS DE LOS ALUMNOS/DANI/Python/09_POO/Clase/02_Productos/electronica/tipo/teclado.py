from ..electronica import Electronica

class Teclado(Electronica):
    def __init__(self, nombre, fabricante, precio, modo,ergonomico):
        super().__init__(nombre, fabricante, precio, modo)
        self.ergonomico = ergonomico
    
    def imprimir(self):
        super().imprimir()
        print(f"Ergnomico: {self.ergonomico}")