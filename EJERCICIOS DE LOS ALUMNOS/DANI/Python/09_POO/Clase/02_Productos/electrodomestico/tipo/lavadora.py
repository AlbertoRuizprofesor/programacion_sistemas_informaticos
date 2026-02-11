from electrodomestico.electrodomestico import Electrodomestico

class Lavadora(Electrodomestico):
    def __init__(self, nombre, fabricante, precio, consumo,tipo_carga):
        super().__init__(nombre, fabricante, precio, consumo)
        self.tipo_carga = tipo_carga
    
    def imprimir(self):
        super().imprimir()
        print (f"Tipo de carga: {self.tipo_carga}")