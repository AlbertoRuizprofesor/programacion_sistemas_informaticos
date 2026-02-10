#Reto 3:
"""Resultado:
Factura nº: 1
Producto: Portatil HP GAME
precio: 2000

iva: 420
total: 2420"""

class Factura:
    def __init__(self,factura="",producto="",precio=""):
        self.factura=factura
        self.producto=producto
        self.precio=precio
    def calculo(self):
        iva=420
        total=self.precio+iva
        print(f"Factura {self.factura}:")
        print(f"Producto: {self.producto} con un precio de {self.precio} euros.")
        print(f"Total con IVA del 21%:", total,"euros.")

factura1=Factura(1,"Portatil HP GAME",2000)
factura1.calculo()
