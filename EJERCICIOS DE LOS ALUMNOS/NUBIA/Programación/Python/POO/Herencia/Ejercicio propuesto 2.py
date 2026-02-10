
class Productos:
    def __init__(self, nombre, fabricante, precio):
        self.nombre = nombre
        self.fabricante = fabricante
        self.precio = precio
        
    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Fabricante: {self.fabricante}")
        print(f"Precio: {self.precio}")
        

class Electronica(Productos):
    def __init__(self, nombre, fabricante, precio, modo):
        super().__init__(nombre, fabricante, precio)
        self.modo = modo
    
    def imprimir(self):
        super().imprimir()
        print(f"Modo: {self.modo}")
        
    
# Bloque principal
producto1 = Productos("Funda", "Samsung", 15)
producto1.imprimir()
electronica1 = Electronica("Portátil", "HP", 2000, "gaming")
electronica1.imprimir()