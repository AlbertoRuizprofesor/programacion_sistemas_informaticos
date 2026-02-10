"""
Reto 3

Resultado:
Factura nº: 1
Producto: Portatil HP GAME
precio: 2000

iva: 420
total: 2420

"""

class Factura:

    def __init__(self, producto, precio):
        self.producto = producto
        self.precio = precio

    def calcular_iva(self):
        iva = self.precio * 0.21
        return iva
    
factura1 = Factura("HP", 2000)
print(f"El iva es: {factura1.calcular_iva()}")
print("El precio total es:", factura1.precio + factura1.calcular_iva())
                                                       

    

