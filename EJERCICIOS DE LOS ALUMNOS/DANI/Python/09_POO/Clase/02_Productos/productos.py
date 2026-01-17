class Producto:
    def __init__(self,nombre,fabricante,precio):
        self.nombre = nombre
        self.fabricante = fabricante
        self.precio = precio
    
    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Fabricante: {self.fabricante}")
        print(f"Precio: {self.precio}")